# Hook Diagnostics Test Procedure

## Quick Test Commands

### Windows (PowerShell/cmd)
```powershell
cd C:\Users\benca\obsidian\Ben
python C:\Users\benca\src\obsidian-scribe\diagnose-hooks.py
```

### WSL (bash)
```bash
cd /mnt/c/Users/benca/obsidian/Ben
python3 /mnt/c/Users/benca/src/obsidian-scribe/diagnose-hooks.py
```

---

## Full Test Procedure

### Step 1: Start Fresh Claude Code Session

**Windows:**
```powershell
cd C:\Users\benca\obsidian\Ben
claude
```

**WSL:**
```bash
cd /mnt/c/Users/benca/obsidian/Ben
claude
```

### Step 2: Check Session Startup Message

Look for these in the startup output:
- `SessionStart:startup hook success` - Which hooks ran?
- Any error messages about plugins or hooks

### Step 3: Run Diagnostic Script

In the Claude Code session, ask:
```
run python C:/Users/benca/src/obsidian-scribe/diagnose-hooks.py
```

Or for WSL:
```
run python3 /mnt/c/Users/benca/src/obsidian-scribe/diagnose-hooks.py
```

### Step 4: Run Claude Code Commands

Run these commands in the Claude Code session:

```
/hooks
```
→ Should show SessionStart hooks including obsidian-scribe

```
/plugins
```
→ Should list obsidian-scribe as installed/enabled

```
/context
```
→ Shows all loaded context, skills, agents from plugins

### Step 5: Check Wikilink Cache

```
run python -c "import json; d=json.load(open('.claude/wikilink-entities.json')); print(d['_metadata'])"
```

Key things to check:
- `generated_at`: Was it just generated (session start) or stale?
- `vault_path`: Does it show Windows or WSL path?
- `generator`: Should say "obsidian-scribe"

---

## What to Compare

| Check | Windows | WSL |
|-------|---------|-----|
| Session startup hook message | ? | ? |
| `/hooks` shows obsidian-scribe | ? | ? |
| `/plugins` shows obsidian-scribe | ? | ? |
| Wikilink cache freshly generated | ? | ? |
| Cache path format | C:\... or /mnt/c/... | ? |
| CLAUDE_PLUGIN_ROOT set | ? | ? |

---

## Expected Output

### If Plugin Hooks Work ✅
```
SessionStart:startup hook success: Success
  - session-start-ai-briefing.py
  - obsidian-scribe/session-start.py  ← Plugin hook!

Wikilink cache: 1153 entities (just generated)
```

### If Plugin Hooks Don't Work ❌
```
SessionStart:startup hook success: Success
  - session-start-ai-briefing.py only

Wikilink cache: old timestamp, wrong path format
```

---

## Debug Mode

For detailed debugging, start Claude with:

```bash
claude --debug hooks
```

Or for all debug output:
```bash
claude --debug '*'
```

This shows hook loading, plugin discovery, and execution details.
