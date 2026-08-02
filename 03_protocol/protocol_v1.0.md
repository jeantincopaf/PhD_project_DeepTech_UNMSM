# Research Protocol v1.0

## AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis

**Principal researcher:** Jean Pierre Tincopa Flores
**Institution:** Universidad Nacional Mayor de San Marcos (UNMSM)
**Program:** PhD in Deep Technologies focused on Artificial Intelligence and Emerging Technologies
**Protocol version:** 1.0
**Date:** 1 August 2026
**Status:** Complete course draft; not approved for human-participant recruitment

## 1. Protocol summary

AI-DOTS is a staged quantitative study of whether computer vision can support remote verification of medication use in tuberculosis treatment. The complete research concept contains two technical components: (1) detection and classification of tuberculosis pills and (2) validation of the ingestion action in video. The present protocol preserves both components. It does not redefine the project as pill detection alone.

The MEDISEG experiment already completed in this repository is the first public-data proof of concept. It establishes that a reproducible YOLO-family pipeline can detect three pill classes in still images, but it does not validate tuberculosis pill brands, swallowing, medication adherence, clinical effectiveness, or deployment in the DOTS program. Later phases will require a locally relevant tuberculosis-pill image dataset and a controlled ingestion-video dataset collected from consenting adults who do not have active tuberculosis and who already take oral medication for a non-contagious condition.

A short closed-ended acceptability and usability questionnaire will be administered after the future recording session. This questionnaire is secondary to the technical evaluation and does not change the primary quantitative empirical paradigm. No sample-size calculation or target number of participants is included in version 1.0. Recruitment cannot begin until the sample strategy, ethics approval, consent materials, and remaining operational details have been approved.

## 2. Background and problem statement

Tuberculosis remains a major global and Peruvian public-health concern. The World Health Organization estimated that 10.7 million people developed tuberculosis worldwide in 2024. Peru's Ministry of Health reported 33,049 tuberculosis cases registered in Peru in 2024. Treatment requires sustained medication use, and directly observed treatment creates logistical demands for patients, health personnel, and services, particularly where distance and resources limit in-person supervision.

Computer vision may offer a technical component for remote medication verification. However, detecting a pill in an image, identifying its type, observing a hand-to-mouth action, and establishing that ingestion occurred are different tasks. A scientifically defensible system must keep these tasks separate, measure each with appropriate outcomes, document failure modes, and avoid equating an algorithmic prediction with confirmed adherence or treatment success.

The research gap identified in the accompanying systematic review is the limited integration of pill classification and temporal ingestion validation in one pipeline, especially for tuberculosis medication used in Peru and under realistic variations in lighting, occlusion, camera angle, and capture device. Existing work supports technical feasibility but does not justify assuming clinical effectiveness in the intended population.

## 3. Rationale and expected contribution

The study is justified as a technical feasibility and validation project. Its intended contribution is a reproducible computer-vision pipeline that:

1. detects and classifies locally relevant tuberculosis pills in controlled still images;
2. recognizes a medication-ingestion event from a restricted video field of view;
3. quantifies robustness under pre-specified capture conditions;
4. documents uncertainty, false confirmations, false rejections, and non-evaluable recordings;
5. evaluates whether the recording procedure is acceptable and usable to adult pilot participants; and
6. produces an auditable basis for a later, separately approved clinical-validation study.

The study will not claim to improve adherence, replace health personnel, diagnose tuberculosis, verify pharmacological absorption, or establish clinical benefit. Those questions require later designs, populations, outcomes, and approvals.

## 4. Research paradigm

The primary paradigm is quantitative empirical (positivist). The principal questions are answered through observable and reproducible measures of detection, classification, temporal event recognition, computational performance, and robustness. Models will be evaluated on held-out data using pre-defined metrics rather than subjective interpretation.

The questionnaire is also quantitative. It captures structured ratings of usability, privacy acceptability, burden, and perceived trust using closed-ended items. It is a secondary feasibility measure and does not convert the study into an interpretivist or mixed-methods design. No qualitative interview or AI-generated personal interpretation is planned in this protocol.

## 5. Research questions

### 5.1 Primary research question

