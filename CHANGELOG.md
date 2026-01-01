# Changelog

All notable changes to Obsidian Scribe will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-01-01

### Added
- **14 New Skills** - Expanded from 21 to 35 skills:
  - **Link Analysis**: `vault-path`, `vault-strength`, `vault-common`, `vault-bidirectional`
  - **Structure Analysis**: `vault-section`, `vault-find-sections`
  - **Frontmatter Intelligence**: `vault-schema`, `vault-schema-check`, `vault-field-values`
  - **Task Management**: `vault-tasks`, `vault-due`
  - **Activity Tracking**: `vault-activity`, `vault-concurrent`
- **2 New Agents** - Expanded from 6 to 8 intelligent agents:
  - **Schema Enforcer Agent** - Audits vault frontmatter schema, detects inconsistencies (e.g., `tags: "work"` vs `tags: ["work"]`), and applies fixes with user confirmation
  - **Relationship Explorer Agent** - Deep relationship analysis between notes using connection strength, link paths, common neighbors, and bidirectional link checks (READ-ONLY)

### Changed
- **README.md** - Major documentation update:
  - Skills section reorganized into 9 categories with clear "Changes Files?" column
  - New "Intelligent Agents" section with natural language workflow examples
  - Updated comparison table to show 35 skills and 8 agents
  - Emphasized read-only vs write behavior for each feature
  - Added conversation examples showing agent workflows
- **Skills Reference** - Updated to reflect 35 skills

### Technical
- Version bumped to 1.3.0 in plugin.json

---

## [1.2.0] - 2026-01-01

### Added
- **Example Rules** (`docs/example-rules/`) - Ready-to-use Claude Code rule templates:
  - `achievements.md` - Achievement log format with timestamps
  - `daily-notes.md` - Daily note structure for rollup chain
  - `obsidian-syntax.md` - Critical Obsidian markdown rules
  - `platform-requirements.md` - WSL/Windows setup requirements
  - `README.md` - Documentation hub for example rules
- **Graph-First Workflow Guide** (`WORKFLOW.md`) - Complete documentation for the graph-first mental model
- **CLAUDE.md Example** (`CLAUDE.md.example`) - Full template for configuring Claude Code in your vault
- **Graph-First README Section** - New section explaining the three-layer architecture
- **RAG Comparison** - "Why Not RAG?" section positioning graph-first vs chunk-based retrieval
- **REPL Advantage Documentation** - Highlighting Claude Code's interactive conversation loop
- **Target Audience Section** - "Who is this for?" targeting Obsidian, Claude Code, RAG, and MCP users
- **Categorized Skills** - Skills now organized into Core Workflows (5), Vault Health (16), and Periodic Rollups (4)
- **Comparison Page** (`docs/comparison.md`) - Feature comparison vs Copilot, Smart Connections, and RAG
- **Skills Reference** (`docs/skills-reference.md`) - Consolidated documentation for all 21 skills
- **Workflows Guide** (`docs/workflows.md`) - Real-world workflow examples

### Changed
- **README.md** - Complete rewrite emphasizing:
  - smoking-mirror MCP as **required** core dependency (not optional)
  - Graph-first navigation vs file-centric approaches
  - RAG alternative positioning with REPL advantages
  - Hyperlinked key concepts (Obsidian, Claude Code, RAG, PKM, MCP)
  - smoking-mirror badge and promotion
- **Documentation Structure** - Simplified from 13+ files to focused hub with key pages
- **Installation Instructions** - Now uses GitHub source (`repo: "bencassie/obsidian-scribe"`) instead of directory source
- **Skill Count** - Updated to reflect 21 skills (was showing 22)
- **Dependencies** - smoking-mirror MCP now listed as Required, not Optional

### Fixed
- **wikilink-suggest.py Hook** - Added exclusions for:
  - `CLAUDE.md` files (case-insensitive)
  - `docs/` directory (repo documentation)
  - `documentation/` directory
  - Root-level files: `README.md`, `CONTRIBUTING.md`, `LICENSE.md`, `CHANGELOG.md`
- **Wikilinks in Docs** - Removed erroneous `[[wikilinks]]` from all documentation files

### Technical
- Version bumped to 1.2.0 in all 3 manifest files:
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
