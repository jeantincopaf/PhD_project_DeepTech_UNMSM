# Retracted Paper Analysis

## 1. Paper selected

**Original article:** Saranya, M., & Praveena, R. (2025). *Accurate and real-time brain tumour detection and classification using optimized YOLOv5 architecture*. Scientific Reports, 15, 25286. https://doi.org/10.1038/s41598-025-07773-1

**Retraction notice:** Saranya, M., & Praveena, R. (2026). *Retraction Note: Accurate and real-time brain tumour detection and classification using optimized YOLOv5 architecture*. Scientific Reports, 16, 12859. https://doi.org/10.1038/s41598-026-47630-3

**Status:** Retracted by the editors on 20 April 2026. The authors disagreed with the retraction.

### AI assistance disclosure

Codex was used to support source discovery, organize the document, assist with English and Markdown drafting, and check factual statements against the publisher's article and retraction notice. Prompt text is not reproduced in this repository. The author reviewed the evidence and approved the interpretation, conclusion, and final submitted version.

## 2. Why this case was selected

This case is directly relevant to AI-DOTS because it applies YOLO to a high-stakes medical imaging task. The AI-DOTS proof of concept also uses a YOLO-family detector, although its present scope is limited to detecting pills in MEDISEG images and does not make diagnostic or clinical-effectiveness claims. The retracted paper therefore provides a useful integrity case: high performance numbers are not sufficient when the data lineage, experimental procedure, and result-generation process cannot be independently verified.

## 3. What the article claimed

The article described a hybrid framework combining a Fully Convolutional Neural Network (FCNN/FCCN) with YOLOv5 for brain-tumour classification, localization, and segmentation in MRI images. Its reported claims included:

- an average classification accuracy of 98.80%;
- real-time tumour detection using YOLOv5;
- an inference speed of 48 frames per second;
- statistical comparisons against U-Net and DeepLabV3 using a Wilcoxon signed-rank test over ten runs per model; and
- potential suitability for clinical and telemedicine settings.

The article linked its data-availability statement to a public Kaggle brain MRI classification dataset. However, availability of a general source link is not equivalent to a reproducible data snapshot. A reproducible study also requires the exact dataset version, included files, exclusions, labels, preprocessing, split assignments, and integrity checks used to generate the reported results.

## 4. Official reason for retraction

The official notice states that concerns were first raised about non-standard terminology. The journal's subsequent investigation identified problems concerning the underlying data and the reporting of analyses and results. According to the editors, these problems prevented independent verification of the findings. The authors were asked for an explanation, but the response did not resolve the concerns, so the editors lost confidence in the reliability of the article.

The notice does **not** state that fabrication, falsification, or plagiarism was proven. It is therefore inappropriate to assign motives or allege misconduct beyond the published evidence. The defensible conclusion is narrower: the journal determined that the article's content was insufficiently reliable and verifiable to remain in the scientific record. This distinction is consistent with COPE guidance that a retraction notice should identify why findings are unreliable and distinguish proven misconduct from error or other causes.

## 5. Integrity and reproducibility assessment

| Area | Evidence visible in the article | Integrity concern |
|---|---|---|
| Dataset identity | A Kaggle dataset link is supplied. | The statement does not identify an immutable dataset version, file manifest, checksum, or retrieval date. |
| Dataset partition | The method gives generic ranges such as 70-80% training and 10-15% validation/test. | Generic ranges do not disclose the actual split, exact counts, patient-level grouping, or image identifiers used in each subset. |
| Leakage control | The paper discusses augmentation and splitting in general terms. | It is not possible to determine from the report whether related images from the same subject were isolated across partitions before augmentation. |
| Code and environment | No code-availability section or executable repository is visible in the current article record. | The model, optimizer, preprocessing, and statistical calculations cannot be independently rerun from the publication alone. |
| Randomness | Random augmentation and ten-run comparisons are described. | Seeds, per-run configurations, and per-run outputs are not reported, so the claimed variability cannot be reconstructed. |
| Metric traceability | Accuracy, F1, mAP, specificity, FPS, and p-values are reported in different sections. | The connection between datasets, tasks, denominators, thresholds, runs, and reported metrics is not sufficiently explicit for independent checking. |
| Statistical evidence | Wilcoxon p-values and summary means/standard deviations are presented for ten runs. | The paired observations, pairing rule, hypotheses, confidence intervals, and analysis code are not supplied. The p-values therefore cannot be verified from the report. |
| Clinical claims | The discussion suggests clinical and telemedicine usefulness. | There is no visible external clinical validation, prospective evaluation, deployment test, or evidence of patient-level benefit supporting those claims. |
| Audit response | The editors requested an explanation after concerns were raised. | The published notice states that the response was not satisfactory and that independent verification remained impossible. |

