# Reproducibility notes

## Final source protocol
The source corpus is Dreaddit. The official train and test partitions are retained as the starting point. The training partition is normalized for audit purposes, duplicate normalized-text records are collapsed, and normalized train/test overlaps are removed from training. The official test partition remains unchanged.

## External evaluation protocol
The public Reddit Title, Reddit Combi, Twitter Full, and Twitter NonAdvert files are reconstructed by the notebooks. Exact normalized duplicates are collapsed and conflicting normalized-text groups are removed.

## Transformer protocol
- Checkpoints: `distilbert-base-uncased`, `roberta-base`
- Seeds: 42, 52, 62
- Train/validation split: stratified 90:10 using random state 42
- Epochs: 3
- Learning rate: 2e-5
- Training batch size: 16
- Evaluation batch size: 32
- Weight decay: 0.01
- Maximum sequence length: 256
- Best checkpoint: validation Macro-F1

## Classical protocol
Training-only 3-fold stratified cross-validation is used on the leakage-clean Dreaddit training partition. Macro-F1 is the selection criterion. The exact selected parameters are generated during the canonical run and should be archived with the repository results.

## Statistical protocol
The final MNB vs RoBERTa comparison uses paired 2,000-sample non-parametric bootstrap confidence intervals and McNemar tests for each of the five datasets and three RoBERTa seeds. Holm correction is applied across all 15 McNemar comparisons.

## Historical note
During manuscript revision, an intermediate MNB result stream was found to differ slightly from the leakage-clean training-only selection protocol. `06b_stageA2_canonical_mnb_reconciliation.ipynb` and `08_finalize_canonical_results.ipynb` explicitly reconcile this and define the final values reported in the paper.
