# AIPE research capability integration

`aipe.yaml` registers AIPE IEEE Paper Agent as an **agent**, consuming research
questions and traceable evidence and producing manuscript plans, venue workspaces
and review reports. AIPE means AI for Power Engineering; this paper engine remains
usable for other research domains through its existing optional domain packs.

Core Engineering State fields map semantically as follows. No runtime conversion
or new manuscript generator is claimed in this release.

| Engineering State | Paper workflow |
| --- | --- |
| `project`, `requirements`, `architecture` | Scope, research questions, design intent |
| `simulation.runs` | Reproducibility methods, tool/version and input records |
| `validation.checks` | Evidence supporting or contradicting a specific claim |
| `evidence` | Source identifiers, provenance, artifacts and review status |
| Unreviewed assumptions | Explicit hypotheses/limitations; never measured results |

Preserve evidence IDs when mapping into the evidence matrix. A schema-valid
Engineering State does not demonstrate an engineering claim. Computed, simulated
and measured results remain distinct. Missing measurements remain missing; the
paper agent must not invent citations, experiments, efficiency or device results.

The open path uses Python's standard library for initialization, indexing and
static audits, and an optional open TeX distribution for compilation. Existing
venue-specific templates and policies remain canonical. Third-party templates,
papers and local-only books retain their rights. No repository-wide software
licence is asserted because the repository currently lacks one; the manifest
reports `NOASSERTION` rather than granting rights to its reference collection.

The AIPE Design Agent can discover this capability through Registry metadata and
request a reviewed hand-off containing the research question, evidence IDs and
chosen venue. Publication or submission is outside automatic orchestration.

Validation: existing architecture tests cover all six supported venues, portable
template initialization, reference index and release generation. Static validation
does not replace PDF inspection or external citation verification.