To what extent can a computer vision system accurately classify tuberculosis pill brands and detect real-time pill ingestion, and which neural network architectures and robustness conditions are most strongly associated with reliable medication verification performance?

### 5.2 Specific research questions

1. How accurately can the system detect and classify the selected tuberculosis pill brands in held-out still images?
2. How accurately can the system distinguish a completed ingestion event from non-ingestion or incomplete-event sequences in held-out video?
3. How do lighting, occlusion, camera angle, capture device, and pill presentation affect performance?
4. Which candidate architecture or pipeline provides the best balance of predictive performance, computational efficiency, and reproducibility under the controlled design?
5. How acceptable and usable is the restricted recording procedure to adults participating in the future pilot?

## 6. Objectives

### 6.1 General objective

To develop and technically validate a reproducible computer-vision pipeline for tuberculosis pill classification and video-based ingestion-event verification under controlled conditions.

### 6.2 Specific objectives

1. Build and document a labeled image dataset of selected tuberculosis pill brands relevant to the Peruvian context.
2. Build a pseudonymous video dataset of ordinarily scheduled oral-medication events from eligible consenting adults without active tuberculosis.
3. Compare candidate deep-learning approaches for pill classification/detection and temporal ingestion-event recognition.
4. Measure predictive performance and computational efficiency on held-out data.
5. Quantify performance changes across lighting, occlusion, camera angle, device, and other pre-specified technical conditions.
6. Measure participant-rated acceptability and usability of the recording procedure through a short quantitative questionnaire.
7. Preserve data provenance, splits, code, environments, configurations, logs, and negative results sufficient for an independent audit.

## 7. Working hypotheses

The hypotheses are directional technical expectations rather than claims of clinical effectiveness:

- **H1:** A purpose-built deep-learning pipeline will outperform a pre-specified simple baseline for tuberculosis pill detection and classification on the same held-out data.
- **H2:** A temporal model using ordered video information will outperform a static-frame baseline for ingestion-event verification on the same participant-independent test set.
- **H3:** Performance will decrease under adverse lighting, greater occlusion, or non-frontal camera angles compared with the reference capture condition.
- **H4:** At least one candidate pipeline will meet performance and latency thresholds that are defined and frozen before access to the final test set.

No directional hypothesis is set for the acceptability questionnaire in version 1.0. Questionnaire results will be reported descriptively unless a separate analysis plan is approved before data collection.

## 8. Study design

This is a staged controlled technical-validation study with a secondary cross-sectional questionnaire component.

| Stage | Data | Purpose | Current status |
|---|---|---|---|
| 0 | Public MEDISEG v2 three-pill subset | Demonstrate an executable, reproducible pill-detection pipeline | Completed proof of concept |
| 1 | Controlled images of selected tuberculosis pill brands | Train and evaluate locally relevant pill detection/classification | Planned |
| 2 | Restricted-view ingestion videos from eligible consenting adults | Train and evaluate temporal ingestion-event verification | Planned; ethics approval required |
| 3 | Closed-ended post-session questionnaire | Describe acceptability, usability, burden, and privacy perceptions | Planned; secondary outcome |
| 4 | Integrated pipeline evaluation | Evaluate sequential pill and ingestion modules without making clinical claims | Planned |

The design is not a clinical trial. No treatment will be assigned or changed, and no participant will receive an additional medication dose for research purposes.

## 9. Current proof of concept and interpretation boundary

The completed MEDISEG experiment used a public, non-participant image dataset with three pill classes. A YOLO26n model was trained with seed 42 on 1,633 training images, with 350 validation and 350 held-out test images. Archived test results were precision 0.9288, recall 0.8980, mAP@0.50 of 0.9740, and mAP@0.50:0.95 of 0.9174.

These results show only that the documented pipeline performed well on the defined MEDISEG subset and split. They are historical proof-of-concept results, not prospective endpoints for the human-participant phase. They do not establish performance on Peruvian tuberculosis pills, video ingestion, different people, home environments, adherence behavior, or health outcomes.

## 10. Study setting and data sources

### 10.1 Public-data phase

