---
paths: "**/*.md"
alwaysApply: false
---

# Obsidian Markdown Syntax Rules

These rules apply when editing ANY markdown file in the vault.

## Wikilinks

- Use `[[wikilink]]` format for internal links
- Use `[[Page|Display Text]]` for aliased links

### CRITICAL - Never Wrap Wikilinks

NEVER wrap wikilinks with formatting characters:

```
WRONG:
**[[Link]]**
*[[Link]]*
_[[Link]]_
`[[Link]]`

CORRECT:
[[Link]]
**Text with [[Link]] inside**
```

Wrapping wikilinks breaks Obsidian's hyperlink functionality.

## Angle Brackets

### CRITICAL - No Angle Brackets in Content

NEVER use angle brackets (< >) in Obsidian notes:

```
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

Example of breakage:
```
"Using ILogger<T> for logging" + later "[[Some Link]]"
= [[Some Link]] becomes broken/unclickable
```

### Allowed Uses of Angle Brackets
- Inside fenced code blocks (```)
- Inside inline code (`like this`)

## YAML Frontmatter

### CRITICAL - No Wikilinks in YAML Frontmatter

NEVER use wikilinks in YAML frontmatter keys or values:

```
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

### General YAML Rules

- Preserve existing metadata structure
- Don't modify frontmatter unless specifically asked
- Common fields: type, date, tags, aliases, title, created, description, source
- Keys must be lowercase without special characters
- Values should be plain text (no wikilinks except for author references)

## Code Blocks

### CRITICAL - Always Close Code Blocks

ALWAYS ensure fenced code blocks have matching opening and closing backticks:

```
WRONG:
```powershell
some command

(missing closing backticks)

CORRECT:
```powershell
some command
```

or inline:
`some command`
```

**Why this matters**: Unclosed code blocks break markdown rendering and cause everything after them to be treated as code.

### Code Block Rules

- Fenced code blocks use triple backticks: ` ``` `
- Inline code uses single backticks: `` ` ``
- Language identifier goes on opening line: ` ```powershell `
- **Opening ` ``` ` must be on its own line**
- **Closing ` ``` ` must be on its own line**
- Always close with matching backticks
- Empty line before/after fenced blocks improves readability

### Code Blocks in Lists

When adding code blocks to list items (especially log entries):

```
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
```

**Rules for code blocks in lists:**
- Indent code block 2 spaces to be part of the list item
- Indent all content (opening ```, code, closing ```, description) consistently
- This preserves list structure and makes entries easy to read

## General Formatting

- Use standard markdown headers: # ## ###
- Use - for unordered lists
- Use 1. for ordered lists
- Preserve existing indentation patterns
