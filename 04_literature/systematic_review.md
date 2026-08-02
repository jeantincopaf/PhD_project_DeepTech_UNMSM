# Systematic Literature Review: AI-DOTS — Computer Vision for Pill Detection and Ingestion Verification


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

**Boolean search string (Web of Science)**

```text
TS=("pill detection" OR "medication detection" OR "drug detection" OR "tablet detection" OR "pill classification" OR "medication classification" OR "drug identification" OR "pharmaceutical identification" OR "pill recognition" OR "medication recognition" OR "drug recognition" OR "tablet recognition" OR "pill image" OR "medication image" OR "drug image" OR "pharmaceutical image" OR "pill counting" OR "medication counting" OR "drug counting" OR "pharmaceutical counting")
AND
TS=("swallowing detection" OR "ingestion detection" OR "pill intake" OR "medication intake" OR "drug intake" OR "medication adherence" OR "drug adherence" OR "pill adherence" OR "medication compliance" OR "drug compliance" OR "treatment adherence" OR "treatment compliance" OR "swallowing verification" OR "ingestion verification" OR "medication consumption" OR "drug consumption" OR "pill consumption" OR "medication taking" OR "drug taking" OR "pill taking" OR "medication swallowing" OR "drug swallowing")
AND
TS=("computer vision" OR "deep learning" OR "convolutional neural network" OR "CNN" OR "machine learning" OR "artificial intelligence" OR "neural network" OR "image classification" OR "object detection" OR "image recognition" OR "video analysis" OR "action recognition" OR "activity recognition" OR "pattern recognition" OR "image processing" OR "video processing" OR "feature extraction" OR "transfer learning")
AND
TS=("tuberculosis" OR "DOTS" OR "directly observed therapy" OR "medication adherence" OR "treatment monitoring" OR "chronic disease" OR "telemedicine" OR "mobile health" OR "mHealth" OR "telehealth" OR "remote monitoring" OR "digital health" OR "eHealth" OR "healthcare technology" OR "medical imaging" OR "smartphone" OR "mobile application" OR "wearable" OR "health informatics")
```

**Boolean search string (Scopus)**

```text
TITLE-ABS-KEY(("pill detection" OR "medication detection" OR "drug detection" OR "tablet detection" OR "pill classification" OR "medication classification" OR "drug identification" OR "pharmaceutical identification" OR "pill recognition" OR "medication recognition" OR "drug recognition" OR "tablet recognition" OR "pill image" OR "medication image" OR "drug image" OR "pharmaceutical image" OR "pill counting" OR "medication counting" OR "drug counting"))
AND
TITLE-ABS-KEY(("swallowing detection" OR "ingestion detection" OR "pill intake" OR "medication intake" OR "drug intake" OR "medication adherence" OR "drug adherence" OR "pill adherence" OR "medication compliance" OR "drug compliance" OR "treatment adherence" OR "treatment compliance" OR "swallowing verification" OR "ingestion verification" OR "medication consumption" OR "drug consumption" OR "pill consumption" OR "medication taking" OR "drug taking" OR "pill taking"))
AND
TITLE-ABS-KEY(("computer vision" OR "deep learning" OR "convolutional neural network" OR "CNN" OR "machine learning" OR "artificial intelligence" OR "neural network" OR "image classification" OR "object detection" OR "image recognition" OR "video analysis" OR "action recognition" OR "activity recognition" OR "pattern recognition" OR "image processing" OR "video processing" OR "feature extraction"))
AND
TITLE-ABS-KEY(("tuberculosis" OR "DOTS" OR "directly observed therapy" OR "medication adherence" OR "treatment monitoring" OR "chronic disease" OR "telemedicine" OR "mobile health" OR "mHealth" OR "telehealth" OR "remote monitoring" OR "digital health" OR "eHealth" OR "healthcare technology" OR "medical imaging" OR "smartphone" OR "mobile application" OR "wearable"))
```

**Boolean search string (IEEEXplore)**

