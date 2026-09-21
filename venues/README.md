# Venue Profiles and Official LaTeX Templates

Each supported venue has `venues/<id>/profile.json` and `template/`. Profiles use
standard JSON so all tools run on Python 3.10+ without third-party dependencies.
They describe the bundled templates; they are not automatically synchronized with
publisher submission rules.

| ID | Class and options | Real entry file |
| --- | --- | --- |
| ieee-conference | IEEEtran [conference] | IEEE-conference-template-062824.tex |
| ieee-transactions | IEEEtran [lettersize,journal] | bare_jrnl_new_sample4.tex |
| ieee-access | ieeeaccess | access.tex |
| ieee-ojpel | ieeeojpel | ojpel.tex |
| ieee-tai | IEEEtai [journal] | TAI_template.tex |
| ieee-ojcsys | IEEEojcsys | OJCSYS_template.tex |

Profiles record the schema version, ID, family, class/options, template path and
entry, source encoding, bibliography style, column count, abstract/keyword
requirements, and preservation checks. `normalization` declares the exact body
marker, keyword environment, extra placeholder environments, and closing commands.
`checks.required_commands` lists venue-specific front/back matter to retain;
`checks.required_assets` identifies logos and class-internal images that must remain
present even when unused demonstration figures are removed.
Paths use forward slashes relative to the repository or packaged asset root.

The generator reads the real entry, keeps the preamble and front-matter order,
replaces sample metadata with TODOs, and substitutes section inputs for the sample
body. Access keeps its font setup, author/address macros, title spacing, and EOD;
OJPEL keeps its logo, dates, affiliations, and journal color; TAI keeps its impact
statement; OJCSYS keeps its category, editor, and author/affiliation structure.
The TAI source has legacy byte encodings in sample prose; Latin-1 decoding preserves
all source bytes while the normalized manuscript is written as UTF-8.

Official support assets are copied unchanged at their original relative locations
beside `main.tex`, including classes, styles, bibliography files, fonts, and logos.
Missing standard TeX packages and IEEEtran.bst where not bundled are supplied by the
LaTeX distribution (including Overleaf). No class/style file is rewritten.

`venues/archive/` retains the older conference template and supplementary IEEEtran
variants for consultation. They are not additional supported initialization profiles
and are not included in skill release packages. The original templates and guide
PDFs remain available for reference; remove unused sample assets from final papers.
