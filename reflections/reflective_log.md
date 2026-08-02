# Project Reflective Log

## Entry 1 — Paradigm, Method, and Literature

### What

The original purpose of the project was to develop software capable of using video to monitor whether tuberculosis (TB) medication is taken. During the presentation, the professor asked me why the project followed a positivist paradigm rather than another paradigm. This question made me realize that I needed to explain more clearly the relationship between the selected paradigm and the way I will evaluate the system.

I also compared three methodological alternatives: classical computer vision with OpenCV, transfer learning, and the construction of a custom dataset to train deep learning models. The literature review showed that few studies focus specifically on TB medication. I also did not find studies that integrate medication detection and intake verification within the same system.

### So what

I understood that the positivist paradigm is appropriate because the main part of the project will be evaluated through observable results and computer vision metrics. These metrics include precision, recall, F1-score, and confusion matrices. However, it is not enough to state that the project is positivist because it uses metrics. I must clearly justify why this paradigm addresses the research question.

I also understood that there is an important ethical limitation. The system is intended to be useful for people with active TB, but at this stage I cannot work directly with this population. Approaching and recording people with active TB requires conditions, authorizations, and protective measures that I do not yet have. Therefore, the initial validation will be conducted with people who do not have active TB but take medication daily for other conditions.

The comparison of methods confirmed that the best option for the final solution is to build a custom dataset. A general-purpose dataset can be used to test the concept, but it does not guarantee that the system will work with the anti-tuberculosis medications used in a real setting.

### Now what

I decided to keep the original research question. The pill-detection proof of concept is only a first stage and does not replace the overall objective. Later, it will be necessary to build a dataset containing images of specific TB medications and develop the video component to evaluate medication intake.

In addition to technical metrics, the project will include a quantitative evaluation of usability and acceptability. This evaluation will initially involve people who take medication daily but do not have active TB. It remains necessary to define how a future validation with the actual clinical population will be conducted and which authorizations will be required.

## Entry 2 — Reproducibility

### What

To develop the first proof of concept, I reviewed different pill datasets. I initially considered Pillbox, but I discovered that it had been discontinued and did not find a clear explanation for this decision. As an alternative, I used MEDISEG, which is a valuable dataset for testing the idea, although it does not contain medications specific to TB.

One of the most difficult parts was correctly configuring the model characteristics and organizing the required libraries. Without AI support, this stage would have been much more complex. Codex also helped organize the presentation of the metrics to highlight the most important results. The decisions regarding the experiment and the review of its results remained under my supervision.

The Zero-PIMA audit also allowed me to examine the information required to reproduce published research. I found that many studies do not share their code and, when they do, they do not always adequately describe the parameters used.

### So what

This exercise changed the way I understand reproducibility. Previously, I might have thought that publishing code was sufficient. I now understand that library versions, training parameters, random seeds, data splits, and instructions for running the experiment must also be recorded.

The disappearance of Pillbox revealed an additional risk: depending entirely on external datasets can affect the continuity of the project. A dataset or link may become unavailable. If information about its source, version, and structure is not preserved, repeating the experiment may become impossible.

I also understood that a study should not be described as reproducible simply because the code works once. Another person must be able to follow the instructions and obtain equivalent results without relying on information known only to the author.

### Now what

Based on this experience, I decided to preserve the data provenance, software versions, file hashes, and execution instructions. The random seeds and data splits used in each experiment must also be recorded.

MEDISEG will remain a proof of concept, but the final project will require a custom dataset containing anti-tuberculosis medications. This decision will make it possible to work with information that is more closely aligned with the system's objective and will reduce dependence on a single external source.

## Entry 3 — Ethics, Data, Bias, and Integrity

### What

At the beginning, I had not sufficiently considered that the videos used in the project contain information that may affect people's identity and privacy. Although the objective is to observe medication intake, a recording may include the face or other elements that are unnecessary for the analysis.

The exercise on algorithmic bias also led me to examine the composition of the datasets. Many available datasets primarily contain records of White or Caucasian people. This may produce a system that does not perform in the same way for other racial and ethnic groups.

