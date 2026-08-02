# Data Management Plan (Draft v0.1)

## AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis

**Data steward:** Jean Pierre Tincopa Flores  
**Contact:** jean.tincopaf@unmsm.edu.pe  
**Institution:** Universidad Nacional Mayor de San Marcos (UNMSM)  
**Document date:** 1 August 2026  
**Related document:** `09_ethics/ethics_protocol.md`  
**Status:** Planning document; human-data collection remains `ETHICS_PENDING`

## 1. Purpose and scope

This plan governs data created, obtained, transformed, analyzed, shared, retained, and destroyed across the AI-DOTS project. It preserves the distinction between:

1. the current MEDISEG object-detection proof of concept, which uses public pill images and no human participants; and
2. a future controlled ingestion-recognition pilot with consenting adults, which would produce personal video data.

The plan covers public source data, annotations, participant video, consent and linkage records, derived features, model artifacts, metrics, code, documentation, and audit logs. No human recruitment or recording may begin until the applicable UNMSM Research Ethics Committee (CEI) has issued a favorable opinion and the operational controls below have been verified.

## 2. Data inventory and classification

| Data class | Examples and format | Source | Personal/sensitive status | Repository treatment |
|---|---|---|---|---|
| Public MEDISEG source | JPEG/PNG images, COCO JSON, `metadata.csv` | MEDISEG v2, DOI 10.25383/city.28574786.v2 | No people or patient data in the used 3-pills subset | Raw archive excluded from Git; retrieved from official source and checksum-verified |
| Current derived ML data | YOLO TXT labels, `data.yaml`, split manifest, checksums | Deterministic processing of MEDISEG | Non-personal | May be versioned if license and size permit |
| Current experimental outputs | Aggregate and per-class metrics, CSV, JSON, plots, predictions | YOLO26n proof of concept | Non-personal | Stored under `05_pipeline/results/` |
| Model artifacts | Weights, optimizer state, configurations | Training process | Normally non-personal, but future models may encode participant-derived information | Configuration and provenance versioned; weights shared only after privacy and license review |
| Future participant video | Hands, pill, and lower facial area; MP4 or equivalent; audio disabled | Consenting adults in controlled pilot | Personal and potentially sensitive; indirectly identifiable | Never committed to GitHub or a public DVC remote |
| Consent and linkage records | Signed consent, participant-code key, withdrawal log | Researcher and participant | Directly identifying and confidential | Stored separately from research video in restricted encrypted storage |
| Future derived human data | Frames, bounding boxes, embeddings, event labels, quality metadata | Processing of participant video | Pseudonymous and potentially re-identifiable | Restricted by default; public release requires documented anonymization review |
| Reproducibility materials | Source code, notebooks, pinned environment, seeds, logs | Research workflow | Non-personal after review | Version-controlled in GitHub |
| Course anonymization lab | Synthetic hospital table, aggregate outputs, figures | Session 10 notebook | Synthetic; no real people | Executed notebook may be public |

Every new data asset must receive an owner, source, purpose, classification, format, location, access group, checksum where appropriate, retention trigger, and deletion rule before use.

## 3. Collection and data minimization

### 3.1 Current public-data phase

The MEDISEG archive is downloaded from its official DOI record. The pipeline verifies archive size and MD5, audits image/annotation consistency, converts COCO boxes to YOLO format, and creates deterministic train/validation/test splits with `seed=42`. The source archive is not redistributed through this repository.

### 3.2 Future human-participant phase

Only adults aged 18 or older, without active tuberculosis, who already take oral medication daily for a non-contagious condition will be eligible. The study will observe an ordinarily scheduled dose and will not request an extra dose or treatment change.

Collection is limited to:

- hands;
- pill and relevant container;
- lower facial area required for the ingestion-recognition task;
- minimal technical metadata such as pseudonymous participant code, recording condition, device category, angle, lighting, occlusion, and timestamp relative to the session.

