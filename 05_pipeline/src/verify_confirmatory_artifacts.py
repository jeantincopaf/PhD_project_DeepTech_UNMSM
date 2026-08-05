"""Verify curated MEDISEG confirmatory robustness artifacts.

Usage:
    python 05_pipeline/src/verify_confirmatory_artifacts.py \
        05_pipeline/results/confirmatory
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import statistics
import sys
from collections import Counter
from pathlib import Path


EXPECTED_SPLITS = {"train": 1633, "val": 350, "test": 350}
EXPECTED_MODELS = {"yolo26n", "yolo11n", "rtdetr_l"}
EXPECTED_SELECTED_MODEL = "yolo26n"
EXPECTED_SEEDS = {7, 21, 42, 84, 123}
EXPECTED_EPOCHS = 40
EXPECTED_RUNS = {
    "screening_yolo26n_seed42": 42,
    "screening_yolo11n_seed42": 42,
    "screening_rtdetr_l_seed42": 42,
    "multiseed_yolo26n_seed7": 7,
    "multiseed_yolo26n_seed21": 21,
    "multiseed_yolo26n_seed42": 42,
    "multiseed_yolo26n_seed84": 84,
    "multiseed_yolo26n_seed123": 123,
}
SUMMARY_METRICS = (
    "test_precision",
    "test_recall",
    "test_mAP50",
    "test_mAP50_95",
)
T_CRITICAL_95_DF4 = 2.776


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    assert isinstance(value, dict), f"Expected a JSON object: {path}"
    return value


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert rows, f"CSV has no data rows: {path}"
    return rows


def verify_hashes(root: Path) -> int:
    checksum_file = root / "SHA256SUMS.txt"
    checked = 0
    for raw_line in checksum_file.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        expected, relative = line.split(maxsplit=1)
        path = root / relative.strip()
        assert path.is_file(), f"Missing artifact: {relative}"
        assert sha256(path) == expected.lower(), f"SHA-256 mismatch: {relative}"
        checked += 1
    assert checked > 0, "No checksums were found."
    return checked


def verify_manifest(root: Path) -> Counter:
    rows = load_csv(root / "split_manifest.csv")
    assert len(rows) == sum(EXPECTED_SPLITS.values())
    assert len({row["image_id"] for row in rows}) == len(rows)
    assert len({row["file_name"] for row in rows}) == len(rows)
    counts = Counter(row["split"] for row in rows)
    assert dict(counts) == EXPECTED_SPLITS, counts
    return counts


def verify_screening_and_selection(root: Path) -> tuple[list[dict[str, str]], dict]:
    rows = load_csv(root / "model_screening_results.csv")
    assert len(rows) == 3
    assert {row["model_key"] for row in rows} == EXPECTED_MODELS
    assert all(int(row["training_seed"]) == 42 for row in rows)
    assert all(int(row["epochs_completed"]) == EXPECTED_EPOCHS for row in rows)
    assert all(0.0 <= float(row["val_mAP50_95"]) <= 1.0 for row in rows)
    assert not any(column.startswith("test_") for column in rows[0])

    selection = load_json(root / "model_selection.json")
    best_map = max(float(row["val_mAP50_95"]) for row in rows)
    near_best = [
        row for row in rows
        if float(row["val_mAP50_95"]) >= best_map - float(selection["tie_margin"])
    ]
    expected = min(
        near_best,
        key=lambda row: (int(row["parameters"]), -float(row["val_mAP50_95"])),
    )
    assert selection["selected_model"] == expected["model_key"]
    assert selection["selected_model"] == EXPECTED_SELECTED_MODEL
    assert selection["test_used_for_selection"] is False
    return rows, selection


def verify_multiseed_and_summary(root: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = load_csv(root / "multiseed_test_results.csv")
    assert len(rows) == 5
    assert {int(row["training_seed"]) for row in rows} == EXPECTED_SEEDS
    assert {row["model_key"] for row in rows} == {EXPECTED_SELECTED_MODEL}
    assert all(int(row["epochs_completed"]) == EXPECTED_EPOCHS for row in rows)
    for row in rows:
        for metric in SUMMARY_METRICS:
            assert 0.0 <= float(row[metric]) <= 1.0

    summary_rows = load_csv(root / "multiseed_summary.csv")
    summary_by_metric = {row["metric"]: row for row in summary_rows}
    assert set(summary_by_metric) == set(SUMMARY_METRICS)

    for metric in SUMMARY_METRICS:
        values = [float(row[metric]) for row in rows]
        mean = statistics.mean(values)
        sd = statistics.stdev(values)
        half_width = T_CRITICAL_95_DF4 * sd / math.sqrt(len(values))
        expected_values = {
            "n_seeds": len(values),
            "mean": mean,
            "standard_deviation": sd,
            "minimum": min(values),
            "maximum": max(values),
            "ci95_lower_descriptive": mean - half_width,
            "ci95_upper_descriptive": mean + half_width,
        }
        recorded = summary_by_metric[metric]
        assert int(recorded["n_seeds"]) == expected_values["n_seeds"]
        for key, expected_value in expected_values.items():
            if key == "n_seeds":
                continue
            assert math.isclose(
                float(recorded[key]), expected_value, rel_tol=1e-12, abs_tol=1e-12
            ), f"Summary mismatch: {metric} {key}"
    return rows, summary_rows


def yaml_scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(\S+)", text)
    assert match, f"Missing YAML field: {key}"
    return match.group(1)


def verify_run_metadata(root: Path) -> int:
    metadata_root = root / "run_metadata"
    actual_runs = {path.name for path in metadata_root.iterdir() if path.is_dir()}
    assert actual_runs == set(EXPECTED_RUNS), actual_runs

    for run_name, expected_seed in EXPECTED_RUNS.items():
        run_dir = metadata_root / run_name
        history = load_csv(run_dir / "results.csv")
        assert len(history) == EXPECTED_EPOCHS, run_name
        assert int(float(history[0]["epoch"])) == 1
        assert int(float(history[-1]["epoch"])) == EXPECTED_EPOCHS

        args = (run_dir / "args.yaml").read_text(encoding="utf-8-sig")
        assert int(yaml_scalar(args, "epochs")) == EXPECTED_EPOCHS
        assert int(yaml_scalar(args, "patience")) == 1000
        assert int(yaml_scalar(args, "seed")) == expected_seed
        assert yaml_scalar(args, "deterministic").lower() == "true"
        assert int(yaml_scalar(args, "workers")) == 0
    return len(actual_runs)


def verify_configuration(root: Path) -> dict:
    config = load_json(root / "experiment_config.json")
    environment = load_json(root / "environment.json")
    dataset = load_json(root / "dataset_summary.json")

    assert config["split_images"] == EXPECTED_SPLITS
    assert config["training_seeds"] == sorted(EXPECTED_SEEDS)
    assert config["epochs"] == EXPECTED_EPOCHS
    assert config["patience"] == 1000
    assert config["early_stopping_effectively_disabled"] is True
    assert dataset["split_images"] == EXPECTED_SPLITS
    for key in ("python", "torch", "ultralytics", "gpu"):
        assert environment.get(key), f"Missing environment field: {key}"
    assert not list(root.rglob("*.pt")), "Model checkpoints must not be committed here."
    return environment


def main() -> None:
    root = Path(
        sys.argv[1] if len(sys.argv) > 1 else "05_pipeline/results/confirmatory"
    ).resolve()
    assert root.is_dir(), f"Confirmatory results directory not found: {root}"

    hashes = verify_hashes(root)
    splits = verify_manifest(root)
    _, selection = verify_screening_and_selection(root)
    multiseed, summary = verify_multiseed_and_summary(root)
    runs = verify_run_metadata(root)
    environment = verify_configuration(root)

    map_summary = next(row for row in summary if row["metric"] == "test_mAP50_95")
    print("Confirmatory artifact verification: PASS")
    print(f"Files checked by SHA-256: {hashes}")
    print(f"Split counts: {dict(splits)}")
    print(f"Detector candidates: {len(EXPECTED_MODELS)}")
    print(f"Selected model: {selection['selected_model']}")
    print(f"Complete training runs: {runs}")
    print(f"Final seeds: {sorted(int(row['training_seed']) for row in multiseed)}")
    print(
        "Test mAP@0.50:0.95 mean +/- SD: "
        f"{float(map_summary['mean']):.6f} ± "
        f"{float(map_summary['standard_deviation']):.6f}"
    )
    print(f"Environment: {environment['gpu']}, Ultralytics {environment['ultralytics']}")


if __name__ == "__main__":
    main()
