# [[Wikilinks]] 🦉🔗

*Hoot! A well-linked [[Vault]] is a wise vault. Let the owl help [[You]] connect your [[Knowledge]].*

[[Wikilink]] [[Features]] automatically [[Suggest]], [[Apply]], and validate [[Links]] in your [[Notes]].

## Features in [[This]] [[Domain]]

| [[Feature]] | Type | Purpose |
|---------|------|---------|
| `/rebuild-wikilink-cache` | [[Skill]] | Rebuild [[Entity]] cache |
| `/wikilink-apply` | Skill | Apply [[Link]] [[Suggestions]] to a [[Note]] |
| `syntax-validate` | [[Hook]] | Warn about [[Syntax]] issues |
| `wikilink-suggest` | Hook | [[Auto]]-apply wikilinks [[After]] [[Edits]] |

**Requires:** smoking-[[Mirror]] [[MCP]] (for `/wikilink-apply` suggestions)

## How It Works

The owl maintains a cache of wikilink [[Entities]] (note titles and aliases) and automatically:
1. **Detects** [[When]] you write [[Text]] [[Matching]] [[Existing]] notes
2. **Suggests** adding `[[brackets]]` around [[Matches]]
3. **Validates** syntax to [[Prevent]] broken links

## `/rebuild-wikilink-cache`

Rebuild the entity cache from your vault.

### Usage

```bash
/rebuild-wikilink-cache
```

### When To Use

- After creating many new notes
- After renaming notes
- When wikilink suggestions seem outdated
- After importing notes from another vault

### Example Output

```
Wikilink cache rebuilt
Entities indexed: 1154
```

*The owl catalogs every note title and alias for quick reference!*

## `/wikilink-apply`

Apply wikilink suggestions to a specific note.

### Usage

```bash
/wikilink-apply path/to/note.md
```

### How It Works

1. Reads the note content
2. Uses smoking-mirror to detect entity mentions
3. Suggests adding `[[brackets]]` around matches
4. Applies changes automatically

### Example

**Before:**
```markdown
I use Claude Code with Obsidian for knowledge management.
```

**After:**
```markdown
I use [[Claude Code]] with [[Obsidian]] for knowledge management.
```

*The owl sees connections you might have missed!* 🦉

## Syntax Validation Hook

Runs automatically after Edit/Write operations to prevent common syntax errors.

### What It Checks

**1. Wrapped Wikilinks**

```markdown
❌ **[[Link]]**  (breaks hyperlink)
✅ [[Link]]      (works correctly)

❌ *[[Link]]*    (breaks hyperlink)
✅ [[Link]]      (works correctly)
```

**2. Angle Brackets in Content**

```markdown
❌ Using ILogger<T> for logging
✅ Using ILogger(T) for logging

❌ List<string> contains items
✅ List of string contains items
```

*Why?* Angle brackets break ALL wikilinks that follow them in Obsidian.

**3. Wikilinks in Frontmatter**

```markdown
❌ title: "[[Some]] [[Text]]"
✅ title: "Some Text"

❌ [[Key]]: value
✅ key: value
```

*Frontmatter should use plain text, not wikilinks!*

### Example Warning

```
⚠️  Syntax Issue Detected

File: daily-notes/2026-01-01.md

Issue: Wrapped wikilink detected
  Line: **[[Important Note]]**
  Fix: Remove formatting around [[brackets]]

Wrapped wikilinks break Obsidian's hyperlink functionality.
```

## Wikilink Suggest Hook

Runs automatically after Edit/Write operations to apply wikilinks.

### How It Works

1. Reads the file you just edited
2. Checks wikilink entity cache
3. Finds text matching note titles/aliases
4. Auto-applies `[[brackets]]` around matches

### Example

You write:
```markdown
Today I learned about Model Context Protocol and Claude Code.
```

The owl auto-converts to:
```markdown
Today I learned about [[Model Context Protocol]] and [[Claude Code]].
```

*Automatic linking as you write - no manual work needed!* 🦉✨

### Configuration

Control sensitivity in `.[[Obsidian]]-scribe.json`:

```json
{
  "wikilinks": {
    "auto_apply": true,
    "min_entity_length": 3,
    "exclude_patterns": [
      "the", "and", "or", "but"
    ]
  }
}
```

## Common Workflows

### New Note Setup

```bash
# Create a note with many entity mentions
# (edit in Obsidian or via Claude Code)

# Apply wikilinks automatically
/wikilink-apply new-note.md
```

The owl adds [[brackets]] around all matching entities.

### Vault-Wide Link Cleanup

```bash
# Rebuild cache first
/rebuild-wikilink-cache

# Then use vault-fix-links to repair broken ones
/vault-fix-links

# Check for unlinked mentions
/vault-unlinked-mentions "Entity Name"
```

### Preventing Link Breakage

The syntax validation hook catches issues automatically:
- Edit a note in Obsidian
- Hook fires on save
- Warns if you used angle brackets or wrapped wikilinks
- Fix before they break links!

## Best Practices

### 1. Keep Cache Fresh

Rebuild after major changes:
```bash
/rebuild-wikilink-cache
```

### 2. Review Auto-Applied Links

The hook is helpful but not perfect - review suggestions:
- Check that context makes sense
- Remove false positives manually
- Add custom exclude patterns for common words

### 3. Avoid Syntax Traps

- Don't wrap wikilinks: `[[Link]]` not `**[[Link]]**`
- No angle brackets: `ILogger(T)` not `ILogger<T>`
- Plain text in frontmatter: `title: "Note"` not `title: "[[Note]]"`

## Troubleshooting

### Auto-suggestions not applying

**Check:**
- Cache is built: `/rebuild-wikilink-cache`
- Hook is enabled in plugin config
- Python is available as `[[Python]]` command

### Too many false positives

**Adjust config:**
```json
{
  "wikilinks": {
    "min_entity_length": 5,  // Increase threshold
    "exclude_patterns": ["common", "word", "list"]
  }
}
```

### Syntax warnings [[Not]] showing

**Ensure:**
- [[Hooks]] [[Are]] enabled
- You're editing markdown [[Files]] in vault
- Hook has correct permissions

## [[Related]] Features

- **[Vault Intelligence](vault-intelligence.md)** - [[Analyze]] link patterns
- **[Daily Logging](daily-logging.md)** - Wikilinks in [[Log]] entries
- **[Examples](../examples/)** - [[See]] wikilink [[Workflows]] in [[Action]]

---

*"A thousand links begin with a single [[bracket]], dear scholar!"* 🦉🔗
