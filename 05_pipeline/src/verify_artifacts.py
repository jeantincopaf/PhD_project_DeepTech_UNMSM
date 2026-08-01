"""Verify the archived MEDISEG proof-of-concept artifacts.

Usage:
    python 05_pipeline/src/verify_artifacts.py 05_pipeline/results
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


EXPECTED_SPLITS = {"train": 1633, "val": 350, "test": 350}
EXPECTED_CLASSES = ["HK-65191", "HK-44618", "HK-62094"]
EXPECTED_TEST_IMAGES = 350


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"Expected a JSON object: {path}")
    return value


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
        actual = sha256(path)
        assert actual == expected.lower(), f"SHA-256 mismatch: {relative}"
        checked += 1
    assert checked > 0, "No checksums were found."
    return checked


def verify_manifest(root: Path) -> Counter:
    with (root / "split_manifest.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == sum(EXPECTED_SPLITS.values()), "Unexpected manifest length."
    assert len({row["image_id"] for row in rows}) == len(rows), "Duplicate image IDs."
    assert len({row["file_name"] for row in rows}) == len(rows), "Duplicate filenames."
    counts = Counter(row["split"] for row in rows)
    assert dict(counts) == EXPECTED_SPLITS, f"Unexpected split counts: {dict(counts)}"
    return counts


def verify_metadata(root: Path) -> dict:
    metrics = load_json(root / "test_metrics.json")
    summary = load_json(root / "dataset_summary.json")
    environment = load_json(root / "environment.json")

    assert metrics["test_images"] == EXPECTED_TEST_IMAGES
    assert summary["split_images"] == EXPECTED_SPLITS
    assert summary["class_names"] == EXPECTED_CLASSES
    for name in ("precision", "recall", "mAP50", "mAP50_95"):
        value = float(metrics[name])
        assert 0.0 <= value <= 1.0, f"Metric outside [0, 1]: {name}={value}"
    assert set(metrics["per_class_mAP50_95"]) == set(EXPECTED_CLASSES)
    for key in ("python", "torch", "ultralytics", "gpu"):
        assert environment.get(key), f"Missing environment field: {key}"
    return metrics


def verify_training_history(root: Path) -> int:
    with (root / "training" / "results.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 12, f"Expected 12 completed epochs, found {len(rows)}."
    return len(rows)


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "05_pipeline/results").resolve()
    assert root.is_dir(), f"Results directory not found: {root}"
    checked = verify_hashes(root)
    splits = verify_manifest(root)
    metrics = verify_metadata(root)
    epochs = verify_training_history(root)
    print("Artifact verification: PASS")
    print(f"Files checked by SHA-256: {checked}")
    print(f"Split counts: {dict(splits)}")
    print(f"Completed epochs: {epochs}")
    print(f"Test mAP@0.50:0.95: {metrics['mAP50_95']:.6f}")


if __name__ == "__main__":
    main()
