---
paths: "**/*.md"
alwaysApply: false
---

# Folder Organization Rules

These rules ALWAYS apply regardless of which file is being edited.

## Protected Top-Level Folders

These folders MUST only contain subfolders, never direct files.

Configure protected folders in `.obsidian-scribe.json`:

```json
{
  "folders": {
    "protected": ["personal", "work", "tech", "kanban"]
  }
}
```

| Folder | Correct Usage |
|--------|---------------|
| `personal/` | `personal/goals/`, `personal/health/` |
| `work/` | `work/projects/`, `work/notes/` |
| `tech/` | `tech/frameworks/`, `tech/tools/` |
| `kanban/` | `kanban/board-name/` |

### Examples

```
WRONG:
personal/MyNote.md
work/MyDoc.md
tech/MyTool.md
kanban/MyTask.md

CORRECT:
personal/goals/MyNote.md
work/projects/MyDoc.md
tech/frameworks/MyTool.md
kanban/work-board/MyTask.md
```

## Folders That Can Contain Files Directly

These top-level folders CAN contain files directly:

- `daily-notes/` - Daily journal entries
- `weekly-notes/` - Weekly summaries
- `monthly-notes/` - Monthly summaries
- `quarterly-notes/` - Quarterly summaries
- `yearly-notes/` - Yearly summaries
- `templates/` - Note templates

## File Creation Checklist

Before creating any new file:
1. Check if target folder is in "protected" list
2. If protected, ensure using a subfolder
3. If unsure which subfolder, ask user
