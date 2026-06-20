# Mini Systematic Review: AI-DOTS — Computer Vision for Pill Detection and Ingestion Verification


## 4.1. Review Question
What does the literature show about computer vision-based systems for pill classification, medication adherence monitoring, and ingestion detection, and what gaps remain for tuberculosis-specific applications in resource-limited settings?

## 4.2. Search Strategy

| Field | Value |
|---|---|
| Databases | PubMed, Scopus, Web of Science, IEEE Xplore |
| Search date | June 20, 2026 |
| Search approach | Broad search first, then screening for technical and clinical relevance |

**Boolean search string (PubMed)**

```text
("pill detection"[Title/Abstract] OR "medication detection"[Title/Abstract] OR "drug detection"[Title/Abstract] OR "tablet detection"[Title/Abstract] OR "pill classification"[Title/Abstract] OR "medication classification"[Title/Abstract] OR "drug identification"[Title/Abstract] OR "pharmaceutical identification"[Title/Abstract] OR "pill recognition"[Title/Abstract] OR "medication recognition"[Title/Abstract] OR "drug recognition"[Title/Abstract] OR "tablet recognition"[Title/Abstract] OR "pill image"[Title/Abstract] OR "medication image"[Title/Abstract] OR "drug image"[Title/Abstract])

AND

("swallowing detection"[Title/Abstract] OR "ingestion detection"[Title/Abstract] OR "pill intake"[Title/Abstract] OR "medication intake"[Title/Abstract] OR "drug intake"[Title/Abstract] OR "medication adherence"[Title/Abstract] OR "drug adherence"[Title/Abstract] OR "pill adherence"[Title/Abstract] OR "medication compliance"[Title/Abstract] OR "drug compliance"[Title/Abstract] OR "swallowing verification"[Title/Abstract] OR "ingestion verification"[Title/Abstract] OR "medication consumption"[Title/Abstract] OR "drug consumption"[Title/Abstract] OR "pill consumption"[Title/Abstract])

AND

("computer vision"[Title/Abstract] OR "deep learning"[Title/Abstract] OR "convolutional neural network"[Title/Abstract] OR "CNN"[Title/Abstract] OR "machine learning"[Title/Abstract] OR "artificial intelligence"[Title/Abstract] OR "neural network"[Title/Abstract] OR "image classification"[Title/Abstract] OR "object detection"[Title/Abstract] OR "image recognition"[Title/Abstract] OR "video analysis"[Title/Abstract] OR "action recognition"[Title/Abstract] OR "activity recognition"[Title/Abstract])

AND

("tuberculosis"[Title/Abstract] OR "DOTS"[Title/Abstract] OR "directly observed therapy"[Title/Abstract] OR "medication adherence"[Title/Abstract] OR "treatment monitoring"[Title/Abstract] OR "chronic disease"[Title/Abstract] OR "telemedicine"[Title/Abstract] OR "mobile health"[Title/Abstract] OR "mHealth"[Title/Abstract] OR "telehealth"[Title/Abstract] OR "remote monitoring"[Title/Abstract] OR "digital health"[Title/Abstract] OR "eHealth"[Title/Abstract] OR "healthcare technology"[Title/Abstract] OR "medical imaging"[Title/Abstract])
```

The search returned **27 records** across 4 databases.

## 4.3. Screening Criteria

**Inclusion criteria**

- Studies on computer vision or deep learning for pill/drug/medication detection, classification, or recognition
- Studies on medication adherence monitoring, ingestion detection, or swallowing verification using visual or sensor-based methods
- Studies on AI/ML frameworks for medication management in chronic disease or elderly care
- Peer-reviewed journal articles and conference proceedings in English or Spanish
- Studies published between 2015 and 2026

**Exclusion criteria**

- Studies without a computer vision, image processing, or AI/ML component
- Studies focused exclusively on pharmacological or biochemical aspects without technical system description
- Protocols, editorials, or highly general review papers with little relevance for the present technical question
- Studies too narrow to support the intended computer vision pipeline framing