## 6. Warning signs that should have triggered closer review

### 6.1 Method descriptions without executable specificity

Statements that a dataset was split into "usually" or "typically" used percentages describe common practice rather than the exact experiment. A reviewer should request exact counts, split manifests, patient-level grouping rules, and a deterministic script.

### 6.2 Exceptional performance without a complete audit trail

Very high accuracy can be genuine, but in medical imaging it increases the need to rule out leakage, duplicated images, hidden preprocessing differences, class imbalance effects, and test-set reuse. The article's reported 98.80% accuracy is not independently testable from the materials linked in the record.

### 6.3 Mixing task definitions and metrics

Classification, object detection, and segmentation require different labels and metrics. Accuracy, mAP, F1-score, specificity, and FPS are not interchangeable. Each reported value should identify the task, dataset partition, decision threshold, averaging method, uncertainty, and exact model checkpoint.

### 6.4 Clinical extrapolation beyond the validation design

A model tested on a public image dataset cannot be described as clinically ready without external validation, representative patient sampling, ethical and regulatory review, and prospective evaluation. Technical performance is evidence of technical performance only.

### 6.5 Missing computational materials

Scientific Reports' policies require a code-availability statement for studies whose custom code or algorithms are central to the conclusions, and they emphasize data availability sufficient for replication and verification. A dataset link alone does not reconstruct the experiment.

## 7. What would have made the study auditable

At minimum, the publication package should have contained:

1. a versioned dataset citation with retrieval date, license, checksum, and file manifest;
2. documented inclusion and exclusion criteria and class counts;
3. patient-level train/validation/test manifests created before augmentation;
4. source code for preprocessing, training, evaluation, figures, and statistical tests;
5. pinned dependencies, hardware information, random seeds, and deterministic settings;
6. model configuration, hyperparameters, checkpoint-selection rule, and saved weights;
7. per-run results for all ten trials and confidence intervals or effect sizes;
8. unambiguous definitions for every metric and the data partition on which it was calculated;
9. an external validation set from a different source; and
10. restrained conclusions that separate benchmark performance from clinical utility.

## 8. Lessons transferred to AI-DOTS

This case changes how evidence should be presented in the AI-DOTS project:

- **Preserve scope.** The MEDISEG experiment is a first proof of concept for pill detection. It does not validate swallowing, adherence, tuberculosis outcomes, or clinical deployment.
- **Freeze the data.** Record the dataset release, license, image and annotation counts, retrieval date, and SHA-256 hashes or DVC-tracked artifact identifiers.
- **Publish the split.** Keep exact train/validation/test manifests and prevent near-duplicate or related images from crossing partitions.
- **Make the run deterministic.** Record seeds, model configuration, software versions, hardware, image size, epochs, early-stopping rule, and checkpoint-selection criterion.
- **Retain primary outputs.** Preserve machine-readable metrics, plots, logs, weights, and integrity hashes, not only screenshots or selected figures.
- **Define every number.** State the unit of analysis, class averaging, IoU thresholds, confidence threshold, and dataset partition for each metric.
- **Separate evidence from aspiration.** Future ingestion validation and clinical testing must be presented as planned phases, not as results of the pill-detection proof of concept.
- **Respond to audit requests.** Materials needed to verify a result should be retained and made available under the ethical and legal conditions defined in the Data Management Plan.

## 9. Conclusion

The central lesson is not that YOLO is unreliable. The problem is that a reported result becomes scientifically fragile when an independent reader cannot reconstruct how the data, code, model, and analysis produced it. Retraction protects the scientific record when unresolved problems remove confidence in published findings. For AI-DOTS, integrity therefore requires a traceable chain from source data to split, configuration, checkpoint, metric, figure, and claim, together with conclusions that remain inside the demonstrated scope.

## References

1. Saranya, M., & Praveena, R. (2025). *Accurate and real-time brain tumour detection and classification using optimized YOLOv5 architecture*. Scientific Reports, 15, 25286. https://doi.org/10.1038/s41598-025-07773-1
2. Saranya, M., & Praveena, R. (2026). *Retraction Note: Accurate and real-time brain tumour detection and classification using optimized YOLOv5 architecture*. Scientific Reports, 16, 12859. https://doi.org/10.1038/s41598-026-47630-3
3. Committee on Publication Ethics. (2019). *Retraction Guidelines*. https://doi.org/10.24318/cope.2019.1.4
4. Scientific Reports. (n.d.). *Editorial and publishing policies: Availability of materials, data, and computer code*. https://www.nature.com/srep/journal-policies/editorial-policies
