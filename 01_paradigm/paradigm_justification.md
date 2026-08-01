# Paradigm Justification Statement

## 1. Current study and broader context

The broader AI-DOTS research direction investigates whether computer vision could contribute to remote medication verification. For the present course delivery, that broad problem has been reduced to an executable first step: detecting and distinguishing three pharmaceutical pill types in static images from the public MEDISEG dataset.

This distinction is essential. The current study does not include tuberculosis patients, healthy volunteers, swallowing videos, adherence measurement, questionnaires, or clinical outcomes.

## 2. Research question

> To what extent can a pretrained YOLO26n object detector locate and distinguish three pharmaceutical pill types in the held-out MEDISEG test set?

## 3. Chosen paradigm

The study adopts a **quantitative empirical, broadly positivist paradigm**. Its claims are evaluated using observable and reproducible measurements obtained from a fixed test set: precision, recall, mean average precision at IoU 0.50, and mean average precision across IoU thresholds from 0.50 to 0.95.

A questionnaire is not required merely because the study uses a positivist paradigm. Questionnaires are one possible quantitative instrument, but the instrument in this experiment is a computational evaluation protocol applied to labeled images.

## 4. Why other paradigms are not primary here

- **Interpretivism** is not primary because the study does not investigate experiences, meanings, attitudes, or perceptions.
- **Mixed methods** are unnecessary for this technical baseline because no qualitative research question is being combined with the performance evaluation.
- **Design science** remains relevant to the broader development of an AI-DOTS artifact, but this course experiment is narrower: it evaluates one trained detector on a defined benchmark rather than evaluating the utility of a complete sociotechnical system.

## 5. Implications for the research design

The paradigm requires a transparent and repeatable computational procedure:

- a documented public data source;
- auditable annotations and class labels;
- predetermined training, validation, and test partitions;
- fixed software versions, seed, model, and main hyperparameters;
- isolation of the test set until final evaluation;
- reporting of favorable and unfavorable results;
- explicit limits on inference.

## 6. Limits of the evidence

High detection performance in MEDISEG cannot be interpreted as evidence that the system recognizes Peruvian tuberculosis medicines, verifies swallowing, improves adherence, or is clinically ready. Those questions require new target-domain data, human-participant protocols, ethics approval, and external validation. The present result is a technical baseline only.
