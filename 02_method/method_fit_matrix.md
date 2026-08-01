# Research Question and Method-Fit Matrix

## 2.1. Refined research question

> To what extent can a pretrained YOLO26n object detector locate and distinguish three pharmaceutical pill types in the held-out MEDISEG test set?

## 2.2. Candidate methods

| Method | Description |
|---|---|
| **Method 1 - Transfer learning for object detection** | Fine-tune a pretrained compact YOLO detector on the labeled MEDISEG `3pills` subset and evaluate it on a held-out test partition. |
| **Method 2 - Classical computer vision** | Engineer color, contour, texture, and shape features, followed by rule-based localization and classification. |
| **Method 3 - Unadapted pretrained inference** | Apply a generic pretrained detector without supervised fine-tuning on the three MEDISEG classes. |

## 2.3. E.D.F.C.V. matrix

Scores range from 1 (weak fit) to 5 (strong fit).

| Criterion | Method 1 | Method 2 | Method 3 |
|---|---:|---:|---:|
| **E - Epistemological fit** | 5 | 5 | 4 |
| **D - Data availability** | 5 | 5 | 5 |
| **F - Feasibility for the course deadline** | 5 | 3 | 5 |
| **C - Contribution to the research question** | 5 | 3 | 2 |
| **V - Venue and disciplinary fit** | 5 | 3 | 2 |
| **Total** | **25** | **19** | **18** |

The scores organize the justification but do not substitute for methodological reasoning.

## 2.4. Selected method

Method 1 was selected because it directly addresses both components of the question: locating pill instances and distinguishing among the three labeled types. Transfer learning also makes the experiment feasible within the course deadline while retaining a rigorous train-validation-test design.

YOLO26n was chosen as a compact baseline rather than as proof that it is universally superior. The experiment evaluates one predefined architecture and one seed; it is not an architecture-comparison study.

## 2.5. Why the alternatives were not selected

Classical computer vision would require handcrafted thresholds that are sensitive to illumination, reflections, background, orientation, and within-class visual variation. It remains a possible baseline for future comparison, but it is less suitable as the main method for this short study.

Unadapted pretrained inference is faster but cannot directly predict the MEDISEG class identifiers because those labels are absent from generic pretraining taxonomies. It therefore has poor construct fit with the stated outcome.

## 2.6. Executed design

- Public MEDISEG v2 `3pills` subset.
- 2,333 images split deterministically into training (1,633), validation (350), and test (350).
- Pretrained YOLO26n fine-tuned using seed 42, image size 640, batch size 16, maximum 40 epochs, and early-stopping patience 8.
- Final reporting on the isolated test set using precision, recall, mAP@0.50, and mAP@0.50:0.95.

## 2.7. Open methodological tension

The image-level split contains no exact duplicate files across partitions, but MEDISEG does not provide acquisition-session identifiers. Near-duplicate or correlated captures cannot therefore be ruled out completely. In addition, one training seed does not quantify run-to-run variability. These limitations constrain generalization beyond the reported benchmark.
