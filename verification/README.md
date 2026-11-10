# Verification targets

These CSV files contain values already verified during manuscript preparation and reported in the finalized paper.

They are **reference targets, not regenerated outputs**. Their purpose is to make it easy to confirm that a clean archival run reproduces the manuscript results.

- `expected_macro_f1.csv`: manuscript six-model Macro-F1 values
- `expected_bootstrap_ci.csv`: per-seed paired bootstrap differences for RoBERTa minus MNB
- `expected_diagnostics.csv`: selected transfer-diagnostic values

Canonical generated outputs are listed in `OUTPUT_MANIFEST.csv`.
