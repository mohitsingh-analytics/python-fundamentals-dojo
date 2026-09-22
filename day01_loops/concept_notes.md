# Day 1 — Loops & Iteration

## Key Concepts

- **`for i in range(a, b)`** — loops from `a` up to (not including) `b`. To make it inclusive of `b`, use `range(a, b+1)`.
- **`range()` is lazy** — it doesn't build a full list in memory upfront; `list(range(...))` forces it into an actual list.
- **Looping over a list directly** (`for item in my_list`) gives you the **value**, not the index.
- **`enumerate(iterable, start=1)`** — gives you `(index, value)` pairs together, with an optional custom starting number. Replaces manual counter variables.
- **Looping over a dict:**
  - `for key in my_dict` → keys only
  - `for value in my_dict.values()` → values only
  - `for key, value in my_dict.items()` → both, as a pair
- **`while` loops** run as long as the condition is `True`. Forgetting to update the loop variable causes an **infinite loop**.
- **`break`** exits the loop immediately — remaining items are never processed, even if they come later in the sequence.

## Common Mistakes I Made

- Forgot `range()`'s upper bound is exclusive — needed `+1` for inclusive ranges.
- Mixed up `while` loop direction (counted down instead of up) for the retry scenario.
- Syntax slip: wrote `break:` with a colon — `break` doesn't take one, it's not a block-opening statement.
- Indentation errors when nesting `if` inside `for` — Python enforces this strictly, no braces to fall back on.

## Where This Applies Later

- Dict looping (`.items()`) is exactly how you'll iterate over `state` in LangGraph nodes.
- `break`-on-condition is the same pattern used in retry/validation logic in real API-calling code.