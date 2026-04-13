# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **cardiac surgery clinical guidelines reference library** — not a software project. It contains PDF guideline documents from major international societies and authored comparative analysis documents synthesizing recommendations across guidelines.

The primary language for authored content is **Japanese**, though source PDFs include both English and Japanese documents.

## Repository Structure

- `reference/` — Source PDF guideline documents organized by region:
  - `reference/Japan/` — JCS (Japanese Circulation Society) and affiliated society guidelines (Japanese + English versions)
  - `reference/Europe/` — ESC, EACTS guidelines and consensus documents
  - `reference/US/` — ACC/AHA, STS, AATS, ISHLT guidelines and consensus documents
- Root directory — Authored comparative analysis documents (`.md` and `.html` pairs)

## File Naming Convention

PDFs follow: `{Society}_{Year}_{Topic}_Guidelines.pdf`
- Japanese guidelines use Japanese topic names (e.g., `JCS_2020_大動脈瘤_大動脈解離_Guidelines.pdf`)
- Some Japanese guidelines have both JP and EN versions

## Comparative Analysis Documents

The authored documents (e.g., `Ascending_Aorta_Surgery_Indications_Guideline_Comparison`) are structured as:
1. **Part I** — Individual guideline summaries with recommendation tables (class/level of evidence)
2. **Part II** — Cross-guideline comparison tables and thematic analysis

These documents cross-reference multiple PDFs from `reference/` and synthesize surgical indications, thresholds (e.g., aortic diameter cutoffs), and classification systems across societies.

## Key Considerations

- When reading or creating comparative analyses, preserve exact recommendation classes (I, IIa, IIb, III) and evidence levels (A, B, C) as stated in the source guidelines — do not paraphrase or reinterpret these.
- Diameter thresholds (mm) and growth rates (mm/year) are critical clinical values — accuracy is paramount.
- Different guidelines use different measurement methodologies (inner-to-inner vs leading-edge-to-leading-edge, CT vs echo) — note these distinctions when comparing.
- Japanese guidelines (JCS) tend to set lower intervention thresholds than ACC/AHA or ESC for certain conditions — this is an intentional difference reflecting different patient populations, not an error.
- The HTML files are rendered versions of the corresponding `.md` files.