MEDISEG v2 is used only for the completed proof of concept. Its DOI, archive checksum, deterministic split manifest, class mapping, software environment, training configuration, metrics, figures, and artifact hashes are preserved under `05_pipeline/`.

### 10.2 Tuberculosis-pill image phase

Reference pills will be sourced only through a lawful and documented pathway. Before acquisition, the study will record formulation, manufacturer or program identifier where applicable, batch-related metadata when legally and scientifically appropriate, image-acquisition protocol, licensing or reuse conditions, and storage requirements. No medicine will be removed from clinical supply or given to a participant for research without authorization.

Images will be collected under pre-specified combinations of background, distance, angle, illumination, pill orientation, grouping, and partial occlusion. An annotation guide will define object boundaries, class labels, ambiguous cases, quality exclusions, and adjudication. Acquisition-session identifiers will be retained so related images can be kept within one data partition.

### 10.3 Ingestion-video phase

Eligible participants will be recorded only while taking an ordinarily scheduled oral medication according to their existing prescription. The research team will not select, prescribe, add, delay, or reschedule the dose. The ingestion-action model is intended to learn the temporal action, not to infer the participant's diagnosis or medication indication.

Video will be limited to hands, the pill and relevant container, and the lower facial area necessary to observe the event. Full-face capture and audio are prohibited. Minimal technical metadata may include pseudonymous participant code, session code, lighting condition, camera angle, occlusion category, device category, and recording-quality status.

## 11. Participants

### 11.1 Target pilot population

Adults without active tuberculosis who already take oral medication daily for a non-contagious condition and can provide autonomous informed consent.

### 11.2 Inclusion criteria

Participants must:

- be at least 18 years old;
- have capacity to provide informed consent;
- have no active or suspected tuberculosis;
- have no contagious condition relevant to the recording setting;
- already take an oral medication daily as part of usual care;
- be willing to follow the recording procedure without changing the prescribed regimen; and
- be able to stop participation immediately if uncomfortable.

### 11.3 Exclusion criteria

Potential participants will be excluded if they:

- are younger than 18;
- have active or suspected tuberculosis;
- cannot provide autonomous informed consent;
- report dysphagia, current swallowing difficulty, or a condition making observation unsafe;
- would need an extra, substituted, delayed, or rescheduled dose solely for the study;
- are under direct academic, employment, clinical, or financial authority of the researcher in a way that could compromise voluntary participation; or
- cannot be recorded within the approved privacy boundaries.

### 11.4 Sampling strategy and size

Recruitment will use criterion-based purposive sampling after ethics approval. Recruitment materials and channels must avoid coercion, therapeutic misconception, and over-recruitment of economically or institutionally dependent individuals.

**No target sample size or sample-size calculation is specified in protocol v1.0.** This is a deliberate unresolved item in the current course version. The number of participants, number of sessions per participant, and statistical justification must be established and approved before CEI submission, recruitment, or collection. No feasibility claim in this protocol should be interpreted as authorization to recruit without that decision.

### 11.5 Compensation

Compensation or reimbursement is not specified in version 1.0. Any later proposal must compensate reasonable time or expenses without becoming an undue inducement and must appear in the approved consent materials.

## 12. Study procedures

### 12.1 Pre-collection preparation

Before any participant activity, the researcher will:

1. obtain a favorable opinion from the competent UNMSM Research Ethics Committee (CEI);
2. finalize the sampling strategy, operational sample target, session duration, repetitions, and compensation decision;
3. finalize participant information, consent, withdrawal, and privacy materials in accessible language;
4. test encrypted storage, backup restoration, access logging, and secure deletion;
5. freeze the recording protocol, annotation manual, questionnaire, and analysis plan;
6. conduct a dry run without ingesting medication and without collecting participant data; and
7. register protocol deviations and amendments through version control.

### 12.2 Enrollment and consent

Eligibility screening will collect the minimum information needed. Detailed diagnosis, prescription, national identifier, address, and other unnecessary health information will not enter the machine-learning dataset. Written or approved digital informed consent will be obtained before recording.

The participant will be told that this is research, not treatment or adherence supervision; participation is voluntary; the model can make errors; there is no guaranteed personal benefit; withdrawal carries no penalty; and raw video will not be made public.

