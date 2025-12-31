---
name: food
description: Log food entries to daily notes with timestamps. Triggers when user mentions eating, food items, meals, snacks, "I ate", "I had", "breakfast", "lunch", "dinner", "snack", or wants to track nutrition. Use when user wants to log what they consumed.
auto_trigger: true
trigger_keywords:
  - "food"
  - "ate"
  - "eating"
  - "I had"
  - "I ate"
  - "breakfast"
  - "lunch"
  - "dinner"
  - "snack"
  - "meal"
  - "consumed"
  - "log food"
  - "track food"
  - "food entry"
  - "what I ate"
allowed-tools: Read, Edit
---

# Food Logger

Automatically log food entries to your daily notes with timestamps.

## When This Skill Activates

This skill triggers when you say things like:
- "I had eggs and toast for breakfast"
- "Log food: chicken salad"
- "Ate an apple with peanut butter"
- "Lunch was pasta"
- "Track this food: protein shake"
- "I ate pizza for dinner"

## Your Task

When user mentions food:

### 1. Extract Food Description

From the user's message, identify what they ate:
- "eggs and toast" → Food entry
- "Breakfast: oatmeal with berries" → Food entry
- "Apple with peanut butter" → Food entry

If the food description is unclear, ask the user to clarify.

### 2. Get Current Time

Parse time from the injected UserPromptSubmit hook context:
- Hook provides: "Time: HH:MM"
- Extract: "HH:MM"

Format: HH:MM (24-hour, e.g., 14:30)

**IMPORTANT**: Do NOT use Bash or PowerShell. Time is already provided by hook context.

### 3. Construct Daily Note Path

Today's daily note path:
```
{paths.daily_notes}/YYYY-MM-DD.md
```

Use today's date in YYYY-MM-DD format. Path from config.

### 4. Read Daily Note

Read the current daily note and locate the Food section (from config `sections.food`).

### 5. Add Food Entry

Use the Edit tool to add the food entry in this format:
```
- HH:MM [food description]
```

Add it to the end of the existing food entries (maintain chronological order).

Example:
```markdown
# Food
- 08:30 Breakfast: eggs and toast
- 12:15 Apple with peanut butter
- 19:00 Dinner: grilled chicken and vegetables  ← ADD HERE
```

### 6. Confirm

Tell the user:
- ✅ Logged food entry
- Timestamp: HH:MM
- What was logged: [food description]

## Critical Rules

- ✅ **Always include timestamp** in HH:MM format
- ✅ **Preserve structure**: Don't modify other sections
- ✅ **Bullet format**: Use `- HH:MM description`
- ✅ **Today only**: Only log to current day's note
- ✅ **Be smart about format**: If user says "breakfast: eggs", keep that format
- ✅ **Extract naturally**: "I ate pizza" → log as "Pizza", not "I ate pizza"

## Examples

**User says**: "I had eggs and toast for breakfast"

**You do**:
1. Extract: "Breakfast: eggs and toast"
2. Get time: "08:30"
3. Add to daily note: `- 08:30 Breakfast: eggs and toast`
4. Confirm: "✅ Logged breakfast at 08:30"

**User says**: "ate an apple"

**You do**:
1. Extract: "Apple"
2. Get time: "14:15"
3. Add: `- 14:15 Apple`
4. Confirm: "✅ Logged apple at 14:15"

**User says**: "log food chicken salad for lunch"

**You do**:
1. Extract: "Lunch: chicken salad"
2. Get time: "12:30"
3. Add: `- 12:30 Lunch: chicken salad`
4. Confirm: "✅ Logged lunch at 12:30"

## Smart Detection

Be intelligent about extracting food from natural language:
- "I'm having coffee" → Log "Coffee"
- "Just ate a sandwich" → Log "Sandwich"
- "Dinner was steak and potatoes" → Log "Dinner: steak and potatoes"
- "Snacking on almonds" → Log "Snack: almonds"

## Edge Cases

- If user mentions food but seems to be asking about it (not logging), ask: "Would you like me to log this to your food entries?"
- If daily note doesn't exist, create it from template first
- If Food section doesn't exist, add it to the daily note

## Configuration

This skill uses these config values:
- `paths.daily_notes`: Folder containing daily notes (default: "daily-notes")
- `sections.food`: Food section header (default: "# Food")
