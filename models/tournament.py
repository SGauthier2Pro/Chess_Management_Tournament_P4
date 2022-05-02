"""classe de tournois"""

from typing import List

from models.player import Player
from models.turn import Turn

TIME_CONTROL = ['Bullet',
                'Blitz',
                'Coup Rapide'
                ]


class Tournament:
    """un tournoi"""

    def __init__(self,
                 tournament_name,
                 tournament_place,
                 tournament_dates,
                 turns_number,
                 index_in_base=0,
                 tournament_description=None,
                 time_control=None):
        """Initialise un tournoi"""
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_dates = []
        for date in tournament_dates:
            self.tournament_dates.append(date)
        self.turns_number = turns_number
        self.tournament_turns: List[Turn] = []
        self.tournament_players: List[Player] = []
        self.index_in_base = index_in_base
        self.tournament_description = tournament_description
        self.time_control = time_control
