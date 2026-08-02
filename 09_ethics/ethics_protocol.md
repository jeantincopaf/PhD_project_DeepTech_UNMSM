# Ethics Protocol (Draft v0.1)

## AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis

**Researcher:** Jean Pierre Tincopa Flores  
**Contact:** jean.tincopaf@unmsm.edu.pe  
**Institution:** Universidad Nacional Mayor de San Marcos (UNMSM)  
**Document date:** 1 August 2026  
**Ethics status:** **ETHICS_PENDING - not yet submitted or approved**

> This document is a planning protocol. No participant recruitment, consent, recording, or human-data processing may begin until the applicable UNMSM Research Ethics Committee (CEI) has issued a favorable opinion and the final consent and data-management documents have been approved.

## 1. Purpose and ethical scope

AI-DOTS investigates whether computer vision can classify tuberculosis pill brands and, in a later phase, detect an ingestion action in video. The long-term purpose is to study a potential technical alternative to some burdens of in-person DOTS supervision. The system is not a clinical product and must not be described as capable of proving treatment adherence or replacing healthcare personnel.

The project has two ethically distinct phases:

1. **Current technical proof of concept:** object detection on the public MEDISEG v2 3-pills dataset. This phase contains pill images and no human participants, patient records, tuberculosis status, or ingestion events.
2. **Future controlled human-participant pilot:** video collection from consenting adults without active tuberculosis who already take oral medication daily for a non-contagious condition. This phase would test only the technical recognition of a routine medication-taking action.

Results from MEDISEG do not authorize the human-participant phase and do not establish clinical validity.

## 2. Ethical framework

The protocol applies the Belmont principles of respect for persons, beneficence, and justice.

### 2.1 Respect for persons

Participation will be voluntary and based on written informed consent in clear Spanish. Candidates will receive the study purpose, procedures, duration, data collected, foreseeable risks, possible benefits, confidentiality measures, intended and prohibited uses, right to ask questions, and right to withdraw without penalty.

The pilot will include only adults with capacity to consent. It will exclude minors and people whose autonomy may be reduced or whose relationship with the researcher could create undue influence. Declining or withdrawing will not affect healthcare, employment, grades, or access to services.

### 2.2 Beneficence and non-maleficence

The study will minimize risk by observing a medication event that would occur as part of the participant's normal routine. The researcher will not prescribe medication, change timing or dosage, request an extra dose, or advise on treatment. Recording will stop immediately if the participant reports discomfort or difficulty.

No direct medical benefit will be promised. The expected benefit is generalizable technical knowledge. Risks include discomfort while being recorded, accidental disclosure of health-related information, re-identification from video, algorithmic errors, and future misuse of adherence predictions. These risks are addressed through data minimization, restricted framing, security controls, human oversight, and strict limits on use.

### 2.3 Justice

Recruitment will be based on the study criteria rather than convenience, economic vulnerability, or institutional dependence. The pilot will not target people with active tuberculosis, minors, detained persons, or people under the researcher's direct academic or employment authority.

Technical performance will be examined across lighting, occlusion, camera angle, and device conditions so that error burdens are not hidden by aggregate metrics. Collection of demographic or other sensitive variables is not currently planned. Any future subgroup variable must have a scientific justification, explicit consent, data-minimization review, and CEI approval.

## 3. Participants

### 3.1 Inclusion criteria

Participants must:

- be 18 years of age or older;
- have capacity to provide informed consent;
- have no active tuberculosis;
- have a non-contagious condition;
- already take oral medication daily as part of their usual care;
- be willing to follow the recording procedure without changing the prescribed regimen.

### 3.2 Exclusion criteria

Potential participants will be excluded if they:

- are under 18;
- have active or suspected tuberculosis or another contagious condition relevant to the setting;
- cannot provide autonomous informed consent;
- report dysphagia, current swallowing difficulty, or another condition that makes observation unsafe;
- would need to take an additional or rescheduled dose solely for the study;
- are students, employees, patients, or others directly dependent on the researcher in a way that could create pressure to participate.

### 3.3 Sample and compensation

The target sample size and its statistical justification are **UNKNOWN - to be established in protocol v1.0 before CEI submission**. Compensation or reimbursement is also **UNKNOWN - to be decided before recruitment and stated in the consent form**. Any payment must compensate time or expenses without becoming an undue inducement.

## 4. Procedures and recording boundaries

