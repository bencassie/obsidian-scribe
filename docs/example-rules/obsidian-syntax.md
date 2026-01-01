---
# This is an EXAMPLE rule file for documentation purposes
# Copy this to your vault's .claude/rules/ directory

# Claude Code scoping
paths: "**/*.md"
alwaysApply: true

# Obsidian metadata (optional - for vault organization)
type: rule
tags:
  - rule
  - obsidian
  - syntax
  - markdown
aliases:
  - Obsidian Syntax Rules
  - Markdown Formatting Rules
date: 2026-01-01
description: Critical syntax rules for Obsidian markdown files (enforced by syntax-validate hook)
---

# Obsidian Markdown Syntax Rules (Example)

> **Note**: This is an example rule file documenting Obsidian markdown syntax issues.
> The **syntax-validate hook** in obsidian-scribe checks for many of these issues automatically.

These rules apply when editing ANY markdown file in the vault.

## Wikilinks

- Use `[[wikilink]]` format for internal links
- Use `[[Page|Display Text]]` for aliased links

### CRITICAL - Never Wrap Wikilinks

NEVER wrap wikilinks with formatting characters:

```markdown
WRONG:
**[[Link]]**
*[[Link]]*
_[[Link]]_
`[[Link]]`

CORRECT:
[[Link]]
**Text with [[Link]] inside**
```

**Why this matters**: Wrapping wikilinks breaks Obsidian's hyperlink functionality. The link becomes unclickable.

**Detected by**: syntax-validate hook ✅

## Angle Brackets

### CRITICAL - No Angle Brackets in Content

NEVER use angle brackets (( )) in Obsidian notes:

```markdown
WRONG:
ILogger<T>
List<string>
Dict<string, int>
<any XML tags>
response.Data<User>

CORRECT:
ILogger(T)
List of string
Dict(string, int)
Use code blocks: `ILogger<T>`
response.Data[User]
```

**Why this matters**: Angle brackets are interpreted as HTML/XML tags by Obsidian and break ALL wikilinks that follow them in the document.

**Example of breakage:**
```
"Using ILogger<T> for logging" + later "[[Some Link]]"
= [[Some Link]] becomes broken/unclickable
```

**Detected by**: syntax-validate hook ✅

### Allowed Uses of Angle Brackets

- Inside fenced code blocks (```)
- Inside inline code (`` `like this` ``)

## YAML Frontmatter

### CRITICAL - No Wikilinks in YAML Frontmatter

NEVER use wikilinks in YAML frontmatter keys or values:

```yaml
WRONG:
---
[[Title]]: "My Note"
title: "[[Some]] [[Text]]"
[[Created]]: 2025-12-30
description: "[[Text]] with [[Links]]"
---

CORRECT:
---
title: "My Note"
created: 2025-12-30
description: "Text with links"
author:
  - "[[@username]]"  # Exception: author references can use [[@]] format
---
```

**Why this matters**:
- Wikilinks in YAML keys break metadata parsing completely
- Wikilinks in YAML values corrupt the metadata and make it unparseable
- The auto-wikilink hook can inadvertently add [[brackets]] to frontmatter
- Only exception: author fields can use `[[@username]]` format for social media references

**Detected by**: syntax-validate hook ✅

### General YAML Rules

- Preserve existing metadata structure
- Don't modify frontmatter unless specifically asked
- Common fields: type, date, tags, aliases, title, created, description, source
- Keys must be lowercase without special characters
- Values should be plain text (no wikilinks except for author references)

## Code Blocks

### CRITICAL - Always Close Code Blocks

ALWAYS ensure fenced code blocks have matching opening and closing backticks:

````markdown
WRONG:
___CODE_BLOCK_5___powershell
some command
___CODE_BLOCK_6___`

**Why this matters**: Unclosed code blocks break markdown rendering and cause everything after them to be treated as code.

### Code Block Rules

- Fenced code blocks use triple backticks: ` ___CODE_BLOCK_7___powershell `
- **Opening ` ___CODE_BLOCK_8___ ` must be on its own line**
- Always close with matching backticks
- Empty line before/after fenced blocks improves readability

### Code Blocks in Lists

When adding code blocks to list items (especially log entries):

````markdown
CORRECT FORMAT:
- 05:20
  ```powershell
  command here
  ```
  description text

WRONG FORMAT:
- 05:20 ```powershell
command here
```
description text
````

**Rules for code blocks in lists:**
- Indent code block 2 spaces to be part of the list item
- Indent all content (opening ___CODE_BLOCK_12___, description) consistently
- This preserves list structure and makes entries easy to read

## General Formatting

- Use standard markdown headers: `#` `##` `###`
- Use `-` for unordered lists
- Use `1.___INLINE_CODE_25[[Link]]INLINE_CODE_26___(` `)___INLINE_CODE_28[[brackets]]INLINE_CODE_29[[Note Name]]INLINE_CODE_30___` `List(T)` `___INLINE_CODE_33[[Link]]INLINE_CODE_34___ILogger(T)`
- Don't put wikilinks in frontmatter: `title: "[[Something]]"`
- Don't leave code blocks unclosed
- Don't use HTML/XML tags in content

## Configuration

To use this rule in your vault:

1. **Copy to your vault**: `.claude/rules/obsidian-syntax.md`
2. **Enable syntax-validate hook** (should be enabled by default in obsidian-scribe)
3. **Set `alwaysApply: true`** to enforce across all markdown files

The syntax-validate hook will automatically warn you about issues as you edit.

## Troubleshooting

### "Why are my wikilinks broken?"

Check for:
1. Angle brackets earlier in the document
2. Wrapped wikilinks with formatting
3. Unclosed code blocks

### "Frontmatter not parsing?"

Check for:
1. Wikilinks in YAML keys or values
2. Invalid YAML syntax
3. Missing closing `---`

## Related Documentation

- [Syntax-Validate Hook](../../plugins/obsidian-scribe/hooks/syntax-validate.py)
- [Wikilink-Suggest Hook](../../plugins/obsidian-scribe/hooks/wikilink-suggest.py)
- [Obsidian Formatting Help](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax)
