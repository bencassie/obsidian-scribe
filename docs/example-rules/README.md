# Example Rules for obsidian-scribe

This directory contains example rule files that demonstrate how to configure Claude Code rules for use with the obsidian-scribe plugin. These files are **informational/documentation** - you should copy them to your vault's `.claude/rules/` directory and adapt them to your needs.

## What are Claude Code Rules?

Claude Code rules are markdown files with YAML frontmatter that provide context and instructions to Claude when working on specific files or across your entire vault. They're stored in `.claude/rules/` within your vault.

## Available Example Rules

### 1. `achievements.md` - Achievement Log Format

**Purpose**: Documents the format requirements for tracking achievements in a dedicated log file.

**Key concepts**:
- Timestamp format: `- YYYY-MM-DD HH:MM - Achievement text`
- Chronological ordering (append-only structure)
- Monthly/yearly organization
- Automatic deduplication
- Integration with achievement-detect hook

**When to use**: If you want to maintain a structured achievement log that's auto-populated by the achievement-detect hook.

**Setup**:
1. Copy to `.claude/rules/achievements.md` in your vault
2. Update `paths` frontmatter to point to your achievements file
3. Configure achievement file path in `.obsidian-scribe.json`

---

### 2. `daily-notes.md` - Daily Note Structure

**Purpose**: Documents recommended structure and formatting for daily notes used in the rollup chain.

**Key concepts**:
- ISO date format filenames (YYYY-MM-DD.md)
- Log section as continuous bullet list (no `---` or `## Headings` inside)
- Chronological order (append to bottom)
- Timestamp format (HH:MM)
- Integration with achievement detection and rollup agents

**When to use**: If you use daily notes for journaling, logging work, or habit tracking.

**Setup**:
1. Copy to `.claude/rules/daily-notes.md` in your vault
2. Update `paths` frontmatter to match your daily notes folder
3. Configure daily notes path in `.obsidian-scribe.json`

---

### 3. `obsidian-syntax.md` - Obsidian Markdown Syntax Rules

**Purpose**: Documents critical syntax issues that break Obsidian functionality.

**Key concepts**:
- Never wrap wikilinks with formatting (`**[[Link]]**` breaks hyperlinks)
- No angle brackets in content (breaks all subsequent wikilinks)
- No wikilinks in YAML frontmatter (corrupts metadata)
- Always close code blocks
- Code block formatting in lists

**When to use**: For all markdown files in your vault to prevent syntax errors.

**Setup**:
1. Copy to `.claude/rules/obsidian-syntax.md` in your vault
2. Set `alwaysApply: true` to enforce across all markdown files
3. Enable syntax-validate hook (enabled by default in obsidian-scribe)

**Enforcement**: The `syntax-validate` hook automatically checks for these issues.

---

### 4. `platform-requirements.md` - Platform-Specific Setup

**Purpose**: Documents platform-specific requirements for obsidian-scribe on WSL and Windows.

**Key concepts**:
- Python symlink requirement for WSL (`python-is-python3`)
- Path format differences (WSL: `/mnt/c/...`, Windows: `C:/...`)
- Cross-platform hook commands using `python` (not `python3`)
- MCP server configuration differences
- Troubleshooting hook execution issues

**When to use**: As a troubleshooting reference when hooks aren't executing or for cross-platform setup.

**Setup**:
1. Copy to `.claude/rules/platform-requirements.md` in your vault
2. Set `alwaysApply: true` to get reminders across all files
3. Follow platform-specific setup steps

---

## Rule File Structure

All example rules use a **combined frontmatter format** with both Claude Code scoping and Obsidian metadata:

```yaml
---
# Claude Code scoping (controls when rule applies)
paths: "path/to/your/files/**/*.md"  # Glob pattern for file matching
alwaysApply: false                   # true = apply to all files in project

# Obsidian metadata (for vault organization)
type: rule                           # Marks this as a rule file
tags:
  - rule
  - your-category
aliases:
  - Human-Readable Name
date: YYYY-MM-DD                     # Creation/modification date
description: Brief description
---

# Rule Content (Markdown)

Your rule instructions and documentation here...
```

### Frontmatter Fields

**Claude Code fields** (controls behavior):
- `paths`: Glob pattern(s) for file matching (e.g., `"daily-notes/**/*.md"`)
- `alwaysApply`: Boolean - if `true`, applies to all files in the project

**Obsidian fields** (for organization):
- `type`: Should be `rule` for rule files
- `tags`: Array of tags (always include `rule`)
- `aliases`: Alternative names for the rule
- `date`: ISO date (YYYY-MM-DD)
- `description`: Brief description of the rule's purpose

