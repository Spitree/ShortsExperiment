import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scheduler import MeetingScheduler

class TestMeetingScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = MeetingScheduler()
        self.scheduler.add_room("Room_A", capacity=6)
        self.scheduler.add_room("Room_B", capacity=12)
        self.scheduler.add_room("Boardroom", capacity=30)

    def test_01_time_parsing_and_valid_meeting_booking(self):
        """
        Test 1: Time conversion and scheduling validation.
        A meeting spanning morning hours (09:30 to 10:15) should be
        properly recognized with start earlier than end, and succeed.
        """
        ok = self.scheduler.schedule_meeting(
            booking_id="meet_1",
            room_id="Room_A",
            start_time="09:30",
            end_time="10:15",
            attendees=["Alice", "Bob"]
        )
        self.assertTrue(ok, "Meeting from 09:30 to 10:15 should be scheduled successfully.")
        self.assertIn("meet_1", self.scheduler.bookings)

    def test_02_back_to_back_meetings_in_same_room(self):
        """
        Test 2: Interval overlap boundary condition.
        Back-to-back meetings in the same room (one ending at 11:00, next starting at 11:00)
        do not overlap and both should be permitted.
        """
        ok1 = self.scheduler.schedule_meeting(
            booking_id="meet_morning",
            room_id="Room_A",
            start_time="10:00",
            end_time="11:00",
            attendees=["Alice"]
        )
        self.assertTrue(ok1)

        ok2 = self.scheduler.schedule_meeting(
            booking_id="meet_midday",
            room_id="Room_A",
            start_time="11:00",
            end_time="12:00",
            attendees=["Charlie"]
        )
        self.assertTrue(ok2, "Back-to-back meeting starting exactly when previous ends should succeed.")

    def test_03_attendee_conflict_across_different_rooms(self):
        """
        Test 3: Attendee schedule conflict across rooms.
        An attendee cannot be in two overlapping meetings simultaneously,
        even if they are scheduled in different rooms.
        """
        ok1 = self.scheduler.schedule_meeting(
            booking_id="eng_standup",
            room_id="Room_A",
            start_time="14:00",
            end_time="15:00",
            attendees=["Dave", "Eve"]
        )
        self.assertTrue(ok1)

        # Dave is already in eng_standup from 14:00 to 15:00
        ok2 = self.scheduler.schedule_meeting(
            booking_id="client_sync",
            room_id="Room_B",
            start_time="14:30",
            end_time="15:30",
            attendees=["Dave", "Frank"]
        )
        self.assertFalse(ok2, "Should reject booking because Dave has a conflicting meeting.")

    def test_04_best_fit_room_recommendation(self):
        """
        Test 4: Best-fit room allocation.
        When requesting a room for 4 people, it should select the smallest
        available room that can hold them (Room_A: cap 6, rather than Boardroom: cap 30).
        """
        chosen_room = self.scheduler.find_available_room(
            start_time="16:00",
            end_time="17:00",
            attendee_count=4
        )
        self.assertEqual(
            chosen_room,
            "Room_A",
            "Should recommend the best-fit (smallest capacity) room that fits the attendees."
        )

    def test_05_cancellation_frees_room_for_new_booking(self):
        """
        Test 5: Meeting cancellation cleanup.
        Cancelling a meeting must free the room so a new meeting can be booked
        in that same room and time slot.
        """
        ok1 = self.scheduler.schedule_meeting(
            booking_id="client_pitch",
            room_id="Room_B",
            start_time="13:00",
            end_time="14:00",
            attendees=["Grace", "Heidi"]
        )
        self.assertTrue(ok1)

        # Cancel the meeting
        cancelled = self.scheduler.cancel_meeting("client_pitch")
        self.assertTrue(cancelled)

        # Room_B should now be free to book a new meeting at 13:00-14:00
        ok2 = self.scheduler.schedule_meeting(
            booking_id="internal_sync",
            room_id="Room_B",
            start_time="13:00",
            end_time="14:00",
            attendees=["Ivan", "Judy"]
        )
        self.assertTrue(ok2, "Room should be available after the conflicting meeting was cancelled.")

if __name__ == "__main__":
    unittest.main()
