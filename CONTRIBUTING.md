# Contributing to [[Obsidian Scribe]]

Hoot hoot! Welcome to the nest, fellow [[Developer]]! 🦉

We're delighted [[You]] want to help make [[Obsidian]] [[Scribe]] even wiser. [[This]] [[Guide]] will help you spread your wings and contribute effectively.

## Development Setup

### Prerequisites

- **[[Python]] 3.8+** with `python` [[Command]] [[Available]]
  - [[WSL]]: Install `python-is-python3` package
  - [[Windows]]: Ensure Python in PATH as `python`
- **[[Claude Code]]** installed and configured
- **[[Git]]** for version control
- An Obsidian [[Vault]] for [[Testing]]

### Clone and Setup

```bash
git clone https://github.com/bencassie/obsidian-scribe.git
cd obsidian-scribe

# Validate the plugin structure
python verify-plugin.py
```

## Code Organization by Domain

The plugin is organized into feature domains, though currently in a flat structure:

| Domain | Components | Dependencies |
|--------|------------|--------------|
| **Core/Logging** | auto-log, task-add, session-start hook | None |
| **Wikilinks** | rebuild-cache, wikilink-apply, syntax-validate, wikilink-suggest hooks | smoking-mirror MCP |
| **Rollup** | rollup skill + 5 agents | None |
| **Vault Intelligence** | 15 vault-* skills | smoking-mirror MCP |
| **Achievements** | achievement-detect hook | None |

When adding features, consider which domain they belong to.

## Version Management Rules

**CRITICAL:** The plugin uses a marketplace architecture with 3 version files that must stay synchronized.

### Version Files (All Must Match)

1. Root marketplace: `.[[Claude]]-[[Plugin]]/[[Marketplace]].[[JSON]]`
2. Plugin marketplace: `plugins/obsidian-scribe/.claude-plugin/marketplace.json`
3. Plugin config: `plugins/obsidian-scribe/.claude-plugin/plugin.json`

### Version Bump Process

```bash
# 1. Find all version fields
grep -n '"version":' .claude-plugin/marketplace.json \
  plugins/obsidian-scribe/.claude-plugin/marketplace.json \
  plugins/obsidian-scribe/.claude-plugin/plugin.json

# 2. Update all to same version (e.g., 1.0.8)
# 3. Verify all match
```

**When to bump:**
- Bug fixes: Patch version (1.0.X)
- New features: Minor version (1.X.0)
- Breaking changes: Major version (X.0.0)

## Development Workflow

### Making Changes

1. **Make your changes** to skills, hooks, or agents
2. **Bump version** in all 3 manifest files (see Version Management above)
3. **Test locally** (see Testing Procedures below)
4. **Commit and push** to GitHub
5. **Update local installation** (see next section)

### Updating Your Local Plugin After Push

**IMPORTANT**: After pushing to GitHub, the plugin does NOT automatically update. You must manually pull and update:

```bash
# 1. Pull latest from GitHub marketplace clone
cd ~/.claude/plugins/marketplaces/obsidian-scribe
git pull origin main

# 2. Update installed plugin (use --scope local for local-scoped plugins)
# NOTE: Command is "plugin" (singular), not "plugins"
claude plugin update --scope local obsidian-scribe@obsidian-scribe

# 3. Restart Claude Code session
```

**Verification:**

```bash
# Check installed version
cat ~/.claude/plugins/installed_plugins.json | grep -A 10 obsidian-scribe

# After restart, check debug log
cat ~/.claude/debug/<session-id>.txt | grep "Found.*plugins"
```

Expected output:
- `Found 2 plugins (2 enabled, 0 disabled)`
- `Registered X hooks from 2 plugins`

**Common Issues:**

- **Hooks not loading**: Check that `plugin.json` includes `"hooks": "./hooks/hooks.json"`
- **Old version persists**: The marketplace clone may not have pulled latest - verify with `git log -1`
- **Wrong command syntax**: It's `claude plugin` (singular), NOT `claude plugins`

## Testing Procedures

### Hook Testing

Test hooks manually with sample JSON input:

```bash
# Create test input
cat > /tmp/test-hook.json << 'EOF'
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "daily-notes/2026-01-01.md"
  }
}
EOF

# Test the hook
cat /tmp/test-hook.json | python plugins/obsidian-scribe/hooks/achievement-detect.py
```

### Cross-Platform Testing

**Always test on both platforms:**

| Platform | Python Command | Path Format |
|----------|----------------|-------------|
| WSL | `python3` | `/mnt/c/...` |
| Windows | `python` | `C:/...` |

```bash
# WSL
cd /mnt/c/Users/.../obsidian-scribe
python3 plugins/obsidian-scribe/hooks/session-start.py

# Windows PowerShell
cd C:\Users\...\obsidian-scribe
python plugins\obsidian-scribe\hooks\session-start.py
```

### Skill Testing

Test skills using Claude Code in a test vault:

```bash
# In Claude Code
/auto-log Testing new feature
/vault-health
/rollup
```

## Pull Request Guidelines

### Before Submitting

- [ ] Version bumped in all 3 files
- [ ] Tested on WSL and Windows
- [ ] Hook tests pass with sample input
- [ ] Code follows existing patterns
- [ ] Documentation updated if adding features
- [ ] `verify-plugin.py` passes

### PR Description

Include:
1. **What changed:** Brief description
2. **Why:** Problem being solved or feature added
3. **Testing:** Platforms tested (WSL/Windows)
4. **Breaking changes:** Any changes requiring user action

## Code Style

### Python

- Follow PEP 8
- Use descriptive variable names
- Add docstrings to functions
- Handle errors gracefully (exit 0 for hooks)

### Hook Patterns

All hooks should:
- Accept JSON input via stdin
- Exit with code 0 (never block operations)
- Print user-friendly output
- Handle exceptions gracefully

```python
#!/usr/bin/env python3
"""
Brief hook description.
"""
import json
import sys

def main():
    try:
        hook_input = json.load(sys.stdin)
        # Hook logic here
        print("✓ Success message")
        sys.exit(0)
    except Exception as e:
        print(f"[obsidian-scribe] Error: {e}", file=sys.stderr)
        sys.exit(0)  # Never block

if __name__ == "__main__":
    main()
```

### Skill Patterns

Skills should:
- Provide clear, actionable output
- Follow domain conventions
- Include usage examples in SKILL.md

## Documentation

When adding features:

1. **Create/update SKILL.md** for new skills
2. **Update feature docs** in `docs/features/`
3. **Add examples** if introducing new workflows
4. **Update getting-started** if setup changes

## Repository Assets

### Images

All branding images are stored in `docs/assets/`:

| File | Purpose | Dimensions |
|------|---------|------------|
| `logo.png` | Compact logo (square) | 512x512 |
| `logo-alt.png` | Logo with text | 512x512 |
| `banner.png` | Feature showcase | 1200x630 |
| `feature-icons.png` | Feature icons (transparent) | 512x512 |
| `social-preview.png` | GitHub social preview | 1280x640 |

### GitHub Social Preview

To set the social preview image (shown when sharing repo links):

1. Go to repository **Settings** > **General**
2. Scroll to **Social preview**
3. Click **Edit** > **Upload an image**
4. Select `docs/assets/social-preview.png`
5. Save changes

## Questions?

The wise owl is here to help!

- Open an issue for questions
- Join discussions for [[Design]] ideas
- Check [[Existing]] issues before [[Creating]] new [[Ones]]

Thank you for helping Obsidian Scribe grow wiser!
