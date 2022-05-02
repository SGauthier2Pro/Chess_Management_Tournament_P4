"""classe de match"""


class Match:
    """un match"""

    def __init__(self, player1, player2, player1_score=0.0, player2_score=0.0):
        """Initialise un match avec ses deux joueurs"""
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def __str__(self):
        return f"([{self.player1.index_in_base},{self.player1_score}]," \
               f"[{self.player2.index_in_base},{self.player2_score}])"

    def __repr__(self):
        match_result = ([self.player1.index_in_base, self.player1_score],
                        [self.player2.index_in_base, self.player2_score])
        return match_result