The full face, audio, name, national ID, voice, detailed diagnosis, prescription, home address, contacts, and precise location will not enter the ML dataset. Any future additional variable requires scientific justification, consent-language review, and CEI approval.

Before each recording, the researcher will verify the field of view and audio-off state. Takes capturing the full face, voice, documents, screens, names, or unnecessary surroundings will be rejected and deleted before annotation.

## 4. File organization, naming, and version control

Participant data will use random identifiers unrelated to initials, dates of birth, or enrollment order. A proposed convention is:

`PID-<random_id>_S<session>_C<condition>_<timestamp>.<ext>`

The code-to-identity key will never appear in filenames or the analysis workspace. Dataset releases and derived bundles will use semantic versions (`vMAJOR.MINOR.PATCH`) and include:

- a data dictionary;
- provenance and transformation history;
- inclusion/exclusion rules;
- split-generation method and seed;
- checksums;
- license or data-use terms;
- known limitations and unresolved fields;
- change log.

Git will track code, Markdown documentation, lightweight configurations, and non-sensitive aggregate results. Large public or approved non-sensitive data may later be tracked by DVC. Participant video, consent forms, identity keys, credentials, encryption keys, and raw access logs must be excluded through repository rules and pre-commit review.

## 5. Storage, encryption, access, and backup

Future raw and pseudonymous participant data will be stored in an encrypted container on a researcher-controlled drive. A second encrypted backup will be kept on a physically separate controlled device. Both copies will use strong current encryption, separate credentials, and automatic locking when not in use.

Access is limited to:

- Jean Pierre Tincopa Flores, as researcher and data steward; and
- one formally authorized research adviser, only to the extent required for supervision.

Access by any additional person requires a documented role, confidentiality obligation, least-privilege approval, and access-log entry. Credentials and encryption recovery material will be stored separately from the encrypted data. Where supported, multifactor authentication will be enabled.

Operational implementation is **PARTIAL**: the exact encryption product, device identifiers, physical backup location, credential-recovery method, and access-log mechanism must be recorded and tested before recruitment. Unencrypted removable media, email attachments, messaging applications, shared consumer folders, and public cloud links are prohibited for participant data.

Backups will be verified at least quarterly and before major processing changes. A restore test will confirm that backup integrity is real rather than assumed. Backup copies inherit the same classification, access restrictions, retention clock, and deletion requirement as the primary data.

## 6. Pseudonymization and anonymization strategy

### 6.1 Pseudonymization at collection

A random participant code will replace direct identity in all research files. Consent documents and the linkage key will be encrypted and stored separately from video and annotations. The working dataset will contain only the participant code and variables necessary for analysis. File metadata will be removed when not needed.

Pseudonymization reduces exposure but is not anonymization. Raw video of hands and the lower face will always be treated as potentially re-identifiable and will not be released publicly.

### 6.2 Tabular release control

Before any participant-derived table is shared, the researcher will identify direct identifiers, quasi-identifiers, and sensitive attributes. Direct identifiers will be removed. Quasi-identifiers will be generalized or suppressed, and small cells will be withheld.

The provisional release target is:

- `k >= 5` for every released quasi-identifier combination;
- `l >= 2` when a sensitive categorical attribute is present; and
- a documented distribution check when group-level skew could still disclose a sensitive value, applying t-closeness or suppressing the release if needed.

These are minimum release gates, not proof of zero re-identification risk. Utility loss from generalization, suppression, or aggregation will be measured and reported.

### 6.3 Aggregate statistics and differential privacy

Current MEDISEG metrics do not require differential privacy because the used subset contains no human participants. For future participant-derived count releases, differential privacy will be evaluated rather than automatically claimed.

The provisional starting point is Laplace noise with `epsilon = 1` per approved count query and a cumulative public-release budget no greater than `epsilon = 3` for the same participant set. Sensitivity, clipping bounds, composition, randomization, utility loss, and the budget ledger must be documented. If results become misleading or the privacy budget is exhausted, the query will not be released.