### 12.3 Recording session

For each approved session:

1. assign a random participant and session code;
2. verify consent and that the medication event is ordinarily scheduled;
3. confirm full-face exclusion, audio-off status, and absence of identifiers in the frame;
4. record only the approved field of view and technical conditions;
5. stop immediately at the participant's request or if discomfort, swallowing difficulty, medication uncertainty, or a privacy violation occurs;
6. delete and document invalid takes that capture prohibited information;
7. transfer valid data through an encrypted pathway; and
8. administer the short questionnaire after the recording has ended.

The researcher will not instruct a participant to repeat ingestion with another pill. Repeated observations, if later approved, must correspond to separate ordinarily scheduled medication events.

### 12.4 Withdrawal

Participants may stop the session without explanation. They may request deletion of identifiable or pseudonymous raw recordings until the analysis-freeze date specified in the approved consent form. The limits of deletion after irreversible aggregation will be explained before consent.

## 13. Instruments

### 13.1 Image-acquisition and annotation protocol

The instrument will specify camera settings, distance, background, lighting, angles, occlusion categories, pill presentation, image-quality checks, label definitions, annotator training, disagreement resolution, and exclusion rules.

### 13.2 Video-recording and event-annotation protocol

The video instrument will define the permitted frame, camera position, audio-off verification, event start and end, positive ingestion-event criteria, incomplete or ambiguous events, non-ingestion controls, quality exclusions, and annotation review. The definition of a positive video label must be operational and must not claim biological proof of swallowing or absorption beyond observable evidence.

### 13.3 Acceptability and usability questionnaire

The self-developed questionnaire in Appendix A contains ten closed-ended statements rated from 1 (strongly disagree) to 5 (strongly agree). It addresses procedural clarity, physical burden, privacy acceptability, perceived usefulness, trust, and the need for human review. It will be completed after the session and will not request a diagnosis, medication name, or open-ended health narrative.

Because this is a new instrument, item-level results are primary for the questionnaire component. A total score will not be treated as validated unless its dimensionality and reliability are evaluated in an appropriately justified future sample. Any translation, cognitive testing, or pilot modification must be documented before the final questionnaire is frozen.

## 14. Variables and operational definitions

| Role | Variable | Operational measurement | Scale |
|---|---|---|---|
| Primary outcome | Pill detection performance | Precision, recall, F1, mAP@0.50, mAP@0.50:0.95 on the held-out pill-image test set | Ratio |
| Primary outcome | Pill classification performance | Per-class and macro-averaged precision, recall, F1; confusion matrix | Ratio |
| Primary outcome | Ingestion-event verification | Event-level sensitivity/recall, specificity, precision, F1, false-positive rate, false-negative rate, and AUROC/AUPRC when probabilistic outputs are valid | Ratio |
| Secondary outcome | Temporal localization | Event onset/offset agreement or temporal IoU under a frozen definition | Ratio |
| Secondary outcome | Computational performance | End-to-end latency, frames per second, memory use, and model size on named hardware | Ratio |
| Secondary outcome | Recording acceptability/usability | Distribution of each 1-5 questionnaire item; domain summaries only if justified | Ordinal |
| Explanatory | Architecture | Candidate image and temporal model/pipeline | Nominal |
| Explanatory | Lighting | Pre-specified reference and adverse categories measured during acquisition | Nominal/ordinal |
| Explanatory | Occlusion | Pre-specified visible-area or obstruction categories | Ordinal |
| Explanatory | Camera angle | Frontal, lateral, overhead, or other frozen categories | Nominal |
| Explanatory | Device category | Approved camera or smartphone category | Nominal |
| Control | Data partition | Train, validation, or test assignment frozen before modeling | Nominal |
| Control | Random seed and configuration | Recorded seed, code commit, environment, and model configuration | Nominal |

For ingestion verification, a false positive is a model confirmation when the reference label does not indicate a completed observable event. A false negative is a model rejection of a reference-labeled completed observable event. Neither label proves medication absorption or adherence outside the recorded event.

