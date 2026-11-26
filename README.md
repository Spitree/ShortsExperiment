# Experimental Programming Tasks: Impact of Short-Form Video on Cognitive Performance

This repository contains two calibrated Python tasks designed for an empirical study with 5th-year CS students using a randomized within-subjects crossover experiment (**AB/BA counterbalanced design**).

The two tasks evaluate different cognitive modalities of software engineering to assess how short-form video consumption affects focus, attention residue, and task re-entry:
1. **Coding Task 1 (Feature Synthesis / Algorithm Implementation)**: Implementing a sports tournament table with score parsing, goal differential metrics, and a multi-tier tie-breaking algorithm (Points -> GD -> GF -> Head-to-Head -> Alphabetical).
2. **Coding Task 2 (Code Comprehension & Debugging)**: Reading a meeting room reservation module, diagnosing 5 distinct algorithmic and state-management defects from unit test failures, and correcting them.

---

# Survey links
[Pre Survey] - https://forms.gle/JWEZ7tPKsHSF2wJG9  
[Post Task Survey] - https://forms.gle/uvZjTqDtASXkW2Sd7  
[Post Experiment Survey] - https://forms.gle/CWm4JjoinFKgYzTw5  

## Experimental Design & Metric Alignment

| Metric | Measurement Method | Implementation in Task Suite |
| :--- | :--- | :--- |
| **RQ1: Effectiveness (Task Score)** | Count of passed unit tests (0 to 5) within the allotted time. | Both tasks feature exactly 5 unit tests (0/5 to 5/5 score). |
| **RQ2: Context-Switching Cost (TTFP)** | Time to First Passing Test (timestamp of 1st passed test - block start time). | **Test 1** in both tasks provides an accessible initial milestone to serve as a reliable behavioral proxy for attention re-engagement. |
| **Work Dynamics** | Total test executions and total completion time. | Captured via local test runner wrappers on standard `python test_*.py` executions. |
| **Cognitive Modality** | Generative vs. analytical debugging processes. | **Task 1** measures generative feature writing; **Task 2** measures code reading, defect localization, and error diagnosis. |

---

## Tasks Summary

### Task 1: League Tournament Table (`task_1_tournament/`)
- **Modality**: Implementation from scratch.
- **Entrypoint**: `tally(rows: list[str]) -> str` in [`tournament.py`]
- **Specification**: [`task_1_tournament/README.md`]
- **Test Suite**: [`test_tournament.py`](5 tests).
- **Reference Solution**: [`solution.py`](5/5 pass).

#### Ranking Criteria (Task 1):
1. Total Points (`P`) descending
2. Goal Difference (`GD = GF - GA`) descending
3. Goals For (`GF`) descending
4. Head-to-Head outcome between tied teams
5. Team Name alphabetically ascending

### Task 2: Meeting Room Scheduler (`task_2_meeting_scheduler/`)
- **Modality**: Code comprehension & debugging.
- **Entrypoint**: `MeetingScheduler` in [`scheduler.py`].
- **Specification**: [`task_2_meeting_scheduler/README.md`].
- **Test Suite**: [`test_scheduler.py`] (5 tests).
- **Reference Solution**: [`solution.py`] (annotated bug fixes, 5/5 pass).

---

## Running the Unit Tests
Each task suite can be executed with standard Python without any external dependencies:

```bash
# Task 1
cd task_1_tournament
python test_tournament.py

# Task 2
cd task_2_meeting_scheduler
python test_scheduler.py
```
