# GitHub → Zenodo publishing guide

1. Keep the repository public.
2. Replace all `REPLACE_WITH_...` fields in `metadata/CITATION.cff.template`.
3. Rename the completed citation template to `CITATION.cff` at repository root before the release.
4. Fill `metadata/zenodo.json.template` with real author names/ORCIDs and the repository URL.
5. If using Zenodo metadata automation, rename the completed file to `.zenodo.json` before release.
6. Confirm no raw social-media text is committed.
7. Create Git tag/release `v1.0.0`.
8. Connect the GitHub repository to Zenodo and archive the release.
9. Copy the Zenodo DOI into:
   - `CITATION.cff`
   - `DATA_AVAILABILITY_PEERJ.md`
   - the PeerJ manuscript Data Availability statement

Repository URL:
https://github.com/komalbashir-sketch/stress-generalization

Recommended topics:
`nlp`, `machine-learning`, `domain-generalization`, `stress-detection`, `roberta`, `naive-bayes`, `reproducibility`, `peerj`