## 15. Dataset partitioning and leakage control

All partitions will be frozen before final model comparison.

- Related still images from the same acquisition session or physical pill instance will remain in one partition where identifiers permit.
- All videos from one participant will remain in one partition; no participant may appear in both training and final test data.
- Frames extracted from one video must never cross partitions.
- Augmentation will be applied only after partitioning and only to training data.
- Exact and near-duplicate checks will be performed before analysis.
- The final test set will remain inaccessible for architecture selection, threshold tuning, or questionnaire development.
- Any cross-validation will be group-aware and participant- or session-independent. It will be used only if the final approved data structure supports it.

Split manifests, exclusions, corrections, and hashes will be retained as reproducibility artifacts.

## 16. Model-development strategy

Candidate approaches may include YOLO-family detectors for pill localization, ResNet or EfficientNet variants for classification, and temporal CNN, recurrent, transformer, or action-recognition architectures for video. Transfer learning may be used within the selected controlled-data method; it does not replace collection and validation on the target domain.

All candidate comparisons must use the same frozen partitions, evaluation code, metric definitions, and hardware reporting rules. Hyperparameters will be selected only with training and validation data. The final architecture and decision threshold will be locked before final test evaluation.

An interpretable simple baseline will be defined for each task. The image baseline may use a conventional pretrained classifier or detector under minimal tuning. The video baseline may aggregate independent frame predictions without temporal modeling. Baselines and thresholds must be documented before comparative testing.

## 17. Analysis plan

### 17.1 Descriptive analysis

Dataset flow will report acquired, excluded, annotated, and partitioned items; class distributions; participant/session counts once approved; missingness; non-evaluable recordings; and technical-condition distributions. Exclusions will be reported with reasons.

### 17.2 Pill detection and classification

The primary report will include held-out precision, recall, F1, mAP@0.50, mAP@0.50:0.95, per-class values, confusion matrices, and confidence intervals calculated by a documented resampling procedure appropriate to the unit of analysis. Results will identify the model checkpoint, threshold, averaging rule, and test-set version.

### 17.3 Ingestion-event verification

Evaluation will occur at the event or video level, not by treating correlated frames as independent samples. Sensitivity, specificity, precision, F1, false-positive rate, false-negative rate, and probabilistic discrimination metrics will be reported where applicable. Confidence intervals will resample at the participant level when participant data are involved.

The false-positive rate will receive explicit safety attention because a false confirmation may conceal a missed medication event. False negatives and non-evaluable recordings will also be reported rather than absorbed into aggregate accuracy.

### 17.4 Architecture comparison

Candidate models will be compared on identical held-out units. Point estimates, uncertainty, and paired differences will be reported. A paired bootstrap, permutation procedure, or other test appropriate to the final data structure may be specified before test access. Multiple comparisons will be controlled if several architectures or conditions are tested. Statistical significance will not substitute for effect size, uncertainty, or practical relevance.

### 17.5 Robustness analysis

Performance will be stratified by lighting, occlusion, camera angle, device category, pill class, and recording quality where adequately represented. The analysis will report absolute performance and the difference from the reference condition. Sparse cells will be disclosed and will not support strong subgroup conclusions.

### 17.6 Questionnaire analysis

Each item will be summarized using response counts, proportions, median, and interquartile range. Negatively framed concern items will not be reverse-scored into a single total unless a scoring plan is justified before analysis. Missing responses and “not applicable” responses, if allowed in the final instrument, will be reported separately.

No inferential acceptability claim or population generalization is planned in version 1.0. Questionnaire results describe only the participants who complete the future pilot.

### 17.7 Missing data and deviations

No outcome will be silently imputed. Missing labels, corrupt files, incomplete events, withdrawals, and protocol deviations will be tabulated. Any imputation or sensitivity analysis proposed later must be justified and frozen before final analysis. Analyses added after seeing the results will be labeled exploratory.

## 18. Performance thresholds and decision rules

Numerical success thresholds are not set in this version because the final target datasets and approved operating context are not yet fixed. Before final test access, the protocol will specify:

