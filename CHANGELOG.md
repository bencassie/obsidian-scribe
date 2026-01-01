# Changelog

All notable changes to Obsidian Scribe will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.17] - 2026-01-01

### Added
- **Graph-First Workflow Guide** (`WORKFLOW.md`) - Complete documentation for the graph-first mental model
- **CLAUDE.md Example** (`CLAUDE.md.example`) - Full template for configuring Claude Code in your vault
- **Graph-First README Section** - New section explaining the three-layer architecture
- **Categorized Skills** - Skills now organized into Core Workflows (5), Vault Health (16), and Periodic Rollups (4)
- **Comparison Page** (`docs/comparison.md`) - Feature comparison vs Copilot and Smart Connections
- **Skills Reference** (`docs/skills-reference.md`) - Consolidated documentation for all 21 skills
- **Workflows Guide** (`docs/workflows.md`) - Real-world workflow examples

### Changed
- **README.md** - Complete rewrite with clearer value proposition and scannable structure
- **Documentation Structure** - Simplified from 13+ files to focused hub with key pages
- **Installation Instructions** - Now uses GitHub source (`repo: "bencassie/obsidian-scribe"`) instead of directory source
- **Skill Count** - Updated to reflect 21 skills (was showing 22)

### Fixed
- **wikilink-suggest.py Hook** - Added exclusions for:
  - `CLAUDE.md` files (case-insensitive)
  - `docs/` directory (repo documentation)
  - `documentation/` directory
  - Root-level files: `README.md`, `CONTRIBUTING.md`, `LICENSE.md`, `CHANGELOG.md`
- **Wikilinks in Docs** - Removed erroneous `[[wikilinks]]` from all documentation files

### Technical
- Version bumped in all 3 manifest files:
  - `.claude-plugin/marketplace.json`
  - `plugins/obsidian-scribe/.claude-plugin/marketplace.json`
  - `plugins/obsidian-scribe/.claude-plugin/plugin.json`

---

## [1.0.13] - 2024-12-XX

### Changed
- Version bump with documentation updates

---

## [1.0.12] - 2024-12-XX

### Fixed
- Missing hooks field in plugin.json

---

## [1.0.11] - 2024-12-XX

### Fixed
- Duplicate hooks loading error

---

## Earlier Versions

See [commit history](https://github.com/bencassie/obsidian-scribe/commits/main) for changes prior to v1.0.11.
