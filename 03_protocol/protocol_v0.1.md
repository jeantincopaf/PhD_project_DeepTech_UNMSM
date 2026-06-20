# Research Protocol Outline (v0.1)

## 1. Working Title

AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis.

## 2. Problem and Context

Adherence to treatment for active tuberculosis in Peru requires patients to physically attend health centers for Directly Observed Treatment, Short-course (DOTS) supervision. This strategy is very costly and logistically unfeasible in remote and marginalized areas. The project focuses on developing a computer vision system capable of classifying the type/brand of tuberculosis pills and subsequently detecting pill intake in real time, as a potential technological alternative to in-person DOTS supervision.

## 3. Rationale

The study matters because tuberculosis is a public health priority in Peru and worldwide, with 33,049 cases registered in Peru in 2024 according to MINSA. Current DOTS strategy imposes a heavy logistical and economic burden on both healthcare systems and patients, particularly those in rural or resource-limited settings. A validated computer vision system could reduce the burden on healthcare centers, improve patient access to supervised treatment, and potentially increase adherence rates by enabling remote medication verification.

## 4. General Research Question

Can a computer vision system designed for pill detection and swallowing validation detect medication use in tuberculosis treatment?

## 5. Specific Questions and Working Hypothesis

The study asks how accurately the system can classify tuberculosis pill brands under varying conditions, how reliably it can detect the ingestion action in real-time video, and which neural network architectures and robustness conditions yield the most consistent performance. The working hypothesis is that a purpose-built deep learning pipeline can achieve acceptable accuracy for both pill classification and ingestion detection under controlled but realistic conditions, though performance will degrade predictably under adverse lighting, occlusion, or extreme camera angles.

## 6. Research Paradigm

The study adopts a quantitative empirical (positivist) paradigm because the central question will be answered by the algorithm's performance metrics and not by subjective interpretations. This is a better fit than interpretivist or design science approaches for the present phase, given that clinical utility in real tuberculosis patients cannot be evaluated due to ethical restrictions.

## 7. Study Design and Data Source

The proposed design is a controlled technical validation study using two generated datasets:
- A dataset of photos of tuberculosis pill brands with different shapes and dimensions
- A dataset with video frames of medication ingestion by healthy participants

The population of interest for the pilot phase is healthy individuals who consume pills daily and have a non-contagious condition, serving as proxies for the technical validation of the ingestion detection module.

## 8. Main Variables

**Outcome variables:**
- Pill classification accuracy (correct brand/type identification)
- Ingestion detection precision/recall (correct swallowing validation)
- Real-time processing speed (frames per second)

**Main explanatory/control variables:**
- Neural network architecture (ResNet, EfficientNet, YOLO, LSTM variants)
- Lighting conditions (natural, artificial, low-light)
- Occlusion level (partial hand coverage, full hand coverage)
- Camera angle (frontal, lateral, overhead)
- Pill brand/type (specific to Peru's national tuberculosis program)

## 9. Analysis Plan

The analysis will begin with descriptive performance metrics for each architecture on the controlled test set, followed by robustness testing under varying conditions. Cross-validation will be used to ensure generalizability. Subgroup comparisons will examine performance degradation across lighting, occlusion, and angle conditions. Survey design features are not applicable here, but dataset balancing and augmentation strategies will be documented to ensure methodological defensibility.

## 10. Ethics, Limitations, and Timeline

The project uses controlled datasets with healthy volunteers rather than tuberculosis patients, so direct clinical risk is low. However, the study must avoid overstating clinical readiness or implying that the system is ready for deployment in active tuberculosis care without further validation. A preliminary 36-month timeline is envisioned, beginning with dataset generation and architecture selection, moving through iterative development and robustness testing, and ending with pilot validation, manuscript writing, and thesis integration.