- minimum acceptable recall and precision for pill detection/classification;
- maximum acceptable false-positive rate for ingestion confirmation;
- treatment of non-evaluable recordings;
- latency target on named hardware;
- robustness degradation limits; and
- the rule for selecting or rejecting a candidate model.

Thresholds will be justified by the intended research use and error consequences, not selected after observing test results.

## 19. Ethics and participant protection

### 19.1 Approval status

Ethics status is **PENDING**. Planning and public MEDISEG work may continue, but no participant recruitment or recording may begin without a favorable CEI opinion and approved consent materials. The study will follow the applicable UNMSM CEI regulation, the Belmont principles, CONCYTEC scientific-integrity requirements, Peru's Law No. 29733, and the current regulation approved by Supreme Decree No. 016-2024-JUS.

### 19.2 Respect for persons

Participation will be voluntary and based on accessible informed consent. Refusal or withdrawal will have no effect on care, employment, education, or benefits. The study will avoid recruitment relationships that could create pressure.

### 19.3 Beneficence and non-maleficence

Only an ordinarily scheduled medication event will be observed. The study will not provide treatment advice. Recording will stop for discomfort, swallowing difficulty, uncertainty about the dose, privacy failure, or participant request. The system will remain research-only and will not autonomously determine adherence or notify third parties.

### 19.4 Justice

Selection will follow scientific eligibility rather than convenience, vulnerability, or ability to bear research burdens. Performance under technical conditions will be reported so that error burdens are not hidden by a single aggregate metric. Demographic data will not be collected without separate scientific justification, consent review, and CEI approval.

### 19.5 Privacy

The full face, audio, names, national identifiers, detailed diagnoses, prescriptions, addresses, and precise locations will not enter the ML dataset. Hands and lower-face video will still be treated as personal and potentially sensitive data. Raw video will not be published or committed to GitHub or a public DVC remote.

### 19.6 Human oversight and prohibited use

Model outputs will not trigger treatment changes, sanctions, surveillance, employment or insurance decisions, identity recognition, diagnosis, or prescription control. Any later clinical use requires separate validation, governance, regulation, human review, and a redress pathway.

## 20. Data management

Participant codes will be random and unrelated to identity. Consent and the code-to-identity key will be encrypted and stored separately from research data. Raw and pseudonymous participant data will be stored in encrypted controlled storage with a physically separate encrypted backup. Access will be limited to the researcher and a formally authorized adviser under least-privilege controls and access logging.

Current planned retention is one year after validation concludes for raw participant video and identifiable extracted frames, and five years for consent/linkage records, pseudonymous derived data, access and incident logs, and core study documentation, subject to CEI or legal requirements. Secure deletion must cover primary storage, backups, working copies, temporary exports, and retired devices.

Public sharing will be limited to code, non-sensitive documentation, aggregate metrics, and artifacts whose license and privacy status permit release. Requests for controlled participant-derived data require a scientific purpose, consent compatibility, CEI-compatible approval, a data-use agreement, and security review.

## 21. Reproducibility and quality assurance

The study will preserve:

- source and derived data provenance;
- dataset versions, retrieval dates, licenses, and checksums;
- annotation guides and adjudication records;
- deterministic or recorded split procedures and manifests;
- code commit identifiers and tagged releases;
- pinned dependencies, container configuration, hardware, and random seeds;
- training configuration, checkpoints, logs, and model-selection rules;
- machine-readable metrics and figure-generation code;
- failed runs, negative findings, exclusions, and deviations when scientifically relevant; and
- a change log linking protocol amendments to analysis changes.

A person with authorized data access should be able to reconstruct each reported result from the retained inputs, code, configuration, and instructions. Reproducibility claims will distinguish the public MEDISEG phase from restricted participant-data phases.

## 22. Risks and mitigation

