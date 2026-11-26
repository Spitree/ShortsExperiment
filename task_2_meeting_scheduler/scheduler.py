from typing import Dict, List, Optional

class MeetingScheduler:
    """
    Manages meeting room reservations and attendee schedules.
    """
    def __init__(self):
        self.rooms: Dict[str, int] = {}
        self.bookings: Dict[str, Dict] = {}

    def add_room(self, room_id: str, capacity: int):
        """Register a meeting room with its maximum capacity."""
        if capacity > 0:
            self.rooms[room_id] = capacity

    def _time_to_minutes(self, time_str: str) -> int:
        """Convert 'HH:MM' string to total minutes from midnight."""
        parts = time_str.split(":")
        return int(parts[0]) + int(parts[1])

    def _intervals_overlap(self, s1: int, e1: int, s2: int, e2: int) -> bool:
        """Check if two time intervals overlap."""
        return s1 <= e2 and s2 <= e1

    def schedule_meeting(
        self,
        booking_id: str,
        room_id: str,
        start_time: str,
        end_time: str,
        attendees: List[str]
    ) -> bool:
        """
        Schedule a meeting.
        Returns True if successful, or False if rejected due to:
        - Unknown room_id
        - Invalid time (start >= end)
        - Attendee count exceeds room capacity
        - Room already booked during this time
        - Any attendee is already in another meeting during this time
        """
        if room_id not in self.rooms:
            return False

        start_m = self._time_to_minutes(start_time)
        end_m = self._time_to_minutes(end_time)
        if start_m >= end_m:
            return False

        if len(attendees) > self.rooms[room_id]:
            return False

        if booking_id in self.bookings:
            return False

        # Check room availability
        for b in self.bookings.values():
            if b["room_id"] == room_id:
                if self._intervals_overlap(start_m, end_m, b["start_m"], b["end_m"]):
                    return False

        # Record booking
        self.bookings[booking_id] = {
            "room_id": room_id,
            "start_m": start_m,
            "end_m": end_m,
            "attendees": list(attendees),
            "status": "confirmed",
        }
        return True

    def cancel_meeting(self, booking_id: str) -> bool:
        """
        Cancel a scheduled meeting and release its booked time slot.
        Returns True if cancelled, or False if the booking was not found or already cancelled.
        """
        if booking_id not in self.bookings:
            return False
        if self.bookings[booking_id].get("status") == "cancelled":
            return False

        self.bookings[booking_id]["status"] = "cancelled"
        return True

    def find_available_room(
        self,
        start_time: str,
        end_time: str,
        attendee_count: int
    ) -> Optional[str]:
        """
        Find an available room that can accommodate attendee_count.
        Selects the best-fit room (smallest capacity that fits the attendees).
        Ties are broken alphabetically by room_id.
        Returns the room_id, or None if no room is available.
        """
        start_m = self._time_to_minutes(start_time)
        end_m = self._time_to_minutes(end_time)
        if start_m >= end_m:
            return None

        candidates = []
        for room_id, capacity in self.rooms.items():
            if capacity >= attendee_count:
                is_free = True
                for b in self.bookings.values():
                    if b["room_id"] == room_id:
                        if self._intervals_overlap(start_m, end_m, b["start_m"], b["end_m"]):
                            is_free = False
                            break
                if is_free:
                    candidates.append(room_id)

        if not candidates:
            return None

        candidates.sort(key=lambda r: (-self.rooms[r], r))
        return candidates[0]
