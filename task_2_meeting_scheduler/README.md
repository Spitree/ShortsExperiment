# Coding Task 2: Meeting Room Scheduler

## Background
You are taking over maintenance of a meeting room reservation module ([`scheduler.py`](file:///c:/Users/filip/OneDrive/Desktop/tasks/task_2_meeting_scheduler/scheduler.py)). The `MeetingScheduler` class coordinates conference room bookings, verifies attendee schedules, and handles meeting cancellations.

A recent update introduced several logic defects, and the test suite ([`test_scheduler.py`](file:///c:/Users/filip/OneDrive/Desktop/tasks/task_2_meeting_scheduler/test_scheduler.py)) currently fails across all 5 test scenarios.

Your goal is to inspect the test suite and codebase, diagnose where the implementation deviates from the system specification below, and fix the bugs in `scheduler.py` until all **5 unit tests pass**.

---

## System Specification

### 1. Time Representation & Validation
- Times are represented as `"HH:MM"` strings (e.g., `"09:30"`, `"14:00"`).
- A valid meeting must have a start time strictly earlier than its end time (`start < end`).
- Back-to-back meetings are permitted: a meeting ending at 11:00 and another starting at 11:00 in the same room do **not** conflict.

### 2. Room & Attendee Scheduling (`schedule_meeting`)
- `schedule_meeting(booking_id, room_id, start_time, end_time, attendees) -> bool`:
  - Returns `False` if `room_id` is unknown, if times are invalid, or if the number of attendees exceeds the room's maximum capacity.
  - Returns `False` if the room is already booked for any overlapping time interval.
  - Returns `False` if **any attendee** is already participating in an overlapping meeting during this time (attendees cannot be double-booked, even across different rooms).
  - If all constraints are satisfied, books the meeting and returns `True`.

### 3. Room Recommendations (`find_available_room`)
- `find_available_room(start_time, end_time, attendee_count) -> str | None`:
  - Returns the `room_id` of the **best-fit room** (the smallest capacity room that can accommodate `attendee_count` and is free during the requested time window).
  - If multiple available rooms share the same smallest capacity, ties are broken alphabetically by `room_id`.
  - Returns `None` if no suitable room is available.

### 4. Meeting Cancellations (`cancel_meeting`)
- `cancel_meeting(booking_id) -> bool`:
  - Cancels the meeting and immediately frees both the room and all attendees for that time window.
  - Returns `True` if cancelled, or `False` if the booking was not found or was already cancelled.

---

## Running the Tests
To run the test suite:
```bash
python test_scheduler.py
```
There are **5 unit tests**. All 5 must pass for the task to be complete.