```text
(("pill detection" OR "medication detection" OR "drug detection" OR "tablet detection" OR "pill classification" OR "medication classification" OR "drug identification" OR "pharmaceutical identification" OR "pill recognition" OR "medication recognition" OR "drug recognition" OR "tablet recognition" OR "pill image" OR "medication image" OR "drug image" OR "pharmaceutical image" OR "pill counting" OR "medication counting" OR "drug counting" OR "pharmaceutical counting"))
AND
(("swallowing detection" OR "ingestion detection" OR "pill intake" OR "medication intake" OR "drug intake" OR "medication adherence" OR "drug adherence" OR "pill adherence" OR "medication compliance" OR "drug compliance" OR "treatment adherence" OR "treatment compliance" OR "swallowing verification" OR "ingestion verification" OR "medication consumption" OR "drug consumption" OR "pill consumption" OR "medication taking" OR "drug taking" OR "pill taking" OR "medication swallowing" OR "drug swallowing"))
AND
(("computer vision" OR "deep learning" OR "convolutional neural network" OR "CNN" OR "machine learning" OR "artificial intelligence" OR "neural network" OR "image classification" OR "object detection" OR "image recognition" OR "video analysis" OR "action recognition" OR "activity recognition" OR "pattern recognition" OR "image processing" OR "video processing" OR "feature extraction" OR "transfer learning" OR "YOLO" OR "ResNet" OR "EfficientNet"))
AND
(("tuberculosis" OR "DOTS" OR "directly observed therapy" OR "medication adherence" OR "treatment monitoring" OR "chronic disease" OR "telemedicine" OR "mobile health" OR "mHealth" OR "telehealth" OR "remote monitoring" OR "digital health" OR "eHealth" OR "healthcare technology" OR "medical imaging" OR "smartphone" OR "mobile application" OR "wearable" OR "health informatics" OR "biomedical engineering"))
```

The search returned **27 records** across 4 databases.

## 4.3. Screening Criteria

**Inclusion criteria**

- Studies on computer vision or deep learning for pill/drug/medication detection, classification, or recognition
- Studies on medication adherence monitoring, ingestion detection, or swallowing verification using visual or sensor-based methods
- Studies on AI/ML frameworks for medication management in chronic disease or elderly care
- Full peer-reviewed journal articles and peer-reviewed conference papers
- Publications written in English
- Studies published from January 1, 2021, through the search date in 2026
- Studies involving human participants, human medication-use scenarios, or technical validation without animal experimentation

**Exclusion criteria**

- Studies without a computer vision, image processing, or AI/ML component
- Studies focused exclusively on pharmacological or biochemical aspects without technical system description
- Publications before 2021 or after the search date
- Publications in languages other than English
- Animal studies
- Books, standalone book chapters, theses, dissertations, preprints, protocols, editorials, and other non-peer-reviewed material
- Review papers without primary technical validation relevant to the research question
- Studies whose full text did not provide sufficient technical detail to evaluate the detection, recognition, monitoring, or ingestion-verification method

Conference papers published within edited proceedings were treated as conference papers rather than as standalone book chapters. This distinction applies, for example, to the peer-reviewed HCII paper by Yang et al. (2021).

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

**Reasons for full-text exclusion (n = 4)**

| Reason | n |
|---|---:|
| Traditional methods without ingestion detection | 2 |
| Spatial detection only, without ingestion analysis | 2 |
| **Total** | **4** |

Google Scholar was not used as a bibliographic database and is not included in the identification count.

## 4.5. Included Studies

| Study | Main contribution to this project |
|---|---|
| Lee & Youm (2021) | Demonstrates a wearable camera and CNN-based system for medication behavior recognition, achieving 92.7% accuracy. It combines object detection and action recognition and is directly relevant to video-based medication-taking analysis. |
| Nguyen et al. (2024) | Introduces Zero-PIMA for zero-shot pill-prescription matching using graph convolutional networks and contrastive learning. It is relevant to recognition when the target pill was not represented during training, although it does not verify swallowing. |
| Pu et al. (2025) | Integrates YOLOv10 pill detection with XGBoost risk modeling in a smart medication-management framework, linking visual detection with risk-oriented decision support. |
| Holtkötter et al. (2022) | Develops and validates an image-processing tool that detects taken and remaining pills in blister packs. Detection varied by blister type, showing both the feasibility and limitations of controlled visual pill-intake monitoring. |
| Abiruth et al. (2026) | Develops MediTrack, an IoT smart-pillbox framework that combines infrared pill detection, vital-sign monitoring, and adherence prediction. It detects pill removal rather than visually confirming swallowing. |
| Yang et al. (2021) | Presents a peer-reviewed HCII conference prototype using AR and OpenCV for mobile medication supervision. Pill contours are detected from user photographs, but the prototype did not establish clinical ingestion verification. |

## 4.6. Main Synthesis

The six verified studies show that visual and sensor-based medication monitoring is technically feasible, but they address different outcomes. Some identify or localize pills, some infer removal from a blister or pillbox, and only the wearable-camera approach analyzes medication-taking behavior. These outcomes should not be treated as equivalent to confirmed swallowing.

