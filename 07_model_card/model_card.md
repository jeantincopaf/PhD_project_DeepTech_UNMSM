# Model Card: MEDISEG-3Pills YOLO26n Proof of Concept

**Documentation scorecard:** 8/8 (self-audited and updated on 4 August 2026)

## 1. Model details

- **Model name/version:** MEDISEG-3Pills YOLO26n Proof of Concept v0.2
- **Model type:** YOLO26n single-stage object detector initialized from pretrained weights
- **Input/output:** 640 x 640 RGB still images; bounding boxes, confidence scores, and labels `HK-65191`, `HK-44618`, or `HK-62094`
- **Owner/contact:** Jean Pierre Tincopa Flores, jean.tincopaf@unmsm.edu.pe, [GitHub](https://github.com/jeantincopaf)
- **Context:** UNMSM Research Methods and Scientific Integrity course
- **Training/evaluation:** exploratory baseline in June 2026; confirmatory extension completed 4 August 2026
- **Artifact repository license:** **UNKNOWN - license not yet specified.** MEDISEG is CC BY 4.0; upstream code and pretrained weights retain their own terms. No combined software/model license is asserted.

This is the first proof of concept within the broader AI-DOTS doctoral project. It does not replace or modify the original research protocol.

## 2. Intended use

The intended use is research and teaching: testing whether a reproducible computer-vision pipeline can localize and distinguish three pill categories in controlled MEDISEG still images. Intended users are the researcher, course reviewers, and researchers auditing the pipeline.

The model is **not intended** for:

- clinical diagnosis, prescription, dispensing, or treatment decisions;
- identifying pills outside the three listed MEDISEG classes;
- recognizing tuberculosis medication as a general category;
- detecting swallowing, ingestion, adherence, or patient behavior;
- use with patients, real-time video, mobile deployment, or autonomous clinical monitoring;
- substituting professional verification or directly observed therapy.

Any such use is misuse or out of scope because it has not been evaluated.

## 3. Factors

Performance may vary with illumination, camera angle, scale, blur, reflections, pill orientation, occlusion, overlap, background, dosette-box geometry, capture device, and class imbalance.

No people or demographic attributes are included, so demographic subgroup analysis is not applicable. Relevant disaggregation is by pill class and, in future work, acquisition conditions. Acquisition-session identifiers were unavailable; correlated or near-duplicate captures across splits cannot be completely ruled out even though exact content duplicates were checked.

## 4. Metrics

Reported metrics are box precision, box recall, mAP@0.50, and mAP@0.50:0.95. Per-class mAP@0.50:0.95 exposes differences hidden by aggregate results.

These metrics apply only to the held-out MEDISEG subset. They do not measure general pill identity, ingestion, adherence, safety, clinical benefit, latency, calibration, or deployment robustness. No deployment confidence threshold has been validated.

## 5. Evaluation data

The held-out test split contains 350 MEDISEG v2 3-pills images and 663 annotations: 275 `HK-65191`, 166 `HK-44618`, and 222 `HK-62094`. It was generated deterministically with `seed=42` and was not used for fitting or early stopping.

The pipeline found no exact image-content duplicates across train, validation, and test. Acquisition-session grouping is unavailable, so independence of visually related captures is **UNKNOWN - to investigate**. No external devices, environments, populations, or tuberculosis medicines were evaluated.

## 6. Training data

MEDISEG v2 3-pills contains 2,333 annotated images. The deterministic split contains 1,633 training, 350 validation, and 350 test images. Model selection used only the validation split.

The historical exploratory YOLO26n baseline used pretrained weights, maximum 40 epochs, batch size 16, image size 640, patience 8, deterministic execution, automatic mixed precision, and `seed=42`. Training stopped after 12 epochs; best validation mAP@0.50:0.95 was 0.9232 at epoch 4.

The confirmatory extension retained the same image split and screened YOLO26n, YOLO11n, and RT-DETR-L for 40 complete epochs using validation only. All candidates used batch size 8, image size 640, AdamW, learning rate 0.001, weight decay 0.0005, `workers=0`, deterministic mode, and `patience=1000`. The predeclared rule selected YOLO26n, which was then trained with seeds 7, 21, 42, 84, and 123. Environment, arguments, split manifest, checksums, notebook, and run histories are under `05_pipeline/`. See the accompanying [Datasheet](datasheet.md).

## 7. Quantitative analyses

Historical exploratory held-out test results:

| Metric | Value |
|---|---:|
| Precision | 0.9288 |
| Recall | 0.8980 |
| mAP@0.50 | 0.9740 |
| mAP@0.50:0.95 | 0.9174 |

Disaggregated held-out test results:

| Pill class | Test instances | mAP@0.50:0.95 |
|---|---:|---:|
| `HK-65191` | 275 | 0.9075 |
| `HK-44618` | 166 | 0.9172 |
| `HK-62094` | 222 | 0.9275 |

The per-class range was 0.0200, lowest for `HK-65191`. These values are retained as historical point estimates.

Confirmatory detector screening on validation:

| Detector | Parameters | Validation mAP@0.50:0.95 |
|---|---:|---:|
| RT-DETR-L | 32,970,476 | 0.9579 |
| YOLO26n | 2,572,280 | 0.9541 |
| YOLO11n | 2,624,080 | 0.9530 |

All candidates were within the predeclared 0.01 tie margin, so the lower-parameter tie-breaker selected YOLO26n without using the test partition.

Confirmatory YOLO26n held-out test results across five seeds:

| Metric | Mean | Standard deviation | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Precision | 0.9784 | 0.0140 | 0.9566 | 0.9934 |
| Recall | 0.9709 | 0.0168 | 0.9419 | 0.9826 |
| mAP@0.50 | 0.9913 | 0.0043 | 0.9841 | 0.9940 |
| mAP@0.50:0.95 | 0.9515 | 0.0054 | 0.9426 | 0.9557 |

The two seed-42 executions were close but not byte-identical: validation mAP@0.50:0.95 was 0.9541 during screening and 0.9524 during the multi-seed phase. This is metric-level stability in the documented GPU environment, not a claim of exact binary determinism. Results remain internal to this image-level split and do not demonstrate external or clinical generalization.

## 8. Ethical considerations

No people or patient data are present. The main ethical risk is misuse: a high detection score could be mistaken for proof that a person swallowed medication or adhered to tuberculosis treatment. That unsupported inference could create false reassurance, punitive monitoring, privacy intrusion, or unsafe clinical decisions.

Mitigations are explicit scope restrictions, per-class reporting, reproducibility artifacts, no clinical deployment, human review, and separation from the future human-participant study in the original protocol. Patient-facing work would require ethics approval, informed consent, privacy/data governance, usability and bias evaluation, external validation, failure procedures, and meaningful human oversight. Formal collection governance beyond public MEDISEG documentation is **UNKNOWN - to investigate**.

## 9. Caveats and recommendations

- Three controlled labels do not establish general pill recognition.
- Extend multi-seed evaluation to external datasets and acquisition-group-aware splits.
- Use acquisition-group identifiers and group-aware splits when available.
- Test external phones, lighting, backgrounds, occlusions, pill brands, and failure cases.
- Evaluate calibration, inference speed, thresholds, uncertainty, and false-negative consequences.
- Weights are not distributed; the notebook regenerates them. Resolve the artifact license before redistribution.
- Evaluate future ingestion/adherence components separately under the original protocol and ethical oversight.