The course policy on AI use led me to review how I am using these tools. In this log, I am using my own words, and Codex is used to organize the ideas and improve the grammar.

### So what

I understood that, when working with human beings, I must consider their rights and integrity, not only the technical usefulness of the videos. The identity of participants must be protected even when they do not belong to a population with active TB.

I also understood that dataset diversity is part of the validity of the system. If the videos do not include sufficient racial and ethnic diversity, the results may represent only part of the population. Therefore, participants cannot be selected without considering this issue.

Regarding the use of AI, my limit is that Codex can help me improve and organize my work, but it must not produce work that I have not reviewed and supervised. The methodological decisions and responsibility for the content remain mine.

### Now what

To protect privacy, the framing will be limited to the hands, the medication, and the lower part of the face needed to observe the action. If the full face is accidentally recorded, that section must be removed or cropped according to the approved protocol.

I will also seek a population with greater racial and ethnic diversity for the future collection of videos. This decision must be reflected in the recruitment procedure and in the final description of the dataset.

All content developed with AI support will be reviewed before being incorporated into the project. The tool may support organization, correction, and some technical tasks, but it does not replace my responsibility as a researcher.

## Entry 4 — Writing and Protocol Development

### What

The professor's main observation was that I needed to describe the work in greater detail. It was necessary to explain the data, procedures, and criteria more clearly to demonstrate that the project follows appropriate guidelines and can be reproduced.

During the development of the repository, it was also necessary to clarify the relationship between MEDISEG and the original question. The proof of concept only demonstrates that a pill-detection process can be executed. It does not answer the general question concerning TB medication and intake verification.

When comparing protocol v0.1 with v1.0, I identified several changes. Version v1.0 describes the ethical aspects more clearly, including facial privacy. It also places greater emphasis on reproducibility and explains the inclusion and exclusion criteria in more detail.

### So what

I understood that methodological detail is not merely a presentation requirement. If the data, criteria, and procedures are not clearly explained, another person cannot adequately evaluate or reproduce the study.

I also reaffirmed that a proof of concept must not be presented as the final solution. MEDISEG is useful for confirming that the pipeline works, but it does not contain TB medications or medication-intake videos. Its results must therefore be interpreted within this limitation.

The development of the protocol showed that ethical and reproducibility considerations must be present from the planning stage. Describing the model is not sufficient. The conditions of participation, privacy, data management, and the limitations of the results must also be explained.

### Now what

For version v2.0, the usability and acceptability questionnaire must be validated, or previously validated instruments suitable for the study must be identified. It will also be necessary to specify the recruitment method and explain how eligible participants will be identified and contacted.

Peer review will be incorporated when it actually takes place. The observations received must be recorded and linked to the changes made in the next version of the protocol.

## Synthesis

The most important lesson from the course is that science must be reproducible to be reliable. A result should not depend solely on whether the original researcher can run the code. The data, parameters, versions, decisions, and procedures must be documented so that other people can review and repeat the work.

At the beginning, I viewed the project mainly as a software development problem. The objective seemed to focus on building a system capable of detecting medications and recognizing an intake action. I now see it as an integrated problem. The system will work with human beings, so I must consider their rights, identity, privacy, and possible differences in performance between groups.

The research question did not change, but my understanding of what is required to answer it did. The proof of concept using MEDISEG demonstrates only an initial technical capability. Moving forward will require building a TB-specific dataset, developing the video component, and documenting each stage in a reproducible manner.

The next steps are to complete the protocol, validate or select the questionnaires, and specify the recruitment procedure. The protocol must then be submitted to a Research Ethics Committee. Only after the corresponding approval is obtained will it be possible to recruit people who meet the defined conditions and provide informed consent.

This sequence is part of scientific work. Ethical review and consent are not activities separate from technical development. They are necessary conditions for the project to move forward responsibly.

## AI Use Declaration

Codex was used to organize notes provided by the author, translate the text into English, and support grammar correction. The reflective experiences, decisions, and conclusions were provided and supervised by the author.
