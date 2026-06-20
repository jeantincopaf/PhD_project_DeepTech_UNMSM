# Research Question and Method-Fit Matrix

## 2.1. Refined Research Question

To what extent can a computer vision system accurately classify tuberculosis pill brands and detect real-time pill ingestion, and which neural network architectures and robustness conditions are most strongly associated with reliable medication verification performance?

## 2.2. Three Candidate Methods

| Method | Short Description |
|---|---|
| **Method 1 - Controlled dataset + deep learning pipeline** | Generate labeled datasets of pill images and ingestion video frames, then train and compare CNN-based architectures (ResNet, EfficientNet, YOLO) for classification and action detection, with robustness testing under varying lighting, occlusion, and camera angles. |
| **Method 2 - Transfer learning with existing medical image datasets** | Use publicly available pill image datasets and pre-trained video action recognition models, fine-tuning them for tuberculosis pill classification and ingestion detection without collecting original data. |
| **Method 3 - Rule-based computer vision (traditional CV)** | Implement classical image processing techniques (color thresholding, edge detection, template matching, optical flow) to identify pills and detect swallowing motions without deep learning, relying on handcrafted features and heuristic rules. |

## 2.3. E.D.F.C.V. Matrix

| Criterion | What it asks | Method 1 | Method 2 | Method 3 |
|---|---|---:|---:|---:|
| **E - Epistemological fit** | Does the method match the quantitative/positivist paradigm? | 5 | 5 | 5 |
| **D - Data availability** | Can the required data be accessed realistically? | 4 | 5 | 4 |
| **F - Feasibility** | Can it be done well within the present course stage? | 5 | 3 | 4 |
| **C - Contribution type** | Does it answer the actual question being asked? | 5 | 3 | 2 |
| **V - Venue fit** | Does it fit likely computer vision and health informatics venues? | 5 | 4 | 2 |
| **Total** |  | **24** | **20** | **17** |

The matrix supports the choice, but it does not replace judgment. The point is to defend the method, not just to score it.

## 2.4. Why Method 1 Wins

Method 1 is the best fit because the question explicitly asks about a computer vision system designed for tuberculosis pill classification and real-time ingestion detection. Generating controlled datasets with the specific pill brands used in Peru's DOTS program and testing under realistic conditions (lighting variation, occlusion, camera angles) is essential for demonstrating technical feasibility and clinical relevance.

This method also respects the sequence of the project. Before asking whether an off-the-shelf transfer learning solution works, I first need to establish whether a purpose-built pipeline can achieve acceptable accuracy on locally relevant medication and under realistic usage conditions. That is the kind of work controlled dataset generation and iterative architecture comparison do well.

## 2.5. Why Method 2 Does Not Win

Transfer learning with existing datasets would offer faster development and lower data collection burden, but publicly available pill datasets rarely include the specific brands and formulations used in Peru's national tuberculosis program. Moreover, pre-trained action recognition models are typically trained on general human actions (sports, cooking) rather than the specific motion pattern of medication ingestion. Without controlled data collection and fine-tuning on the target domain, the system risks poor generalization to the actual clinical context.

In other words, transfer learning could become a valuable component within Method 1, but relying on it as the primary strategy would compromise the study's ability to answer whether the system works for the specific tuberculosis treatment scenario in Peru.

## 2.6. Why Method 3 Does Not Win

Rule-based computer vision is appealing because it avoids the complexity of deep learning training and requires less computational resources. The problem is that handcrafted features struggle with the variability inherent in real-world medication intake: different pill colors and shapes, varying skin tones, diverse backgrounds, changing lighting conditions, and unpredictable head/camera movements. The ingestion detection task in particular requires understanding temporal sequences, which traditional optical flow and template matching handle poorly compared to deep learning approaches.

If I forced a rule-based design, the project would likely fail to achieve the accuracy and robustness thresholds required for any practical medication adherence application, making the technical validation meaningless.

## 2.7. Open Tension

The chosen method is strong for technical validation and architecture comparison, but weaker for immediate clinical deployment. The controlled dataset and lab testing provide rigorous evidence of algorithmic performance, yet they do not demonstrate whether the system improves actual treatment adherence in tuberculosis patients. If the project later evolves into a clinical implementation study, it may need to shift toward a mixed-methods design integrating technical metrics with patient adherence data. For now, though, the defensible choice is to build a reliable technical baseline first.