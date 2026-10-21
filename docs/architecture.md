# Architecture: five layers, repository map, execution path and compatibility

## Five layers

1. **Core IEEE paper-production engine** — `core/SKILL.md`, `core/workflows/`, and
   `core/policies/` are the single maintained instruction layer. Writing guidance,
   research reasoning, citation rules, and reviewer-response procedures live here.
2. **Venue profiles and LaTeX templates** — `venues/<id>/profile.json` identifies
   the actual entry file, document class/options, required front matter, and
   normalization rules. Official files live in `venues/<id>/template/`.
3. **Optional domain packs** — `domains/power-electronics/` contains curated
   knowledge, terminology, and literature-maintenance guidance. Generic papers
   work without a domain pack. The existing library remains in `PE_IEEE_reference/`.
4. **Planning/artifact templates** — `artifacts/` contains idea briefs, paper plans,
   evidence matrices, figure/table plans, and citation-audit/verification records.
5. **Tools and validation** — `scripts/` initializes manuscripts, indexes references,
   audits citations and venue structure, and builds portable releases; `tests/`
   guards these contracts with standard-library Python tests.

```text
AIPE-IEEE-Paper-Agent/
├── AGENTS.md
├── core/
│   ├── SKILL.md
│   ├── policies/
│   ├── workflows/
│   └── agents/openai.yaml
├── venues/
│   ├── ieee-conference/{profile.json,template/}
│   ├── ieee-transactions/{profile.json,template/}
│   ├── ieee-access/{profile.json,template/}
│   ├── ieee-ojpel/{profile.json,template/}
│   ├── ieee-tai/{profile.json,template/}
│   ├── ieee-ojcsys/{profile.json,template/}
│   └── archive/
├── domains/power-electronics/{knowledge/,terminology/,literature/}
├── PE_IEEE_reference/
├── artifacts/
├── scripts/
├── tests/
└── dist/                         # generated, ignored by Git
```

## Execution path

The execution path is: research idea → Problem/Gap/Idea/Evidence/Impact spine →
research questions → 2–4 verifiable contribution claims → evidence and figure/table
plan → paper plan → venue profile → real template initialization → optional domain
knowledge → evidence-based drafting → citation verification → LaTeX/venue audit →
publication-readiness review.

Each important question maps to an experiment, figure, table, derivation, theorem,
simulation, or other evidence. Missing evidence is blocking, important, or optional.
Draft Method → Experiment setup → Results → Introduction → Related Work → Abstract
→ Conclusion where appropriate. Never invent results or reference metadata.
Detailed writing and revision guidance remains in the canonical core workflows.

## Migration and compatibility

- The two editable workflow/reference trees were consolidated into `core/`.
  Source skill installation is replaced by repository mode or generated packages.
- Official venue templates moved into `venues/<id>/template/`; older conference
  and supplementary IEEEtran variants are retained under `venues/archive/`.
- Curated power-electronics content moved into the optional domain pack; planning
  templates moved into `artifacts/`. Original scientific content is preserved.
- `scripts/` command locations and `PE_IEEE_reference/` are unchanged.
- Manuscript initialization now takes `--venue`; the old `--template` switch exits
  with migration guidance instead of silently generating the wrong venue.
- `--no-clean` remains accepted by the packager; only its named generated package
  trees are replaced, and unrelated files under the output root are preserved.

Semantic/RAG literature search, web synchronization of venue rules, automatic
experimental results, advanced paper scoring, and multi-agent orchestration are
outside this architecture consolidation.

## AIPE ecosystem

The [capability manifest](../aipe.yaml) and the [Core evidence mapping](aipe-integration.md)
make this research agent discoverable without changing the paper-production engine or
venue templates.
