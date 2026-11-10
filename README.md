# Beyond In-Domain Performance: Cross-Dataset and Cross-Platform Generalization of Social Media Stress Classifiers

Reproducibility repository for the manuscript submitted to **PeerJ Computer Science**.

## Study purpose

This repository supports an empirical study of whether model rankings established on a source dataset remain stable under external cross-dataset and cross-platform transfer. Six source-trained classifiers are evaluated:

- Logistic Regression
- Multinomial Naive Bayes
- Linear SVM
- Random Forest
- DistilBERT
- RoBERTa-base

The source corpus is Dreaddit. External evaluation uses Reddit Title, Reddit Combi, Twitter Full, and Twitter NonAdvert. No target-domain retraining, target-domain hyperparameter tuning, checkpoint selection, or threshold optimization is used for the primary transfer results.

## Canonical workflow

The public workflow contains only the six notebooks that define the final audited/canonical manuscript pipeline:

1. `notebooks/05_statistical_robustness_persistent_v3.ipynb`
2. `notebooks/06_reviewer_revision_stageA.ipynb`
3. `notebooks/06b_stageA2_canonical_mnb_reconciliation.ipynb`
4. `notebooks/07_reviewer_revision_stageB_all_models_diagnostics.ipynb`
5. `notebooks/07b_stageB_final_audit.ipynb`
6. `notebooks/08_finalize_canonical_results.ipynb`

Earlier Phase 1–4 notebooks and superseded Phase 5 variants were development history and are intentionally excluded from the canonical public workflow. See `EXCLUDED_LEGACY_FILES.md`.

## Canonical checks

A correct reconstruction should produce:

| Dataset | Final evaluation size |
|---|---:|
| Dreaddit leakage-clean training set | 2,817 |
| Dreaddit official test set | 715 |
| Reddit Title | 5,503 |
| Reddit Combi | 3,123 |
| Twitter Full | 8,415 |
| Twitter NonAdvert | 1,967 |

Headline Macro-F1 values reported in the manuscript are stored as verification targets in `verification/expected_macro_f1.csv`.

## Environment

The original experiments were run in Google Colab, with a T4 GPU used for transformer training.

Core transformer settings:
- checkpoints: `distilbert-base-uncased`, `roberta-base`
- seeds: 42, 52, 62
- train/validation split: stratified 90:10, random state 42
- epochs: 3
- learning rate: 2e-5
- training batch size: 16
- evaluation batch size: 32
- weight decay: 0.01
- maximum sequence length: 256
- best checkpoint selected by validation Macro-F1

The exact historical package-version snapshot was not preserved in the deleted Drive outputs, so `requirements.txt` lists the packages required by the recovered canonical notebooks without claiming exact historical version pinning.

## Data

Raw social-media datasets are **not redistributed** in this repository.

The notebooks retrieve source datasets from the public sources cited in the manuscript. The Reddit Combi discrepancy is documented because the publication reports 3,604 records while the public file used in the study contains 3,123 records.

## Privacy and prediction files

Some working notebooks originally write prediction CSVs containing a `text` column. Do **not** publish those files unchanged.

Use:

```bash
python scripts/sanitize_predictions.py INPUT OUTPUT
```

The sanitizer replaces raw text with the same normalized SHA-256 text hash used in the audit and removes the raw text column.

## Canonical result reconciliation

During manuscript revision, an intermediate MNB result stream was found to differ slightly from the leakage-clean, training-only model-selection protocol.

The final manuscript values are defined by:
- `notebooks/06b_stageA2_canonical_mnb_reconciliation.ipynb`
- `notebooks/08_finalize_canonical_results.ipynb`

The finalization notebook replaces stale intermediate MNB rows with the canonical MNB results before producing the manuscript tables.

## Repository structure

- `notebooks/` — six canonical analysis notebooks
- `verification/` — manuscript-verified reference values
- `scripts/` — utility scripts, including prediction sanitization
- `data/` — data-source and redistribution notes
- `results/` — guidance for canonical generated outputs
- `metadata/` — citation/Zenodo metadata templates

## Release workflow

1. Add sanitized generated result files if available.
2. Fill in the author metadata templates in `metadata/`.
3. Create a GitHub release, recommended tag: `v1.0.0`.
4. Archive that release in Zenodo.
5. Obtain the Zenodo DOI.
6. Replace `[ZENODO DOI]` in `DATA_AVAILABILITY_PEERJ.md`.
7. Copy the final statement into the PeerJ manuscript.

## Verification files

Files under `verification/` are **reference targets transcribed from the finalized manuscript/previously verified outputs**. They are not substitutes for generated notebook outputs. They are provided so a release run can be checked quickly for agreement with the paper.

## License

Repository code and original documentation are released under the MIT License. Third-party datasets and pretrained model weights remain subject to their original licenses and terms.