## How to Use These Examples

1. **Identify relevant rules** for your workflow (achievements, daily notes, syntax validation, etc.)

2. **Copy to your vault**:
   ```bash
   cp docs/example-rules/[rule-name].md /path/to/your/vault/.claude/rules/
   ```

3. **Adapt the configuration**:
   - Update `paths` frontmatter to match your vault structure
   - Customize `alwaysApply` based on scope (true = all files, false = specific paths)
   - Update example paths in the content to match your setup

4. **Configure obsidian-scribe** (if needed):
   Edit `.obsidian-scribe.json` in your vault root:
   ```json
   {
     "paths": {
       "daily_notes": "daily-notes",
       "achievements": "personal/goals/Achievements.md"
     },
     "sections": {
       "log": "## Log"
     }
   }
   ```

5. **Verify hooks are enabled**:
   Check your Claude Code session startup for:
   - "Registered 4 hooks from obsidian-scribe"
   - Hook names: session-start, wikilink-suggest, achievement-detect, syntax-validate

## Rule Interactions with Hooks

obsidian-scribe hooks use these rules as context:

| Hook | Related Rules | Behavior |
|------|---------------|----------|
| **syntax-validate** | obsidian-syntax.md | Warns about wrapped wikilinks, angle brackets, frontmatter issues |
| **achievement-detect** | achievements.md, daily-notes.md | Auto-detects achievements from daily notes, writes to log with timestamps |
| **wikilink-suggest** | obsidian-syntax.md | Auto-applies `[[brackets]]` to entity mentions (respects protected zones) |
| **session-start** | platform-requirements.md | Provides vault intelligence at session start |

## Testing Your Rules

After copying rules to your vault:

1. **Start new Claude Code session** in your vault
2. **Check debug log** for rule loading:
   ```bash
   # WSL
   cat ~/.claude/debug/[session-id].txt | grep "rules"

   # Windows (PowerShell)
   Get-Content $env:USERPROFILE\.claude\debug\[session-id].txt | Select-String "rules"
   ```

3. **Test rule behavior**:
   - Edit a file matching the rule's `paths` pattern
   - Ask Claude about the rule's topic (achievements, syntax, etc.)
   - Verify Claude references the rule in its response

## Customization Examples

### Example 1: Different Daily Notes Folder

If your daily notes are in `journal/` instead of `daily-notes/`:

```yaml
# In .claude/rules/daily-notes.md frontmatter:
paths: "journal/**/*.md"
```

```json
// In .obsidian-scribe.json:
{
  "paths": {
    "daily_notes": "journal"
  }
}
```

### Example 2: Multiple Achievement Logs

If you have separate work/personal achievement logs:

```yaml
# Create .claude/rules/work-achievements.md:
paths: "work/achievements/Work-Log.md"

# Create .claude/rules/personal-achievements.md:
paths: "personal/goals/Achievements.md"
```

### Example 3: Apply Syntax Rules Everywhere

```yaml
# In .claude/rules/obsidian-syntax.md frontmatter:
paths: "**/*.md"
alwaysApply: true
```

## Troubleshooting

### Rules Not Loading

**Check**:
1. Rule files are in `.claude/rules/` directory
2. Frontmatter is valid YAML (no syntax errors)
3. `paths` pattern matches your file structure
4. Debug log shows "Loaded X rules" at session start

### Hooks Not Running

**Check**:
1. Platform requirements met (see platform-requirements.md)
2. Python available as `python` (not just `python3`)
3. Hooks registered in debug log
4. MCP servers connected (smoking-mirror required for vault-* skills)

**WSL-specific**:
```bash
# Install python symlink if missing
sudo apt install python-is-python3
python --version  # Should show Python 3.x.x
```

## Related Documentation

- [obsidian-scribe Installation Guide](../installation/README.md)
- [Hook Configuration](../../plugins/obsidian-scribe/hooks/hooks.json)
- [Configuration Schema](../../plugins/obsidian-scribe/config/schema.json)
- [Troubleshooting Guide](../installation/troubleshooting.md)
- [Cross-Platform Setup](../../CLAUDE.md.example)

## Contributing

Have a useful rule pattern? Consider contributing it to this directory:

1. Create your rule in `docs/example-rules/`
2. Add "EXAMPLE/INFORMATIONAL" note in frontmatter
3. Use placeholder paths (not your specific vault paths)
4. Include setup instructions
5. Document configuration requirements
6. Submit a pull request

## License

These example rules are part of obsidian-scribe and released under the MIT license.