Each participant would be recorded only during an ordinarily scheduled medication event. The camera frame will be restricted to:

- the participant's hands;
- the pill and relevant container;
- the lower facial area needed to observe the ingestion action.

The full face will not be recorded. Audio will be disabled because it is not required for the research objective. The researcher will check the frame before recording and stop or discard any take that captures the full face, names, documents, screens, voices, location details, or other unnecessary identifiers.

Session duration, number of repetitions, camera distance, and stopping rules are **UNKNOWN - to be finalized before CEI submission**. No recording will occur in clinical care unless separately authorized.

## 5. Informed consent and withdrawal

The final consent form will explain:

- that this is research, not treatment or adherence supervision;
- that participation is voluntary;
- exactly which body areas will be recorded;
- that lower-face and hand video may remain indirectly identifiable even without a full face;
- that audio is disabled;
- who will access raw and derived data;
- whether data will be used for model training;
- the retention and destruction schedule;
- that raw video will not be published;
- foreseeable risks and the absence of guaranteed personal benefit;
- how to withdraw and contact the researcher or CEI.

Participants may stop a session immediately and request deletion of their identifiable or pseudonymous raw recordings until the analysis-freeze date defined in the final consent form. After data have been irreversibly aggregated into published statistics, removal from those aggregate results may not be possible; this limit must be explained before consent.

## 6. Risk-benefit assessment

| Risk | Likelihood / severity | Mitigation |
|---|---|---|
| Accidental capture of the full face or surroundings | Low / moderate privacy impact | Restricted frame, pre-recording check, audio disabled, immediate deletion of invalid takes |
| Re-identification from hands or lower-face video | Low to moderate / moderate | Pseudonymous IDs, separate linkage file, encryption, restricted access, no raw-video publication |
| Disclosure of medication or health information | Low / potentially significant | Collect only eligibility confirmation; do not record diagnosis or prescription unless separately justified |
| Discomfort, embarrassment, or fatigue | Low / mild | Short sessions, breaks, immediate stop without penalty |
| Swallowing difficulty or medication error | Low / potentially significant | Observe only the participant's normal prescribed dose; no extra dose or treatment advice; exclude reported dysphagia |
| False model confirmation of ingestion | Plausible / potentially serious in future use | Research-only use, no automated clinical action, human review, explicit validation thresholds |
| False model rejection of genuine ingestion | Plausible / burdensome or stigmatizing | Human review, appeal/correction pathway, no punitive response |
| Secondary surveillance or coercive use | Plausible / serious | Purpose limitation, access controls, license/use restrictions, governance review before any deployment |

The risk-benefit balance is provisional and must be reviewed by the CEI.

## 7. Privacy and data protection

Video of hands and the lower face will be treated as personal and potentially sensitive data even when the full face is absent.

Planned controls are:

- assign a random participant code at collection;
- store the code-to-identity linkage separately from recordings;
- avoid collecting names, national IDs, detailed diagnoses, prescriptions, voices, or location metadata in the ML dataset;
- remove unnecessary file metadata;
- encrypt data at rest and in transit;
- limit raw-data access to the researcher and specifically authorized supervisors;
- maintain an access log and incident record;
- never commit raw participant videos to GitHub or a public DVC remote;
- publish only aggregate metrics, non-identifying documentation, and artifacts approved for release;
- securely delete data when the approved retention period ends.

The exact storage platform, encryption implementation, authorized-person list, backup arrangement, retention period, and deletion verification are **UNKNOWN - mandatory items for the Session 10 Data Management Plan and CEI review before collection**.

Processing must comply with Peru's Law No. 29733 and its current Regulation approved by Supreme Decree No. 016-2024-JUS. Participants will be informed how to exercise applicable rights of access, rectification, cancellation, and opposition. A privacy-impact assessment will be completed before the human pilot.

## 8. Fairness, error allocation, and distribution shift

For a future ingestion-validation system, a **false positive** means reporting that ingestion occurred when it did not. This may conceal a missed dose and create unsafe reassurance. A **false negative** means rejecting a genuine ingestion event, which may burden, stigmatize, or unfairly penalize the participant.

The primary safety priority will be to control and report the false-positive rate, including variation across relevant technical conditions. False-negative rate, precision, recall, calibration, and uncertainty must also be reported; selecting one fairness criterion does not erase other harms.

