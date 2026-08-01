# Reproducibility Audit: Zero-PIMA

## 6.1. Paper Identification

**Paper:** Nguyen, T. T., Nguyen, P. L., Kawanishi, Y., Komamizu, T., & Ide, I. (2024). *Zero-Shot Pill-Prescription Matching With Graph Convolutional Network and Contrastive Learning*. IEEE Access, 12, 55889-55904. https://doi.org/10.1109/ACCESS.2024.3390153

- **Project page:** https://zero-pima.github.io/
- **Official code:** https://github.com/thanhhff/Zero-PIMA
- **Audited code snapshot:** commit [`debe0c1ece16f8e90fc021de2dc7bf327b585286`](https://github.com/thanhhff/Zero-PIMA/tree/debe0c1ece16f8e90fc021de2dc7bf327b585286)
**Audit date:** August 1, 2026

Zero-PIMA was selected because it is directly related to this project's pill-detection component and provides more public reproducibility material than the other studies in the systematic review. It addresses pill-prescription matching under a zero-shot setting using a pill detector, a graph convolutional network for prescription structure, and contrastive learning for image-text alignment.

## 6.2. Audit Scope and Verification Status

This is a documentation and static-code audit of the published paper, project page, dataset link, and official repository. The repository was cloned successfully and all 12 Python files passed syntax parsing. A full training rerun was not attempted because the reviewed materials do not provide a self-contained, versioned route to the exact VAIPE-PP dataset split, software environment, pretrained checkpoint, and published expected outputs.

**Verification status: ANALYZED, NOT REPRODUCED.** The score below measures whether an independent researcher could reproduce the published results from the public materials; it does not assess the novelty or clinical value of the method.

## 6.3. Reproducibility Checklist

| Criterion | Evidence found | Assessment |
|---|---|---|
| Paper and method access | The article is open access and has a DOI. The project page explains the architecture, dataset size, and main task. | **Good** |
| Public code | An official GitHub repository contains training code, model modules, evaluation utilities, shell commands, and configuration files. | **Good, but incomplete** |
| Code versioning | Git history exists, but the repository has no tagged release corresponding to the article and no archived DOI for the code. This audit therefore pins the latest reviewed commit explicitly. | **Partial** |
| Dataset access | The project page states that VAIPE-PP contains 2,156 multi-pill photos matched to 1,527 prescriptions across four templates, collected in Vietnam during 2021-2022. The data link leads to a general resource site rather than an immutable release of the exact experimental dataset. No checksum or DVC-style version is supplied. | **Weak** |
| Data splits | The code expects pre-existing `pres/train/`, `pres/test/`, `pills/train/`, and `pills/test/` directories. Seen and unseen pill labels are partly encoded in `config.py`, but the repository does not provide the script, manifest, or random procedure that generated the exact published split. | **Partial** |
| Leakage controls | Train and test folders are read separately. However, the absence of a split-generation manifest prevents independent verification that prescriptions, patients, or near-duplicate images do not cross partitions. | **Unverifiable** |
| Random seeds | A command-line seed with default value 42 is declared, but the entry point only calls `torch.cuda.manual_seed`. It does not set Python `random`, NumPy, CPU PyTorch, `PYTHONHASHSEED`, DataLoader worker seeds, or deterministic CUDA behavior. | **Weak** |
| Hyperparameters | Epochs, learning rate, batch sizes, number of workers, text encoder, embedding dimensions, dropout, optimizer, and weight decay can be recovered from the argument parser, training code, and shell scripts. | **Moderate** |
| Environment | The README supplies Conda installation commands and specifies CUDA 11.6. Package versions, Python version, operating system, and a lock file or container are absent. Reproduction also requires manually replacing the installed TorchVision `roi_heads.py`, which is version-sensitive. | **Weak** |
| Pretrained weights and checkpoints | The repository initializes public pretrained backbones, but it does not publish the final Zero-PIMA checkpoint tied to the paper's tables. | **Missing** |
| Evaluation metrics | The code evaluates COCO-style average precision and separates seen and unseen cases. The paper/project materials report point estimates and ablations. | **Moderate** |
| Multiple runs and seed variability | No multi-seed protocol, mean plus standard deviation, or run-level results sufficient to estimate training variability were found in the reviewed materials. | **Missing** |
| Statistical tests | No hypothesis test supporting superiority claims was found in the public reproducibility materials. | **Missing** |
| Confidence intervals | No confidence intervals or bootstrap uncertainty estimates were found for the reported performance differences. | **Missing** |
| Compute reporting | The authors state that computation used the Nagoya University supercomputer **Flow**, but do not identify the exact node, GPU model/count, CPU, memory, runtime, or energy cost required for the reported experiments. | **Weak** |
| Exact run instructions | Several shell scripts reveal internal commands and paths, but the README does not give a complete download-to-result workflow or a numeric expected output for verification. Some paths are machine-specific, such as `/workdir/data/...`. | **Weak** |

## 6.4. Seed Audit

The presence of `--seed 42` may initially suggest that randomness is controlled. The implementation is only partial:

```python
parser.add_argument('--seed', type=int, default=42)
...
torch.cuda.manual_seed(parse_args.seed)
```

This does not guarantee repeatability. The data loader shuffles the training set, the detector samples proposals, and the model includes dropout. A stronger implementation would set all relevant random number generators, seed DataLoader workers, and document deterministic-algorithm settings and their limitations. The paper should then report results over several independent seeds as mean plus standard deviation rather than relying on a single run.

## 6.5. Split and Leakage Audit

The published task requires special attention to the seen/unseen split. The repository contains a hard-coded `UNSEEN_LABELS` dictionary and reads already-separated train and test folders. This helps explain which pill identities are treated as unseen, but it does not reconstruct the complete partition.

For a reliable audit, the release should include:

1. a manifest listing every prescription and multi-pill image in each split;
2. the rule and seed used to generate the split;
3. grouping by anonymous patient or prescription source to prevent correlated samples from appearing in both sets;
4. a duplicate or near-duplicate image check; and
5. separate documentation for model-selection validation data and final test data.

Without those artifacts, the reported seen and unseen metrics cannot be independently checked for partition leakage.

## 6.6. Statistical Rigor

The main quantitative evidence is based on point estimates of average precision and ablation comparisons. Point estimates are useful for benchmarking but do not show how much results change across random initialization, data order, or sampling variation.

The minimum stronger reporting package would be:

- at least five independent training seeds for the main model and principal baselines;
- mean, standard deviation, and individual run values;
- a 95% confidence interval, preferably using a patient- or prescription-level bootstrap that respects grouping;
- a paired comparison on the same resamples or test units when claiming improvement over a baseline; and
- correction or explicit caution when interpreting many ablation comparisons.

Because these elements were not found, the audit cannot determine whether small differences between methods exceed experimental variability.

## 6.7. Overall Reproducibility Score

| Dimension | Maximum | Score | Justification |
|---|---:|---:|---|
| Paper identification and access | 10 | 8 | Open article, DOI, and informative project page |
| Code availability and versioning | 10 | 7 | Official source code exists, but no article-specific release or archive |
| Data availability and documentation | 10 | 5 | Dataset is described, but the exact immutable experimental package is not supplied |
| Split reconstruction and leakage control | 10 | 6 | Train/test structure and unseen labels are visible, but the split manifest and generation procedure are absent |
| Seeds and deterministic execution | 10 | 3 | Only the CUDA seed is set |
| Environment and dependencies | 10 | 3 | CUDA version is mentioned, but dependencies are unpinned and a library file must be replaced manually |
| Training configuration and checkpoints | 10 | 5 | Many hyperparameters are recoverable, but final checkpoints are absent |
| Evaluation and statistical rigor | 10 | 2 | Point metrics exist; multi-seed variability, statistical tests, and confidence intervals are absent |
| Compute reporting | 10 | 2 | Supercomputer is named, but exact hardware and runtime are not reported |
| End-to-end instructions and expected outputs | 10 | 2 | Internal shell commands exist, but there is no complete verified reproduction path |
| **Total** | **100** | **43** | **Low reproducibility from the public materials** |

**Overall verdict:** Zero-PIMA is more reusable than a paper with neither data nor code, and its repository is valuable for understanding the proposed implementation. Nevertheless, the current public package does not pass the course's "stranger test." A researcher cannot yet move from a clean machine to the exact published tables without resolving undocumented dataset, split, environment, checkpoint, and compute details.

## 6.8. Priority Improvements

The five changes with the greatest impact would be:

1. archive the exact code revision, dataset, annotations, and split manifests with persistent identifiers and checksums;
2. publish a pinned Conda environment or `requirements.txt` plus a Docker image or Dockerfile;
3. replace the manual TorchVision source-file modification with a versioned patch or repository-local implementation;
4. provide pretrained checkpoints and a one-command evaluation script with expected metrics; and
5. rerun the main comparisons across multiple seeds and report uncertainty and paired statistical comparisons.

## 6.9. Relevance to AI-DOTS

Zero-PIMA supports the feasibility of matching pill images with medication names, including pills excluded from training. This is relevant to the pill-identification component of AI-DOTS, but it does **not** validate pill ingestion, tuberculosis adherence, or deployment in Peru. Its reproducibility weaknesses also reinforce the design decisions for this project: preserve immutable dataset manifests, document patient-independent splits, fix all random seeds, pin the environment, retain checkpoints, and report variability rather than a single best result.

## 6.10. Sources Reviewed

- Nguyen et al. (2024), IEEE Access: https://doi.org/10.1109/ACCESS.2024.3390153
- Official Zero-PIMA project page: https://zero-pima.github.io/
- Official repository snapshot: https://github.com/thanhhff/Zero-PIMA/tree/debe0c1ece16f8e90fc021de2dc7bf327b585286
- VinUni-Illinois Smart Health Center resources: https://smarthealth.vinuni.edu.vn/resources/
