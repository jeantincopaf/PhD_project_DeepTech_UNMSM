# Educational EU AI Act Annex IV Crosswalk

This crosswalk maps current proof-of-concept documentation to Annex IV of Regulation (EU) 2024/1689: [official EUR-Lex text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689).

It is an educational gap analysis, not legal advice, conformity assessment, or a compliance claim. This academic proof of concept has not been placed on the EU market or put into service. Article 2 contains exclusions for systems specifically developed and put into service for scientific research and for research, testing, and development before market placement, subject to its conditions. Whether a future AI-DOTS system would be in scope or high-risk is **UNKNOWN - requires fact-specific legal assessment**.

Status key: **PRESENT**, **PARTIAL**, **GAP**, or **NOT APPLICABLE AT THIS STAGE**.

| Annex IV topic | Status | Current evidence | Gap / next action |
|---|---|---|---|
| 1. Purpose, provider, version | PARTIAL | Model Card identifies research purpose, v0.1, owner, contact. | Define legal provider, territories, and regulated purpose. |
| 1. Hardware/software interaction | PARTIAL | Colab, Ultralytics, PyTorch, NVIDIA L4 recorded. | Specify interfaces, data flows, dependencies, failures. |
| 1. Software/computational versions | PRESENT | `environment.json`, training arguments, notebook, checksums. | Add a software bill of materials. |
| 1. Market forms | NOT APPLICABLE AT THIS STAGE | No product is marketed or deployed. | Document delivery form before deployment. |
| 1. Hardware requirements | PARTIAL | Training hardware and image size recorded. | Establish supported inference hardware and bounds. |
| 1. Interface/instructions | GAP | No user-facing system. | Produce interface, warnings, instructions, accessibility requirements. |
| 2(a). Methods/pretrained tools | PRESENT | YOLO26n and workflow documented. | Record exact weight provenance and license. |
| 2(b). Design specifications | PARTIAL | Architecture, input, parameters, metrics documented. | Add requirements, thresholds, acceptance criteria, rationale. |
| 2(c). Architecture/resources | PARTIAL | Environment and training configuration available. | Add component/data-flow diagrams and resource envelopes. |
| 2(d). Data/provenance/labeling/cleaning | PRESENT | Datasheet and pipeline artifacts document these. | Obtain grouping metadata; resolve governance unknowns. |
| 2(e). Human oversight | PARTIAL | Autonomous clinical use prohibited; human review required. | Define roles, competencies, override, escalation. |
| 2(f). Lifecycle changes | GAP | Only v0.1 described. | Adopt change log, approval, impact reassessment. |
| 2(g). Validation/testing and impacts | PARTIAL | Held-out aggregate/per-class results and limitations. | Add seeds, intervals, external/robustness/calibration testing. |
| 2(h). Cybersecurity | GAP | No threat model or security testing. | Assess poisoning, adversarial input, access, logging, dependencies. |
| 3. Monitoring/function/limitations/oversight | PARTIAL | Capabilities, misuse, risks documented. | Define monitoring, alerts, incidents, input specifications. |
| 4. Metric appropriateness | PARTIAL | Metrics and non-clinical meaning stated. | Link thresholds to harms; add uncertainty and latency. |
| 5. Risk management | GAP | Ethical risks discussed; no formal register. | Establish lifecycle risk process and ownership. |
| 6. Lifecycle changes | GAP | No deployed lifecycle. | Define revalidation triggers, rollback, traceability. |
| 7. Standards/specifications | GAP | None claimed. | Identify applicable standards after classification. |
| 8. EU declaration of conformity | NOT APPLICABLE AT THIS STAGE | No market product or assessment. | Prepare only if future classification requires it. |
| 9. Post-market monitoring | GAP | No deployment. | Define feedback, incidents, drift, corrective action. |

## Priority gaps before any real-world study or deployment

1. Resolve repository/model license and upstream-weight terms.
2. Establish data governance, acquisition grouping, and human-data ethics.
3. Define users, oversight, failure response, and prohibited use operationally.
4. Expand validation to multiple seeds, external conditions, robustness, uncertainty, latency, and clinically meaningful endpoints.
5. Create risk-management, cybersecurity, lifecycle, and monitoring plans.

Crosswalk tally: **3 PRESENT, 9 PARTIAL, 7 GAP, 2 NOT APPLICABLE AT THIS STAGE**.

## Documentation scorecard

| Course criterion | Result | Evidence |
|---|---:|---|
| Model Card has all 9 sections | 1/1 | `model_card.md` sections 1-9 |
| Datasheet has all 7 sections | 1/1 | `datasheet.md` sections 1-7 |
| Misuse/out-of-scope stated | 1/1 | Model Card section 2 |
| Performance variation addressed | 1/1 | `seed=42` and unknown standard deviation |
| Disaggregated metrics | 1/1 | Per-class table |
| Dataset "should not be used" stated | 1/1 | Datasheet section 5 |
| Collection explains "How collected" | 1/1 | Datasheet section 3 |
| Gaps flagged with "UNKNOWN" | 1/1 | Both documents |
| **Total** | **8/8** | **All criteria met** |
