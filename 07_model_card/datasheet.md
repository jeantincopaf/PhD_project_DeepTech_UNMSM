# Datasheet: MEDISEG v2 3-Pills Subset Used in the Proof of Concept

## 1. Motivation

MEDISEG supports research on medication recognition using annotated pill images. It has a controlled 3-pills component and a diverse 32-pills component. This project uses only 3-pills as a reproducible object-detection proof of concept; it is not a tuberculosis, swallowing, or adherence dataset.

The dataset is MEDISEG v2 by William Chu on City St George's, University of London Figshare: [DOI 10.25383/city.28574786.v2](https://doi.org/10.25383/city.28574786.v2). The accompanying paper is *MEDISEG: An Extensible Deep Learning Framework and Dataset for Multi-Pill Detection, Segmentation and Recognition* by Chu, Hirani, Tarroni, and Li: [arXiv:2603.10825](https://arxiv.org/abs/2603.10825).

## 2. Composition

The subset contains 2,333 images and three classes: `HK-65191`, `HK-44618`, and `HK-62094`. MEDISEG provides COCO instance masks, bounding boxes, and class labels; this experiment uses only bounding boxes and class labels for YOLO detection.

| Split | Images | `HK-65191` | `HK-44618` | `HK-62094` |
|---|---:|---:|---:|---:|
| Train | 1,633 | 1,332 | 827 | 1,066 |
| Validation | 350 | 293 | 188 | 234 |
| Test | 350 | 275 | 166 | 222 |
| **Total** | **2,333** | **1,900** | **1,181** | **1,522** |

Counts after the image column are annotation instances. No people, patient records, demographic attributes, tuberculosis status, prescriptions, ingestion events, or adherence outcomes are included. Acquisition-session identifiers and systematic condition labels are **UNKNOWN - not supplied in the proof-of-concept artifacts**.

## 3. Collection process

**How collected:** The paper states that 3-pills images were photographed with an iPhone 12 Pro Max, with pills in a standard 4 x 7 dosette box. Artificial-light intensity and angle were manipulated; images include different orientations, occlusions, overlaps, and reflections. Classes were selected for subtle shape/color similarities.

Multiple annotators manually labeled images in COCO Annotator following guidelines, with initial annotation and secondary error review. Pill metadata uses Hong Kong drug registration information. Exact dates, session count, annotator identities, inter-annotator agreement, and compensation are **UNKNOWN - not reported in accessible documentation**.

No human subjects are depicted. A formal ethics-review statement was not identified in the accessible record or paper; whether an institutional determination was obtained is **UNKNOWN - to investigate**.

## 4. Preprocessing / cleaning / labeling

The paper states that images were cropped, padded, and resized to 640 x 640. The notebook verifies the archive, audits image/annotation consistency, converts boxes to YOLO format, and creates a deterministic split with `seed=42`.

The archive `MEDISEG.tar.gz` is 439,343,024 bytes with MD5 `64d851d97d85de706e941539d48bbd72`. The pipeline recorded a split manifest and found no exact content duplicates across splits. Session-level independence and correlated near-duplicates remain unknown because grouping identifiers were unavailable. This project did not manually relabel the source.

## 5. Uses

Appropriate uses are research, teaching, reproducibility exercises, and baselines for the three represented pill classes under similar conditions.

The dataset **should not be used** to:

- infer swallowing, ingestion, adherence, or patient behavior;
- support clinical decisions without representative data and governance;
- identify arbitrary pills, tuberculosis medicines, counterfeit products, dosage, or treatment correctness;
- make decisions about individual patients;
- estimate demographic fairness, because no people or demographic labels are present;
- claim real-world generalization from the controlled subset alone.

Future users should preserve class identifiers, record transformations, use group-aware splits if possible, and report per-class and aggregate results.

## 6. Distribution

MEDISEG v2 is distributed through [Figshare](https://doi.org/10.25383/city.28574786.v2) under CC BY 4.0. Users should cite it and its paper and comply with the current license.

Raw images are not committed here. The notebook downloads the official archive and verifies size and MD5. This repository retains derived split metadata, configuration, metrics, figures, and checksums. Additional restrictions on any externally incorporated item are **UNKNOWN - verify the current official record before redistribution**.

## 7. Maintenance

The authoritative source is the versioned Figshare item. The accessed v2 release was published 12 May 2026. William Chu is listed as dataset creator; the paper lists William Chu, Shashi Hirani, Giacomo Tarroni, and Ling Li.

Users should check the DOI for corrections or newer versions. Update cadence, deprecation policy, response time, and long-term maintenance are **UNKNOWN - not specified**. This project does not control the dataset. Proof-of-concept questions: Jean Pierre Tincopa Flores, jean.tincopaf@unmsm.edu.pe.
