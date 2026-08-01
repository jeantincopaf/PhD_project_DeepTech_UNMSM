# First Technical Proof of Concept: MEDISEG Pill Detection

## Relationship to AI-DOTS

This folder contains the first small reproducible artifact developed within the broader **AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis** project.

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
│   └── verify_artifacts.py
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
    └── training/
```

## Data and model

- Dataset: MEDISEG v2, `3pills` subset
- DOI: `10.25383/city.28574786.v2`
- Dataset archive MD5: `64d851d97d85de706e941539d48bbd72`
- Images: 2,333
- Split: 1,633 training, 350 validation, and 350 test images
- Classes: `HK-65191`, `HK-44618`, and `HK-62094`
- Model: pretrained YOLO26n
- Seed: 42
- Reported runtime: Google Colab Pro with NVIDIA L4 GPU

## Reproduce the experiment

1. Upload `notebook.ipynb` to Google Colab.
2. Select a GPU runtime.
3. Run every cell from top to bottom.
4. The notebook downloads the official MEDISEG archive and rejects it if its byte size or MD5 checksum does not match.
5. It audits the COCO annotations, creates the deterministic split, converts the labels, trains YOLO26n, evaluates the isolated test set, and packages the artifacts.
6. Compare the generated metrics and split manifest with the files in `results/`.

The raw MEDISEG images and trained weights are not committed here. The notebook retrieves the official data and regenerates the model checkpoint.

## Verify the archived artifacts

From the repository root:

```bash
python 05_pipeline/src/verify_artifacts.py 05_pipeline/results
```

The command checks the recorded hashes, JSON files, split counts, class mapping, metric ranges, and expected training history.

## Interpretation boundary

The result is evidence for a first controlled pill-detection proof of concept within AI-DOTS. It is not evidence that the complete proposed system detects ingestion or improves tuberculosis-treatment adherence.
