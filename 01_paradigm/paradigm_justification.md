# Paradigm Justification Statement

## 1. Research Topic and Context

Tuberculosis remains a public health priority in Peru and worldwide. According to the latest WHO Global Tuberculosis Report 2025, an estimated 10.7 million people were infected globally in 2024, and Peru registered 33,049 cases that same year according to MINSA. In Peru, the Directly Observed Treatment, Short-course (DOTS) strategy is used for medication administration, which requires in-person supervision by healthcare workers to verify that patients are taking their medication. However, this strategy is very costly and logistically unfeasible in remote and marginalized areas.

My tentative topic is the development of a computer vision system capable of classifying the type/brand of tuberculosis pills and subsequently detecting pill intake in real time. This solution aims to reduce the burden on healthcare centers and improve patient adherence to treatment, particularly in areas where in-person DOTS supervision is not viable.

## 2. Preliminary Research Question

Can a computer vision system designed for pill detection and swallowing validation detect medication use in tuberculosis treatment?

## 3. Chosen Paradigm and Justification

The most appropriate starting point for this study is a **quantitative empirical (positivist) paradigm**. The reason is straightforward: the central question will be answered by the algorithm's performance metrics (accuracy, precision, recall, F1-score) and not by subjective interpretations. The system must be evaluated through objective, measurable outcomes on controlled test sets.

I am **not** choosing an interpretivist paradigm as the main frame because I am not seeking to understand the lived experiences of patients, their perceptions of treatment, or their subjective adherence behaviors. While such insights could be valuable in a later implementation phase, they do not answer the immediate technical question about whether the computer vision system can correctly classify pills and detect ingestion.

I am also **not** choosing a design science paradigm as the primary one at this stage. While design science could eventually evaluate the clinical utility of the system, its full evaluation in real patients with active tuberculosis cannot be conducted due to ethical restrictions. A pilot study with healthy patients who consume pills daily and have a non-contagious condition can validate the technical feasibility of this work without exposing vulnerable populations to risk.

I am likewise **not** using mixed methods as the central framing for this phase. Mixed methods would make sense if the study were already designed to integrate algorithm performance evaluation with patient interviews, usability testing, or clinical outcome tracking. At the moment, the question remains mainly technical and quantitative, and forcing a mixed label too early would make the design sound broader than it really is.

## 4. Implications of the Paradigm Choice

The paradigm choice points clearly toward controlled dataset generation and algorithmic evaluation. It requires:

- A dataset of photos of tuberculosis pill brands with different shapes and dimensions
- A dataset with video frames of medication ingestion
- Iterative development of the device with robustness tests for lighting, occlusion, and camera angles
- Quasi-experimental evaluation where neural network architectures are compared on controlled test sets
- Cross-validation to ensure generalizability of results

The expected contribution is both technical and practical. A validated computer vision pipeline could serve as a foundation for remote medication adherence monitoring in tuberculosis treatment, with potential extension to other chronic diseases requiring supervised medication intake.

## 5. One Doubt or Tension

The main tension is the gap between technical validation and clinical deployment. The system can be validated for pill classification and ingestion detection accuracy in controlled settings, but its real-world effectiveness in improving tuberculosis treatment adherence depends on factors beyond the algorithm itself: patient acceptance, healthcare integration, regulatory approval, and ethical clearance for use with active TB patients. The safest route is to establish a rigorous technical baseline first, then design a phased validation strategy that moves from controlled lab conditions to simulated environments and eventually to supervised pilot testing with healthy volunteers.