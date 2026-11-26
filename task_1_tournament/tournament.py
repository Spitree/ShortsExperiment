def tally(rows: list[str]) -> str:
    """
    Given a list of match score records, return a formatted tournament standings table.

    Each line in `rows` is formatted as: "<Team1>;<Team2>;<Score1>-<Score2>"
    e.g. "Allegheny;Blizzards;3-1"

    Metrics to track per team:
    - MP: Matches Played
    - W:  Matches Won
    - D:  Matches Drawn
    - L:  Matches Lost
    - GF: Goals For (total goals scored)
    - GA: Goals Against (total goals conceded)
    - GD: Goal Difference (GF - GA)
    - P:  Total Points (Win = 3, Draw = 1, Loss = 0)

    Tie-breaking hierarchy:
    1. Points (descending)
    2. Goal Difference (descending)
    3. Goals For (descending)
    4. Head-to-Head outcome between tied teams
    5. Team Name alphabetically (ascending)

    Table format:
    Team                           | MP |  W |  D |  L | GF | GA | GD |  P
    """
    header = "Team                           | MP |  W |  D |  L | GF | GA | GD |  P"
    # TODO: Implement this function
    pass