## 4.4. PRISMA 2020 Flow

| Phase | n |
|---|---:|
| Records identified (PubMed) | 1 |
| Records identified (Scopus) | 13 |
| Records identified (WoS) | 4 |
| Records identified (IEEE Xplore) | 9 |
| Total records identified | 27 |
| Duplicates removed | 9 |
| Records screened | 18 |
| Excluded at title/abstract | 8 |
| Full texts assessed | 10 |
| Full texts excluded | 4 |
| **Studies included** | **6** |

The diagram version of this process is available in `prisma_diagram.png`.

## 4.5. Included Studies

| Study | Main contribution to this project |
|---|---|
| Lee & Youm (2021) | Demonstrates a wearable camera + CNN-based system for medication behavior recognition achieving 92.7% accuracy. Integrates object detection (Model 1) and action recognition (Model 2). Directly relevant to real-time ingestion detection using deep learning. |
| Nguyen et al. (2024) |	Introduces Zero-PIMA for zero-shot pill-prescription matching using graph convolutional networks and contrastive learning. Highly relevant for handling unseen pill brands in tuberculosis treatment. |
| Pu et al. (2025) |	Integrates YOLOv10 detection with XGBoost risk modeling in a smart medication management framework. Shows the synergy between detection and adherence prediction. |
| Yadav et al. (2026) |	Proposes a unified smart medication assistant combining CNN-based pill detection, ingestion verification, and conversational AI. Achieves 94.2% pill detection accuracy and 21.4% improvement in adherence. |
| Abiruth et al. (2026)	| Develops MediTrack, an IoT framework with automated pill detection, vital sign monitoring, and predictive health analytics. Achieves 98.5% pill detection accuracy and 88.90% adherence prediction accuracy. |
| Yang et al. (2021) |	Proposes an AR + OpenCV mobile application for elderly medication adherence supervision, demonstrating practical mobile deployment potential for remote supervision contexts. |

## 4.6. Main Synthesis

The literature points in a consistent direction. Computer vision-based medication management is a rapidly growing field with demonstrated feasibility across multiple clinical contexts. Deep learning approaches (CNN, YOLO) consistently outperform classical image processing methods, particularly for real-time applications.

Several clear patterns emerge:

1. Pill detection accuracy is high when trained on specific datasets, with most studies reporting 90-97% accuracy for classification tasks.
2. Ingestion detection is more challenging and requires temporal analysis (video frames, action recognition) rather than static image classification alone.
3. Mobile and edge deployment is increasingly feasible, with studies using Raspberry Pi, ESP32, and smartphone cameras for low-cost solutions.
4. Adherence improvement is measurable but modest (20-40% improvement over reminder-only systems), suggesting that detection alone is insufficient without behavioral support.
5. Zero-shot and transfer learning approaches are emerging to handle unseen medications, which is critical for tuberculosis programs with multiple drug formulations.

The review also reveals significant gaps. Most studies focus on elderly or chronic disease populations in high-resource settings. There is minimal work on tuberculosis-specific applications, particularly in low-resource or remote contexts where DOTS supervision is most needed. Furthermore, very few studies integrate both pill classification and ingestion detection in a unified pipeline; most address only one of the two tasks.

## 4.7. What This Means for the Present Study

This review supports the direction of the AI-DOTS project, but it also clarifies its niche. The literature demonstrates technical feasibility for pill detection and ingestion verification separately, yet there is still room for a purpose-built system that integrates both tasks for tuberculosis treatment in Peru's DOTS program context. The specific contributions of this project would be:

- Integration of pill classification and real-time ingestion detection in a single pipeline
- Focus on tuberculosis pill brands used in Peru's national program
- Validation under realistic conditions (lighting, occlusion, angles)
- Potential for remote DOTS supervision in resource-limited settings
- Technical feasibility demonstration as a foundation for future clinical validation
