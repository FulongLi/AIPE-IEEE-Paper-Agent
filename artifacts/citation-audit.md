# Citation Audit

Run `scripts/check-citations.py <workspace> --write-audit` after adding citations.
The generated audit reports resolved keys, missing entries, duplicate keys, and
uncited entries. It does not verify DOI/URL records or whether sources support claims.
Keep manual verification findings in `notes/citation-verification.md` so rerunning
the structural checker does not overwrite them.