| Risk | Planned mitigation |
|---|---|
| Accidental full-face or environmental capture | Restricted framing, audio disabled, pre-recording check, immediate invalid-take deletion |
| Re-identification from hands or lower face | Pseudonymous codes, separate linkage, encryption, restricted access, no raw-video publication |
| Disclosure of medication or health information | Collect only eligibility confirmation; exclude medication name and diagnosis from the ML dataset unless separately approved |
| Discomfort, fatigue, or embarrassment | Short approved session, immediate stop, no penalty, no unnecessary repetitions |
| Swallowing difficulty or medication error | Observe only the usual prescribed dose; exclude reported dysphagia; no treatment instruction |
| False ingestion confirmation | Research-only output, human review, explicit false-positive reporting, no autonomous clinical action |
| False rejection of genuine ingestion | Human review, contest/correction pathway, no punitive response |
| Dataset leakage or inflated performance | Participant/session-grouped splits, pre-split augmentation, duplicate checks, frozen final test set |
| Distribution shift | Condition-stratified testing and revalidation before any new population, device, or setting |
| Coercive or surveillance reuse | Purpose limitation, access controls, prohibited-use statement, new governance review for any repurposing |

## 23. Limitations

1. Adults without active tuberculosis are technical proxies and do not represent the clinical, behavioral, or social conditions of people receiving tuberculosis treatment.
2. Controlled recordings may not reproduce home environments, unstable connectivity, cultural practices, or long-term adherence behavior.
3. Observable ingestion behavior does not prove swallowing, absorption, correct medication identity, correct dose, or treatment adherence over time.
4. A self-developed questionnaire does not have established validity and will initially support item-level descriptive reporting only.
5. The absence of a sample-size decision in version 1.0 prevents recruitment and limits the precision claims that can currently be planned.
6. Performance may vary by pill formulation, packaging, device, lighting, skin appearance, hand movement, camera position, and unseen behaviors.
7. The MEDISEG proof of concept contains only three non-tuberculosis pill classes and cannot establish target-domain performance.

## 24. Timeline

The provisional 36-month sequence is milestone-based rather than authorization to collect data:

| Period | Planned activity |
|---|---|
| Months 1-6 | Finalize literature, target-pill scope, acquisition and annotation protocols, legal sourcing, preregistration plan, and CEI materials |
| Months 7-12 | Build and quality-audit the controlled tuberculosis-pill image dataset; establish baselines |
| Months 13-18 | Train and compare pill detection/classification architectures; complete robustness tests |
| Months 19-24 | After CEI approval, conduct the controlled ingestion-video pilot and administer the questionnaire |
| Months 25-30 | Train and evaluate temporal ingestion models; integrate modules; perform leakage and reproducibility audits |
| Months 31-36 | Final analysis, limitations assessment, thesis integration, manuscript preparation, and planning for separately approved clinical validation |

Dates will be amended if approvals, sourcing, recruitment, or technical validation require more time.

## 25. Dissemination

Results will be reported whether favorable, null, or negative. Publications and presentations will distinguish completed results from planned work and technical validation from clinical effectiveness. Participant-derived raw video will not be displayed publicly. Representative images or clips may be used only if they are non-identifying, consent explicitly permits that use, and the CEI approves the dissemination plan.

Authorship, acknowledgements, conflicts of interest, funding, and AI assistance will be disclosed according to institutional and venue requirements. Codex assistance is governed by `12_integrity/ai_use_policy.md`; no prompt text is included in this protocol.

## 26. Governance, amendments, and stopping rules

The researcher is responsible for protocol implementation, data stewardship, deviation records, and reporting. An authorized adviser may provide scientific oversight. The CEI retains oversight of participant protections and relevant amendments.

Data collection will pause for an uncontrolled privacy breach, unexpected safety concern, medication error, repeated capture outside the approved frame, loss of valid consent, serious protocol deviation, or inability to secure the data. Material changes to population, data, recording field, questionnaire, model purpose, sharing, or analysis require documented review and, where applicable, CEI approval before implementation.

## 27. Readiness and unresolved items

| Item | Status in v1.0 | Required before participant recruitment |
|---|---|---|
| Research question, paradigm, and staged scope | Defined | Maintain scope in amendments |
| MEDISEG proof of concept | Completed | Do not generalize beyond its dataset |
| Inclusion and exclusion criteria | Defined | CEI review |
| Sample size and statistical justification | Not specified by instruction | Define and obtain approval |
| Session duration and repetitions | Not specified | Define and dry-run |
| Compensation/reimbursement | Not specified | Decide and disclose |
| Consent and participant information | Draft concepts only | Final documents and CEI approval |
| Storage implementation and restore test | Partially specified in DMP | Implement and test |
| Questionnaire | Draft in Appendix A | Cognitive review, language check, CEI approval, and freeze |
| Numeric performance thresholds | Not specified | Define before final test access |
| Conflicts of interest and funding declaration | Pending | Complete formal declaration |
| CEI favorable opinion | Not obtained | Mandatory |

