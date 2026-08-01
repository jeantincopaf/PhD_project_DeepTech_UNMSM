# Executed Research Protocol (v0.2)

## 1. Title

Reproducible Detection of Three Pharmaceutical Pill Types with YOLO26n: A Technical Validation Study Using MEDISEG.

## 2. Scope

This protocol describes the course experiment that was actually executed. It is narrower than the long-term AI-DOTS doctoral direction. It evaluates object detection in static images and does not evaluate swallowing, adherence, tuberculosis medicines, patients, or clinical outcomes.

## 3. Research question

To what extent can a pretrained YOLO26n object detector locate and distinguish three pharmaceutical pill types in the held-out MEDISEG test set?

## 4. Objective

To train and evaluate a reproducible three-class pill object detector using a public labeled dataset and a held-out test partition.

## 5. Study design

Controlled computational experiment with transfer learning and a fixed train-validation-test split. The unit of analysis is an annotated pill instance contained in a MEDISEG image.

## 6. Data source

- Dataset: MEDISEG v2, `3pills` subset.
- Persistent identifier: DOI `10.25383/city.28574786.v2`.
- Archive MD5 recorded by the pipeline: `64d851d97d85de706e941539d48bbd72`.
- Total images: 2,333.
- Classes: `HK-65191`, `HK-44618`, and `HK-62094`.

The notebook downloads the official archive, verifies its checksum, audits COCO annotation integrity, and converts valid annotations to YOLO format. The original images are not redistributed in the repository.

## 7. Partitioning

Images were sorted and assigned with seed 42:

| Partition | Images |
|---|---:|
| Training | 1,633 |
| Validation | 350 |
| Test | 350 |

The file-level assignment is preserved in `05_pipeline/results/split_manifest.csv`. The test partition was reserved for the final evaluation.

## 8. Model and training

- Architecture: pretrained YOLO26n.
- Image size: 640 x 640 pixels.
- Batch size: 16.
- Maximum epochs: 40.
- Early-stopping patience: 8 epochs.
- Seed: 42.
- Deterministic option: enabled.
- Accelerator used: NVIDIA L4 GPU.
- Software: Python 3.12.13, PyTorch 2.11.0+cu128, Ultralytics 8.4.102.

Default Ultralytics augmentations recorded in `args.yaml` were applied. Model selection used validation performance; the test partition was not used for early stopping.

## 9. Outcomes

Primary outcome:

- mAP@0.50:0.95 on the held-out test set.

Secondary outcomes:

- mAP@0.50;
- precision;
- recall;
- per-class mAP@0.50:0.95;
- confusion matrix and qualitative prediction examples.

## 10. Analysis plan

The final checkpoint (`best.pt`) is evaluated once on the held-out test partition. Overall and per-class metrics are reported without null-hypothesis significance tests because the experiment is a benchmark evaluation rather than a group-comparison study.

The F1-confidence curve is used to identify an operating confidence threshold. For deployment-oriented interpretation, the confusion matrix should be regenerated at the selected threshold rather than assumed to represent every possible operating point.

## 11. Reproducibility controls

- fixed seed and deterministic split procedure;
- archive checksum and dataset summary;
- complete split manifest;
- recorded environment and training arguments;
- training history, evaluation plots, best checkpoint, and test metrics;
- SHA-256 checksums for repository result artifacts.

GPU execution and stochastic augmentation may still produce minor differences across platforms. A single completed run does not estimate multi-seed variability.

## 12. Ethics

This experiment uses an existing public image dataset and involves no recruitment, intervention, questionnaire, identifiable patient information, or clinical decision-making. Dataset licensing and attribution requirements remain applicable.

## 13. Limitations

- Only three MEDISEG classes were evaluated.
- The classes are not established here as tuberculosis medicines used in Peru.
- The data represent static pill images, not ingestion video.
- No external dataset was used.
- No acquisition-session grouping was available to rule out correlated captures.
- Only one model family and one seed were evaluated.
- Metrics from a curated dataset do not establish clinical predictive value.

## 14. Predefined interpretation boundary

A strong result supports technical feasibility for three-class pill detection within MEDISEG. It must not be presented as swallowing verification, medication-adherence measurement, clinical validation, or readiness for tuberculosis care.