Before any new population or setting is considered, the model must be re-evaluated for distribution shift involving pill brands, capture devices, lighting, camera angle, occlusion, internet availability, and urban/rural operating conditions. Performance degradation beyond pre-specified thresholds will pause use and trigger investigation and revalidation. Those thresholds are **UNKNOWN - to be defined before deployment-oriented research**.

## 9. Human oversight, monitoring, and redress

The system will not autonomously determine adherence, apply sanctions, change treatment, or notify third parties. Any model output used in later research must be reviewable by a trained human with access to uncertainty and failure information.

Participants must have a documented channel to:

- report a concern or adverse event;
- ask what data are held about them;
- request correction or eligible deletion;
- contest an incorrect system output;
- withdraw without penalty.

Protocol deviations, privacy incidents, unexpected risks, and serious adverse events will be recorded and reported to the CEI according to its requirements. Data collection will be suspended if an uncontrolled risk threatens participant rights, health, integrity, or dignity.

## 10. Dual-use and prohibited uses

The data and system must not be used for covert surveillance, punitive adherence enforcement, employment or insurance decisions, identity recognition, emotion inference, diagnosis, prescription control, law-enforcement assessment, or training unrelated face/biometric models.

No third party may receive identifiable recordings without a new lawful basis, participant information or consent as applicable, a data-sharing agreement, security review, and CEI authorization.

## 11. Scientific integrity and transparency

The study will preserve version-controlled protocols, preprocessing decisions, seeds, splits, environments, model configurations, failures, negative findings, and amendments. Results will be reported without fabrication, falsification, selective omission, or unsupported clinical claims.

Conflicts of interest and funding sources must be declared before CEI submission. Current status: **UNKNOWN - formal declaration pending**. AI-assisted drafting or coding must be reviewed by the researcher and logged according to the repository's future `12_integrity/ai_use_policy.md`; responsibility for the content remains with the researcher.

## 12. Ethics approval and readiness checklist

Under the 2025 UNMSM CEI Regulation, research involving observation or collection of identifiable human data requires ethics review. The faculty CEI evaluates projects from students and graduates; research must have project approval and voluntarily signed/accepted informed consent before it begins.

| Requirement | Status | Required action |
|---|---|---|
| Scope and participant population defined | PASS | Maintain current adult, non-TB pilot limits |
| Recording minimization defined | PASS | Verify framing and audio-off procedure in a dry run without participants |
| Informed-consent pathway | NEEDS_ACTION | Draft participant information sheet and consent form |
| CEI favorable opinion | NEEDS_ACTION | Submit final protocol before recruitment or recording |
| Risk assessment | PARTIAL | CEI review and operational stopping procedure required |
| Secure storage and access control | NEEDS_ACTION | Specify implementation in the Data Management Plan |
| Retention and deletion period | NEEDS_ACTION | Define and include in consent |
| Sample-size justification | NEEDS_ACTION | Complete before protocol v1.0 |
| Compensation/reimbursement | UNKNOWN | Decide and disclose before recruitment |
| Data-sharing plan | PARTIAL | Raw video prohibited from public release; define any controlled sharing |
| Fairness and distribution-shift plan | PARTIAL | Pre-specify subgroup/condition metrics and thresholds |
| Conflict-of-interest declaration | NEEDS_ACTION | Complete before CEI submission |

**Readiness decision:** `ETHICS_PENDING`. Planning and use of public non-human MEDISEG data may continue. Human recruitment and video recording may not begin.

## 13. References

1. U.S. Department of Health and Human Services, *The Belmont Report*. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/
2. Universidad Nacional Mayor de San Marcos, Resolucion Rectoral No. 008534-2025-R, *Reglamento del Comite de Etica en Investigacion de la UNMSM*. https://vrip.unmsm.edu.pe/normas/RR_008534-2025-R.pdf
3. Consejo Nacional de Ciencia, Tecnologia e Innovacion, *Codigo Nacional de Integridad Cientifica*, approved by Resolucion de Presidencia No. 028-2024-CONCYTEC-P. https://repositorio.concytec.gob.pe/entities/publication/b0fe4014-f79a-4782-a567-035fcbb20b21
4. Congreso de la Republica del Peru, Ley No. 29733, *Ley de Proteccion de Datos Personales*. https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733
5. Autoridad Nacional de Proteccion de Datos Personales, Decreto Supremo No. 016-2024-JUS, *Reglamento de la Ley No. 29733*. https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus
