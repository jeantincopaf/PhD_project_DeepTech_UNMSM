# AI-DOTS: Computer Vision-Driven Pill Ingestion Verification for the Treatment of Tuberculosis

**Author:** Jean Pierre Tincopa Flores      
**University:** Universidad Nacional Mayor de San Marcos (UNMSM)     
**Program:** PhD in Deep Tech focused on Artifitial Intelligence and Emerging Technologies      
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies       

---

## What this is

This repository documents the doctoral research project for the development of a computer vision system capable of classifying tuberculosis pill brands and detecting real-time pill ingestion. The goal is to provide a technological alternative to in-person DOTS (Directly Observed Treatment, Short-course) supervision, reducing the burden on healthcare centers and improving patient adherence to treatment — particularly in remote and marginalized areas of Peru.

---

## Repository Structure

| Folder | Content |
|--------|---------|
| `01_paradigm/` | Paradigm Justification Statement |
| `02_method/` | Method-Fit Matrix |
| `03_protocol/` | Research Protocol versions v0.1 and v1.0 |
| `04_literature/` | Systematic Literature Review + PRISMA diagram + Gap Analysis |
| `05_pipeline/` | Reproducible ML pipeline, exploratory baseline, and confirmatory robustness results |
| `06_repro_audit/` | Reproducibility audit of the published Zero-PIMA study |
| `07_model_card/` | Model Card, Dataset Datasheet, and educational EU AI Act Annex IV crosswalk |
| `09_ethics/` | AI-DOTS ethics protocol and executed COMPAS fairness lab |
| `10_data_mgmt/` | FAIR Data Management Plan and executed anonymization lab |
| `11_bias_audit/` | COMPAS race bias audit with before/after AIF360 metrics |
| `12_integrity/` | Retracted YOLOv5 paper analysis and personal AI use policy |

---

## Research Context

Tuberculosis is a public health priority in Peru and worldwide. According to the WHO Global Tuberculosis Report 2025, an estimated 10.7 million people were infected globally in 2024, and Peru registered 33,049 cases that same year (MINSA). The current DOTS strategy requires in-person supervision by healthcare workers, which is very costly and logistically unfeasible in remote areas.

This research proposes a computer vision system that:
1. **Classifies** the type/brand of tuberculosis pills
2. **Detects** pill intake in real time via video analysis

---

## Research Paradigm

**Quantitative empirical (positivist)** — The central question is answered by the algorithm's performance metrics (accuracy, precision, recall, F1-score), not by subjective interpretations.

---

## Method

Controlled dataset generation + deep learning pipeline with:
- CNN-based architectures for pill classification (ResNet, EfficientNet, YOLO)
- Temporal action recognition for ingestion detection
- Robustness testing under varying lighting, occlusion, and camera angles
- Quasi-experimental evaluation with cross-validation

---

## Current Status

- [x] `01_paradigm/` — Paradigm justification completed
- [x] `02_method/` — Method-fit matrix completed
- [x] `03_protocol/` — Protocol v1.0 complete; v2.0 remains pending peer-review integration
- [x] `04_literature/` — Systematic review in progress
- [x] `05_pipeline/` — MEDISEG proof of concept completed and strengthened with three-detector screening, 40-epoch training, and five-seed YOLO26n evaluation
- [x] `06_repro_audit/` - Zero-PIMA reproducibility audit completed
- [x] `07_model_card/` - Model Card, Datasheet, and Annex IV gap analysis completed
- [x] `09_ethics/` - Ethics protocol drafted; COMPAS fairness lab executed
- [x] `10_data_mgmt/` - FAIR Data Management Plan and anonymization lab completed
- [x] `11_bias_audit/` - COMPAS bias audit and Reweighing mitigation completed
- [x] `12_integrity/` - Retracted medical-imaging paper analysis and personal AI use policy completed

---

## References

1. WHO, "Global Tuberculosis Report 2025," 2025. Available: https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025
2. MINSA, "La tuberculosis es curable: detección temprana y tratamiento completo son la clave," 2024. Available: https://www.gob.pe/institucion/minsa/noticias/1189372-la-tuberculosis-es-curable-deteccion-temprana-y-tratamiento-completo-son-la-clave

---

**Last updated:** 4 August 2026