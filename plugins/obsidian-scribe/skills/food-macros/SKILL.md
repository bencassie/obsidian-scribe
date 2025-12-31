---
name: food-macros
description: Calculate daily nutrition macros from food entries and insert formatted tables. Triggers on "macros", "calories", "nutrition", "food totals", "what did I eat", "calculate food".
auto_trigger: true
trigger_keywords:
  - "macros"
  - "calories"
  - "nutrition"
  - "food totals"
  - "what did I eat"
  - "calculate food"
  - "calculate macros"
  - "nutrition summary"
allowed-tools: Read, Edit
---

# Food Macros Calculation

Calculate nutrition for daily food entries and insert formatted tables into daily notes.

## When to Use

This skill activates when the user asks about:
- Daily food/nutrition/macros/calories
- "Calculate my macros"
- "What are my totals today"
- "Food summary"

## Process

1. **Identify the daily note**
   - Default to today: `{paths.daily_notes}/YYYY-MM-DD.md`
   - Or use specified date if provided

2. **Read the daily note**
   - Find the Food section (from config `sections.food`)
   - Extract all food entries (bullet points under Food)

3. **Look up nutrition data**
   - Use common nutritional knowledge for known foods
   - For unknown foods, estimate based on similar items or ask user
   - NEVER fabricate data - if uncertain, ask

4. **Calculate totals**
   - Sum all columns: Calories, Carbs, Sugars, Protein, Fat, Sat Fat, Fiber

5. **Insert the table**
   - Place after the food list, before the next section
   - Use Edit tool with exact text matching
   - If table exists, replace it entirely

## Output Format

```markdown
## Food Macros
| Food Item | Calories (kCal) | Carbs (g) | Sugars (g) | Protein (g) | Fat (g) | Sat Fat (g) | Fiber (g) |
|-----------|-----------------|-----------|------------|-------------|---------|-------------|-----------|
| Item 1    | xxx             | xx        | xx         | xx          | xx      | xx          | xx        |
| Item 2    | xxx             | xx        | xx         | xx          | xx      | xx          | xx        |
| **TOTAL** | **xxxx**        | **xx**    | **xx**     | **xx**      | **xx**  | **xx**      | **xx**    |
```

## Critical Rules

- **No fabrication**: Only use existing food entries
- **Exact matching**: Use precise text for Edit tool old_string
- **One operation**: Read -> Calculate -> Insert in single workflow
- **Preserve formatting**: Don't break existing daily note structure

## Common Foods Reference

Use standard nutritional values for common foods:
- **Eggs** (1 large): 70 cal, 0g carbs, 6g protein, 5g fat
- **Toast** (1 slice): 80 cal, 15g carbs, 3g protein, 1g fat
- **Apple**: 95 cal, 25g carbs, 19g sugars, 0g protein
- **Chicken breast** (100g): 165 cal, 0g carbs, 31g protein, 3.6g fat
- **Rice** (1 cup cooked): 206 cal, 45g carbs, 4g protein, 0g fat

For foods not in this reference, use your nutritional knowledge or ask the user.

## Configuration

This skill uses these config values:
- `paths.daily_notes`: Folder containing daily notes (default: "daily-notes")
- `sections.food`: Food section header (default: "# Food")
