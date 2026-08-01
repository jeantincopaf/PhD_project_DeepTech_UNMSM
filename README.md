# Reproducible Detection of Three Pharmaceutical Pill Types with YOLO26n

**Author:** Jean Pierre Tincopa Flores<br>
**University:** Universidad Nacional Mayor de San Marcos (UNMSM)<br>
**Program:** PhD in Deep Tech focused on Artificial Intelligence and Emerging Technologies<br>
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies

## Study scope

This repository reports a controlled technical baseline for detecting three pharmaceutical pill types in MEDISEG images. It is a deliberately reduced and executable course study within the broader AI-DOTS research direction.

The present experiment addresses only **pill localization and class identification in static images**. It does not evaluate swallowing, medication adherence, tuberculosis patients, clinical effectiveness, or deployment in health services.

## Research question

> To what extent can a pretrained YOLO26n object detector locate and distinguish three pharmaceutical pill types in the held-out MEDISEG test set?

## Data and experimental design

- Dataset: MEDISEG v2, `3pills` subset ([DOI: 10.25383/city.28574786.v2](https://doi.org/10.25383/city.28574786.v2))
- Classes: `HK-65191`, `HK-44618`, and `HK-62094`
- Images: 2,333
- Deterministic split, seed 42: 1,633 training, 350 validation, and 350 test images
- Model: pretrained YOLO26n, fine-tuned at 640 x 640 pixels
- Maximum training: 40 epochs, patience 8, batch size 16
- Execution environment: Google Colab Pro with NVIDIA L4 GPU

The test partition remained isolated until final model evaluation. The complete assignment of files is recorded in `05_pipeline/results/split_manifest.csv`.

## Main results

| Test metric | Value |
|---|---:|
| Precision | 0.9288 |
| Recall | 0.8980 |
| mAP@0.50 | 0.9740 |
| mAP@0.50:0.95 | 0.9174 |

Training stopped after epoch 12 through early stopping. The best validation mAP@0.50:0.95 occurred at epoch 4 (0.9232). The held-out test result was 0.9174, a difference of approximately 0.0058.

Detailed metrics, figures, model weights, environment information, and limitations are documented in [`05_pipeline/RESULTS.md`](05_pipeline/RESULTS.md).

## Repository structure

| Folder | Content |
|---|---|
| `01_paradigm/` | Quantitative empirical paradigm justification |
| `02_method/` | Method-fit matrix for the executed technical study |
| `03_protocol/` | Original protocol and current executable protocol v0.2 |
| `04_literature/` | Broader AI-DOTS literature review and PRISMA materials |
| `05_pipeline/` | Colab notebook, results, figures, manifest, and best checkpoint |

## Reproduction

1. Open `05_pipeline/MEDISEG_3Pills_YOLO26_Colab.ipynb` in Google Colab.
2. Select a GPU runtime; the reported run used an NVIDIA L4.
3. Run the notebook from top to bottom.
4. Confirm the dataset checksum and audit gates.
5. Compare the generated `test_metrics.json` and split manifest with the archived artifacts.

The original MEDISEG images are not redistributed in this repository. The notebook downloads the official archive and verifies its checksum before use.

## Interpretation boundary

The results support technical feasibility within a three-class curated image dataset. They do not establish clinical validity, medication ingestion, adherence improvement, or performance for tuberculosis medicines used in Peru. These are later phases of the broader doctoral project and require new data, ethics review, and external validation.

**Last updated:** 1 August 2026