Several clear patterns emerge:

1. Performance depends strongly on the task, dataset, packaging, lighting, and evaluation design; accuracy values from pill classification, pill removal, behavior recognition, and adherence prediction are not directly comparable.
2. Static images can support pill recognition or detection of remaining pills, but stronger evidence of ingestion requires temporal evidence, such as video-based action recognition.
3. Wearable cameras, smartphones, and embedded pillboxes demonstrate practical deployment routes, but the included studies are mainly prototypes or controlled validations.
4. Zero-shot matching may reduce dependence on retraining for every pill presentation, but it does not by itself solve ingestion verification.
5. No included study validates an integrated computer-vision pipeline for tuberculosis treatment under Peru's DOTS conditions.

The principal gap is therefore not simply pill detection accuracy. It is the lack of an end-to-end, externally validated system that links pill presence or identity to a reliable sequence of medication-taking actions while protecting privacy and operating under realistic conditions. The reviewed evidence supports a staged research strategy: first validate pill detection as a proof of concept, then study temporal ingestion verification and, only after appropriate ethical approval, evaluate the complete system in the intended population.
## 4.7. What This Means for the Present Study

This review supports the direction of the AI-DOTS project, but it also clarifies its niche. The literature demonstrates technical feasibility for pill detection and ingestion verification separately, yet there is still room for a purpose-built system that integrates both tasks for tuberculosis treatment in Peru's DOTS program context. The specific contributions of this project would be:

- Integration of pill classification and real-time ingestion detection in a single pipeline
- Focus on tuberculosis pill brands used in Peru's national program
- Validation under realistic conditions (lighting, occlusion, angles)
- Potential for remote DOTS supervision in resource-limited settings
- Technical feasibility demonstration as a foundation for future clinical validation

The MEDISEG/YOLO proof of concept reported elsewhere in this repository addresses only the first of these stages: pill detection. It does not constitute evidence of ingestion or medication adherence and does not alter the original research question or protocol.

## 4.8. Verified References

1. Lee, H., & Youm, S. (2021). Development of a wearable camera and AI algorithm for medication behavior recognition. *Sensors, 21*(11), 3594. https://doi.org/10.3390/s21113594
2. Nguyen, T. T., Nguyen, P. L., Kawanishi, Y., Komamizu, T., & Ide, I. (2024). Zero-shot pill-prescription matching with graph convolutional network and contrastive learning. *IEEE Access, 12*, 55889-55904. https://doi.org/10.1109/ACCESS.2024.3390153
3. Pu, X., Shi, B., Pu, R., & Zhao, G. (2025). Developing a smart medication management framework: Integration of YOLOv10 detection and XGBoost risk modeling. In *2025 5th International Symposium on Computer Technology and Information Science (ISCTIS 2025)* (pp. 829-833). IEEE.
4. Holtkötter, J., Amaral, R., Almeida, R., Jácome, C., Cardoso, R., Pereira, A., Pereira, M., Chon, K. H., & Fonseca, J. A. (2022). Development and validation of a digital image processing-based pill detection tool for an oral medication self-monitoring system. *Sensors, 22*(8), 2958. https://doi.org/10.3390/s22082958
5. Abiruth, S., Ghanasree, S., Sriranjana, C., Thrishala, S. N., Sabapathy, S., & Jayakody, D. N. K. (2026). MediTrack: An intelligent IoT framework for medication adherence and real-time health monitoring. In *2026 6th International Conference on Advanced Research in Computing (ICARC 2026)*. IEEE. https://doi.org/10.1109/ICARC68737.2026.11453866
6. Yang, S., Pang, X., & He, X. (2021). A novel mobile application for medication adherence supervision based on AR and OpenCV designed for elderly patients. In Q. Gao & J. Zhou (Eds.), *Human Aspects of IT for the Aged Population: Supporting Everyday Life Activities* (LNCS 12787, pp. 335-347). Springer. https://doi.org/10.1007/978-3-030-78111-8_23

### Source-verification note

The previous table contained a record attributed to “Yadav et al. (2026)” with the claims of 94.2% pill-detection accuracy and a 21.4% adherence improvement. No matching peer-reviewed publication, title, venue, or DOI could be verified by author, description, or reported metrics. To avoid retaining an unsupported citation while preserving the PRISMA total of six included studies, that entry was replaced during the source audit by the verified and eligible study of Holtkötter et al. (2022).