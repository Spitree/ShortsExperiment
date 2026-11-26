import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tournament import tally

class TestTournament(unittest.TestCase):
    HEADER = "Team                           | MP |  W |  D |  L | GF | GA | GD |  P"

    def test_01_empty_input_returns_header_only(self):
        """Test 1 (Warm-up / Baseline): Empty input returns only the header."""
        expected = self.HEADER
        self.assertEqual(tally([]), expected)

    def test_02_single_match_score_and_goal_differential(self):
        """Test 2: Single match with goal scoring and differential calculation."""
        rows = ["Allegheny;Blizzards;3-1"]
        expected = "\n".join([
            self.HEADER,
            "Allegheny                      |  1 |  1 |  0 |  0 |  3 |  1 |  2 |  3",
            "Blizzards                      |  1 |  0 |  0 |  1 |  1 |  3 | -2 |  0",
        ])
        self.assertEqual(tally(rows), expected)

    def test_03_tie_breaking_by_goal_difference_and_goals_scored(self):
        """
        Test 3: Teams tied on points should be ranked by Goal Difference (GD),
        then by Goals For (GF).
        """
        rows = [
            "Allegheny;Courage;2-1",  # Allegheny: P=3, GF=2, GA=1, GD=+1
            "Blizzards;Devils;3-0",   # Blizzards: P=3, GF=3, GA=0, GD=+3
        ]
        # Blizzards (GD +3) ranks above Allegheny (GD +1)
        # Courage (GD -1) ranks above Devils (GD -3)
        expected = "\n".join([
            self.HEADER,
            "Blizzards                      |  1 |  1 |  0 |  0 |  3 |  0 |  3 |  3",
            "Allegheny                      |  1 |  1 |  0 |  0 |  2 |  1 |  1 |  3",
            "Courage                        |  1 |  0 |  0 |  1 |  1 |  2 | -1 |  0",
            "Devils                         |  1 |  0 |  0 |  1 |  0 |  3 | -3 |  0",
        ])
        self.assertEqual(tally(rows), expected)

    def test_04_head_to_head_tie_breaker(self):
        """
        Test 4: When two teams have identical Points, GD, and GF,
        their head-to-head match outcome breaks the tie.
        """
        rows = [
            "Alpha;Beta;1-0",   # Alpha defeats Beta
            "Alpha;Gamma;0-1",  # Gamma defeats Alpha
            "Beta;Delta;1-0",   # Beta defeats Delta
        ]
        # Alpha: MP 2, W 1, L 1, GF 1, GA 1, GD 0, P 3
        # Beta:  MP 2, W 1, L 1, GF 1, GA 1, GD 0, P 3
        # Tied on P(3), GD(0), GF(1). Alpha beat Beta in their direct match -> Alpha ranks above Beta!
        # Gamma: MP 1, W 1, L 0, GF 1, GA 0, GD +1, P 3 -> 1st place on GD(+1)
        # Delta: MP 1, W 0, L 1, GF 0, GA 1, GD -1, P 0 -> 4th place
        expected = "\n".join([
            self.HEADER,
            "Gamma                          |  1 |  1 |  0 |  0 |  1 |  0 |  1 |  3",
            "Alpha                          |  2 |  1 |  0 |  1 |  1 |  1 |  0 |  3",
            "Beta                           |  2 |  1 |  0 |  1 |  1 |  1 |  0 |  3",
            "Delta                          |  1 |  0 |  0 |  1 |  0 |  1 | -1 |  0",
        ])
        self.assertEqual(tally(rows), expected)

    def test_05_multi_team_tournament_with_complex_standings(self):
        """Test 5: Full 4-team tournament with mixed outcomes and secondary ranking."""
        rows = [
            "Allegheny;Blizzards;2-1",
            "Courage;Devils;1-1",
            "Devils;Allegheny;0-2",
            "Blizzards;Courage;3-0",
            "Allegheny;Courage;1-2",
            "Blizzards;Devils;2-2",
        ]
        expected = "\n".join([
            self.HEADER,
            "Allegheny                      |  3 |  2 |  0 |  1 |  5 |  3 |  2 |  6",
            "Blizzards                      |  3 |  1 |  1 |  1 |  6 |  4 |  2 |  4",
            "Courage                        |  3 |  1 |  1 |  1 |  3 |  5 | -2 |  4",
            "Devils                         |  3 |  0 |  2 |  1 |  3 |  5 | -2 |  2",
        ])
        self.assertEqual(tally(rows), expected)

if __name__ == "__main__":
    unittest.main()