No claim of differentially private model training will be made unless an appropriate method such as DP-SGD is implemented, its assumptions are satisfied, and epsilon/delta accounting is independently verified.

## 7. Data quality and reproducibility

Quality controls include:

- checksum verification at acquisition and transfer;
- image readability and annotation-schema validation;
- documented exclusions and corrections;
- deterministic splitting with recorded seed;
- exact-duplicate checks across splits;
- group-aware splitting when acquisition-session identifiers become available;
- range and consistency checks for labels and technical metadata;
- code, environment, dependency, and model-configuration capture;
- preservation of failed runs and negative results when scientifically relevant;
- versioned changes rather than silent overwriting.

Human-video annotation guidelines, reviewer procedure, inter-annotator agreement target, disagreement resolution, and label-quality sample must be defined before annotation begins. These items are currently **UNKNOWN - to be specified in protocol v1.0**.

## 8. FAIR implementation

| FAIR principle | Planned implementation | Current status |
|---|---|---|
| Findable | Persistent DOI for MEDISEG; structured repository; descriptive filenames; data dictionary; version tags; checksums | PARTIAL - repository structure and source DOI exist; formal metadata record remains pending |
| Accessible | Public code and aggregate outputs through GitHub; source data through its official DOI; controlled access for participant data | PARTIAL - participant access procedure must be operationalized |
| Interoperable | COCO JSON, YOLO TXT/YAML, CSV, JSON, Markdown, standard image/video formats, documented class identifiers | PRESENT for current proof of concept |
| Reusable | Provenance, preprocessing, seeds, splits, metrics, limitations, licenses, and intended/prohibited uses documented | PARTIAL - repository license is still UNKNOWN and human-data reuse requires consent/CEI terms |

FAIR does not mean that all data must be open. Sensitive participant data will be as accessible as ethically and legally permissible, not as open as technically possible.

## 9. Sharing and publication

The following may be shared after quality, privacy, and license review:

- source code and executed notebooks;
- environment and configuration files;
- aggregate and per-class metrics;
- non-identifying plots and documentation;
- synthetic teaching data;
- participant-derived tables only after the release gates in Section 6 are passed;
- model weights only after privacy leakage, license, and intended-use review.

The following will not be public:

- raw or clipped participant video;
- extracted participant frames that remain identifiable;
- audio;
- consent forms;
- names or contact information;
- participant-code linkage key;
- raw access and incident logs;
- encryption keys or credentials.

Requests for controlled access to participant-derived data require a written scientific purpose, CEI-compatible approval, a data-use agreement, security review, and evidence that the consent permits the proposed use. Approval is not automatic.

## 10. Retention and secure destruction

Retention clocks begin when the relevant validation phase is formally closed:

| Data | Retention period | End-of-period action |
|---|---:|---|
| Raw participant video and identifiable extracted frames | 1 year after validation concludes | Cryptographic erasure from primary and backup; deletion logged and verified |
| Consent forms and participant-code linkage | 5 years | Secure destruction after confirming no unresolved withdrawal, audit, or legal hold |
| Pseudonymous derived participant data | 5 years | Delete or irreversibly anonymize following documented review |
| Aggregate metrics, code, environment, and study documentation | 5 years minimum; non-personal public artifacts may remain longer if ethically and legally permissible | Archive or retain under versioned repository policy |
| Public MEDISEG source copy | Only while required for reproducibility and subject to source license | Delete local copy when no longer required; authoritative source remains the DOI record |
| Access, incident, amendment, and deletion logs | 5 years | Secure destruction unless an approved longer requirement applies |

Deletion must cover primary storage, backup, working copies, temporary exports, annotation workspaces, and retired devices. If a legal, institutional, or research-integrity hold requires longer retention, access remains restricted and the reason, scope, and new review date will be documented.

