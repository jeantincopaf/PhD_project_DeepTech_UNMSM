# Reproducible MEDISEG Pipeline

This folder contains the executable Google Colab notebook and the archived outputs of the reported YOLO26n experiment.

## Contents

- `MEDISEG_3Pills_YOLO26_Colab.ipynb`: complete download, audit, conversion, training, testing, and packaging workflow.
- `RESULTS.md`: concise interpretation of the final test results and limitations.
- `results/test_metrics.json`: machine-readable overall and per-class test metrics.
- `results/split_manifest.csv`: deterministic assignment of every image.
- `results/dataset_summary.json`: dataset counts and provenance.
- `results/environment.json`: execution environment.
- `results/data.yaml`: class mapping and partition configuration.
- `results/training/`: exact training arguments and epoch history.
- `results/figures/`: training, precision-recall, F1-confidence, and confusion-matrix figures.
- `results/predictions/`: representative test predictions.
- `results/weights/best.pt`: selected checkpoint used for final testing.
- `results/SHA256SUMS.txt`: integrity hashes for the archived artifacts.

## Recommended execution

Run the notebook from top to bottom in a GPU-enabled Colab runtime. The reported experiment used an NVIDIA L4 GPU. Do not inspect or tune against the test set before the final evaluation cell.

The official MEDISEG archive is downloaded at runtime and is not committed to this repository.
