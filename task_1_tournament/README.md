# Coding Task 1: League Tournament Table Generator

## Objective
Implement the function `tally(rows: list[str]) -> str` in `tournament.py` that processes match score results from a sports league and returns a formatted standings table string according to standard international league ranking rules.

---

## Input Specification
You are given a list of strings (`rows`). Each string represents a match result in the format:
```text
"<Team1>;<Team2>;<Score1>-<Score2>"
```
*Example*: `"Allegheny;Blizzards;3-1"` means Allegheny scored 3 goals and Blizzards scored 1 goal.

---

## Scoring & Statistics
For every team, calculate:
- **MP**: Matches Played
- **W**: Matches Won (scored strictly more goals than the opponent)
- **D**: Matches Drawn (both teams scored equal goals)
- **L**: Matches Lost (scored fewer goals than the opponent)
- **GF**: Goals For (total goals scored)
- **GA**: Goals Against (total goals conceded)
- **GD**: Goal Difference (`GF - GA`)
- **P**: Total Points (**3** points for a win, **1** point for a draw, **0** for a loss)

---

## Multi-Tier Tie-Breaking Hierarchy
Teams must be ordered according to the following strict ranking criteria:
1. **Total Points (`P`)** (descending)
2. **Goal Difference (`GD`)** (descending)
3. **Goals For (`GF`)** (descending)
4. **Head-to-Head Result** (if two teams are tied on points, GD, and GF, the winner of their direct head-to-head match takes precedence)
5. **Team Name** (alphabetically ascending, A to Z)

---

## Output Format
Return a single multi-line string (lines joined by `\n`).

### 1. Header Line:
```text
Team                           | MP |  W |  D |  L | GF | GA | GD |  P
```
- Column 1 (`Team`): 30 characters wide, left-aligned (`f"{team:<30}"`).
- Columns 2–9 (`MP`, `W`, `D`, `L`, `GF`, `GA`, `GD`, `P`): 2 characters wide, right-aligned (`f"{val:>2}"`), separated by `" | "`.

### 2. Edge Case (Empty Input):
If `rows` is empty (`[]`), return **only** the header string:
```text
"Team                           | MP |  W |  D |  L | GF | GA | GD |  P"
```

### 3. Example:
Given:
```python
rows = [
    "Allegheny;Blizzards;3-1",
    "Courage;Devils;2-2",
]
```
Expected output:
```text
Team                           | MP |  W |  D |  L | GF | GA | GD |  P
Allegheny                      |  1 |  1 |  0 |  0 |  3 |  1 |  2 |  3
Courage                        |  1 |  0 |  1 |  0 |  2 |  2 |  0 |  1
Devils                         |  1 |  0 |  1 |  0 |  2 |  2 |  0 |  1
Blizzards                      |  1 |  0 |  0 |  1 |  1 |  3 | -2 |  0
```
*(Courage and Devils tied on points, GD, and GF, and drew each other, so Courage comes first alphabetically).*

---

## How to Run Tests
From your terminal:
```bash
python test_tournament.py
```
Or:
```bash
python -m unittest test_tournament.py
```
There are **5 unit tests**. All 5 must pass for the task to be complete.
