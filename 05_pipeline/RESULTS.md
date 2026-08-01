# Experiment Results

## Execution status

- Model: YOLO26n pretrained checkpoint.
- Dataset: MEDISEG v2 `3pills` subset.
- Test images: 350.
- Maximum epochs: 40.
- Completed epochs: 12.
- Stop reason: early stopping with patience 8.
- Best validation epoch: 4.
- Hardware: NVIDIA L4 GPU.

## Held-out test metrics

| Metric | Value |
|---|---:|
| Precision | 0.9288 |
| Recall | 0.8980 |
| mAP@0.50 | 0.9740 |
| mAP@0.50:0.95 | 0.9174 |

### Per-class mAP@0.50:0.95

| Class | Value |
|---|---:|
| HK-65191 | 0.9075 |
| HK-44618 | 0.9172 |
| HK-62094 | 0.9275 |

The best validation mAP@0.50:0.95 was 0.9232 and the final test value was 0.9174. Their absolute difference was approximately 0.0058, with no large validation-test degradation.

## Confidence threshold and confusion matrix

The F1-confidence curve reaches an overall maximum F1 of approximately 0.91 at a confidence threshold of approximately 0.51. This is the most defensible initial operating point for this experiment.

The exported confusion matrix reflects the threshold used by the evaluation routine that generated it. It contains 638 class-correct detections, 7 cross-class confusions, 18 missed objects, and 140 predictions assigned against background. Because error counts change with confidence threshold, a deployment-oriented matrix should be regenerated explicitly at `conf=0.51`.

## Data-integrity audit

The split manifest contains 2,333 unique image IDs and filenames. A local SHA-256 audit found no exact duplicate image content within or across the training, validation, and test partitions. All referenced source images were present during the audit.

This check does not exclude near-duplicate or correlated captures because acquisition-session identifiers are not available in the dataset metadata used by the pipeline.

## Interpretation

The experiment provides evidence that YOLO26n can detect and distinguish the three selected pill classes with high internal test performance in MEDISEG.

It does **not** establish:

- recognition of Peruvian tuberculosis medicines;
- swallowing or medication-ingestion verification;
- medication-adherence measurement;
- clinical effectiveness or patient benefit;
- robustness in homes, health facilities, or mobile devices;
- external generalization to other datasets or pill types.

## Reproducibility status

The repository preserves the data checksum, seed, split manifest, class map, environment, training arguments, epoch history, best checkpoint, test metrics, and principal figures. A complete independent rerun has not yet been performed, so reproducibility is documented but not independently confirmed.

## Suggested result statement

> On the held-out MEDISEG `3pills` test set (350 images), the fine-tuned YOLO26n detector achieved a precision of 0.929, recall of 0.898, mAP@0.50 of 0.974, and mAP@0.50:0.95 of 0.917. These results establish an internal technical baseline for three-class pill detection and should not be interpreted as evidence of ingestion verification or clinical readiness.