**Readiness decision:** `ETHICS_PENDING`. Public-data and planning activities may continue. Recruitment and participant recording may not begin.

## 28. References

1. World Health Organization. (2025). *Global tuberculosis report 2025*. https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025
2. Ministerio de Salud del Peru. (2025). *La tuberculosis es curable: deteccion temprana y tratamiento completo son la clave*. https://www.gob.pe/institucion/minsa/noticias/1189372-la-tuberculosis-es-curable-deteccion-temprana-y-tratamiento-completo-son-la-clave
3. Universidad Nacional Mayor de San Marcos. (2025). *Reglamento del Comite de Etica en Investigacion de la UNMSM*, Resolucion Rectoral No. 008534-2025-R. https://vrip.unmsm.edu.pe/normas/RR_008534-2025-R.pdf
4. Congreso de la Republica del Peru. (2011). *Ley No. 29733, Ley de Proteccion de Datos Personales*. https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733
5. Ministerio de Justicia y Derechos Humanos. (2024). *Decreto Supremo No. 016-2024-JUS: Reglamento de la Ley No. 29733*. https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus
6. Consejo Nacional de Ciencia, Tecnologia e Innovacion. (2024). *Codigo Nacional de Integridad Cientifica*, approved by Resolucion de Presidencia No. 028-2024-CONCYTEC-P. https://repositorio.concytec.gob.pe/entities/publication/b0fe4014-f79a-4782-a567-035fcbb20b21
7. National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). *The Belmont Report*. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/
8. Chu, W. (2025). *MEDISEG: A large-scale dataset of medication images with instance segmentation masks for preventing adverse drug events* (Version 2). City St George's Research Data. https://doi.org/10.25383/city.28574786.v2
9. Lee, H., & Youm, S. (2021). Development of a Wearable Camera and AI Algorithm for Medication Behavior Recognition. *Sensors, 21*(11), 3594. https://doi.org/10.3390/s21113594
10. Nguyen, T. T., Nguyen, P. L., Kawanishi, Y., Komamizu, T., & Ide, I. (2024). Zero-Shot Pill-Prescription Matching With Graph Convolutional Network and Contrastive Learning. *IEEE Access, 12*, 55889-55904. https://doi.org/10.1109/ACCESS.2024.3390153

## Appendix A. Draft acceptability and usability questionnaire

### Instructions

Please rate each statement about today's recording procedure. Do not include your diagnosis or medication name.

| Response | Meaning |
|---:|---|
| 1 | Strongly disagree |
| 2 | Disagree |
| 3 | Neither agree nor disagree |
| 4 | Agree |
| 5 | Strongly agree |

| No. | Statement | Domain |
|---:|---|---|
| 1 | The instructions for the recording session were clear. | Procedural usability |
| 2 | The steps required during the session were easy to follow. | Procedural usability |
| 3 | The recording session caused little physical burden or fatigue. | Burden |
| 4 | Recording only my hands and lower facial area was acceptable to me. | Privacy acceptability |
| 5 | Knowing that the full face and audio were not recorded increased my comfort. | Privacy acceptability |
| 6 | I felt able to stop or withdraw from the session without pressure. | Autonomy |
| 7 | A system like this could fit into a normal medication routine if it were validated. | Perceived usefulness |
| 8 | I would be concerned if the system incorrectly confirmed that a pill had been taken. | Error concern |
| 9 | A trained person should review uncertain or disputed system results. | Human oversight |
| 10 | I would be willing to participate in a similar recording session again. | Overall acceptability |

Questionnaire responses will be stored under the participant code and separately from consent and identity records. Items will be reported individually unless a later validated scoring plan is approved.