## 11. Incident response

A suspected loss, unauthorized disclosure, malware event, credential compromise, or accidental public commit will trigger:

1. immediate containment and access suspension;
2. preservation of a minimal incident record;
3. assessment of affected data, people, and risk;
4. notification to the adviser, UNMSM/CEI, and applicable data-protection authority or participants when required;
5. credential/key rotation and recovery from a verified backup;
6. corrective action and protocol amendment;
7. documented closure and lessons learned.

The contact route, notification responsibilities, and legally applicable time limits must be finalized before collection.

## 12. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| Researcher/data steward | Consent implementation, collection, classification, access approval, quality control, backups, release review, incident response, retention and deletion |
| Authorized adviser | Scientific supervision and approved limited data access; confidentiality and incident-reporting duties |
| UNMSM CEI | Ethical review, favorable/unfavorable opinion, monitoring, guidance, and review of incidents or amendments |
| Future annotator, if approved | Minimum necessary pseudonymous access, training, confidentiality agreement, no local copies |
| External recipient, if approved | Data-use agreement, purpose limitation, security controls, no re-identification, deletion/return at end |

No role may unilaterally repurpose participant data beyond the approved protocol and consent.

## 13. Legal and institutional compliance checklist

| Requirement | Application to AI-DOTS | Status |
|---|---|---|
| UNMSM CEI Regulation, RR No. 008534-2025-R | Favorable ethics opinion and informed consent before human research; confidentiality and participant protection | NEEDS_ACTION before recruitment |
| Belmont Report | Respect, beneficence, justice, consent, risk-benefit assessment, fair selection | ADDRESSED in `09_ethics/ethics_protocol.md` |
| CONCYTEC National Code of Scientific Integrity | Transparent, responsible, reproducible data practices and honest reporting | PARTIAL - continue across the project |
| Peru Law No. 29733 | Lawful, purpose-limited, proportionate, secure processing and participant rights | NEEDS_ACTION before collection |
| Supreme Decree No. 016-2024-JUS | Current regulation of Law No. 29733; security, accountability, and data-subject procedures | NEEDS_ACTION before collection |
| Consent-compatible reuse | New use or sharing must fit the consent and CEI approval | NOT YET APPLICABLE |
| International transfer / GDPR | No international participant-data transfer planned | NOT APPLICABLE unless the plan changes |

## 14. Review and amendment schedule

This DMP will be reviewed:

- before CEI submission;
- before the first participant is recruited;
- before a new data type, variable, recipient, storage service, or model use is introduced;
- after any incident or substantial protocol amendment;
- at least annually during active data processing;
- at the end of validation and before each public release;
- at each retention/deletion milestone.

All amendments will be versioned with date, author, rationale, affected data, risk impact, approval requirement, and migration or deletion action.

## 15. References

1. Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. https://doi.org/10.1038/sdata.2016.18
2. U.S. Department of Health and Human Services. *The Belmont Report*. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/
3. Universidad Nacional Mayor de San Marcos. Resolucion Rectoral No. 008534-2025-R, *Reglamento del Comite de Etica en Investigacion de la UNMSM*. https://vrip.unmsm.edu.pe/normas/RR_008534-2025-R.pdf
4. Consejo Nacional de Ciencia, Tecnologia e Innovacion. *Codigo Nacional de Integridad Cientifica*, approved by Resolucion de Presidencia No. 028-2024-CONCYTEC-P. https://repositorio.concytec.gob.pe/entities/publication/b0fe4014-f79a-4782-a567-035fcbb20b21
5. Congreso de la Republica del Peru. Law No. 29733, *Ley de Proteccion de Datos Personales*. https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733
6. Autoridad Nacional de Proteccion de Datos Personales. Supreme Decree No. 016-2024-JUS, *Reglamento de la Ley No. 29733*. https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus

