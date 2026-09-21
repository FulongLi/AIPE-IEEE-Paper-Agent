# Chapter Notes

This folder is for commit-safe, non-substitutive chapter notes. Use it to make the power electronics knowledge base searchable and useful for IEEE paper writing without reproducing a textbook.

## Recommended Note Types

- One-page chapter overview in original wording
- Key concepts and topic tags
- Equation and model index by topic
- Useful IEEE-style terminology
- Design tradeoffs and experiment vocabulary
- Local source pointers, such as chapter, section, or page number

## Do Not Commit

- Full chapter text
- Long copied passages
- Extracted figures or tables from the textbook
- Page-by-page Markdown conversion
- Notes detailed enough to replace reading the source chapter

## Suggested File Naming

```text
chapter-notes/
├── chapter-index.md
├── ch01-topic-name.md
├── ch02-topic-name.md
└── formula-index.md
```

Start from [chapter-index.md](chapter-index.md) for the current chapter-note map.

## Template

```markdown
# Chapter X: Topic Name

## Retrieval Tags

converter family, control topic, component topic, modeling topic

## Core Ideas

- Original one-sentence idea.
- Original one-sentence idea.
- Original one-sentence idea.

## Useful IEEE Language

- Sentence pattern with placeholders.
- Sentence pattern with placeholders.

## Formula / Model Index

| Topic | What It Is Used For | Local Source Pointer |
| --- | --- | --- |
| Volt-second balance | Deriving steady-state conversion ratio | Chapter/section/page |

## Paper-Writing Use

Use this note when drafting sections about ...

## Local Source Pointers

- Chapter/section/page pointer for verification.
```
