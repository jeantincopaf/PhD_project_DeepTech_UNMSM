# First Technical Proof of Concept: MEDISEG Pill Detection

## Relationship to AI-DOTS

This folder contains the first small reproducible artifact developed within the broader **AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis** project. It preserves the original exploratory baseline and a later confirmatory robustness extension completed after instructor feedback.

The purpose of this proof of concept is limited and sequential: before developing the complete ingestion-verification system, it tests whether a compact computer-vision model can locate and distinguish pills in controlled static images.

This experiment does **not** replace or modify the original research question, paradigm, selected method, literature review, or research protocol. It also does not evaluate tuberculosis medicines, swallowing, adherence, patients, or clinical effectiveness.

## Proof-of-concept question

> Can a pretrained object detector be fine-tuned to detect and distinguish three pharmaceutical pill types in the MEDISEG dataset under a reproducible train-validation-test procedure?

## Contents

```text
05_pipeline/
├── notebook.ipynb
├── README.md
├── src/
│   ├── verify_artifacts.py
│   └── verify_confirmatory_artifacts.py
└── results/
    ├── README.md
    ├── test_metrics.json
    ├── dataset_summary.json
    ├── environment.json
    ├── split_manifest.csv
    ├── data.yaml
    ├── SHA256SUMS.txt
    ├── figures/
    ├── predictions/
    ├── training/
    └── confirmatory/
        ├── README.md
        ├── model_screening_results.csv
        ├── model_selection.json
        ├── multiseed_test_results.csv
        ├── multiseed_summary.csv
        ├── multiseed_metrics_mean_sd.png
        ├── experiment_config.json
        ├── environment.json
        ├── split_manifest.csv
        ├── run_metadata/
        └── SHA256SUMS.txt
```

## Data and exploratory baseline

- Dataset: MEDISEG v2, `3pills` subset
- DOI: `10.25383/city.28574786.v2`
- Dataset archive MD5: `64d851d97d85de706e941539d48bbd72`
- Images: 2,333
- Split: 1,633 training, 350 validation, and 350 test images
- Classes: `HK-65191`, `HK-44618`, and `HK-62094`
- Model: pretrained YOLO26n
- Seed: 42
- Reported runtime: Google Colab Pro with NVIDIA L4 GPU

The archived exploratory baseline used early stopping and one training seed. It remains available for historical traceability and is not presented as the final robustness result.

## Confirmatory robustness extension

The extension uses the same immutable image-level split and adds:

- screening of YOLO26n, YOLO11n, and RT-DETR-L on validation only;
- 40 complete epochs for all eight executions, with `patience=1000`;
- a predeclared `0.01` validation-mAP tie margin and lower-parameter tie-breaker;
- YOLO26n evaluation with seeds 7, 21, 42, 84, and 123; and
- mean, standard deviation, range, and descriptive 95% t intervals.

YOLO26n was selected because all three detectors were within the tie margin and it had the fewest parameters. Across five seeds, held-out test mAP@0.50:0.95 was `0.9515 ± 0.0054`. Full results and limitations are documented in [`results/confirmatory/`](results/confirmatory/README.md).

## Reproduce the experiment

1. Upload `notebook.ipynb` to Google Colab.
2. Select a GPU runtime.
3. Run the setup and data-preparation cells in order. The notebook downloads the official MEDISEG archive and rejects it if its byte size or MD5 checksum does not match.
4. Run the original training section to reproduce the historical baseline, if required.
5. Run the confirmatory section to screen three detectors and execute the selected model with five seeds. Expect several hours on an NVIDIA L4 because eight 40-epoch runs are performed.
6. Compare the generated tables and split manifest with `results/confirmatory/`.

The raw MEDISEG images and trained weights are not committed here. The notebook retrieves the official data and regenerates the model checkpoint.

## Verify the archived artifacts

From the repository root:

```bash
python 05_pipeline/src/verify_artifacts.py 05_pipeline/results
python 05_pipeline/src/verify_confirmatory_artifacts.py 05_pipeline/results/confirmatory
```

The first command verifies the historical baseline. The second checks the confirmatory hashes, split, three-model screening, locked selection rule, eight complete training histories, five seeds, and recomputed summary statistics.

## Interpretation boundary

The result is evidence for a first controlled pill-detection proof of concept within AI-DOTS. It is not evidence that the complete proposed system detects ingestion or improves tuberculosis-treatment adherence.
