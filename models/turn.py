"""Classe de tour"""

from typing import List
from datetime import datetime
from models.match import Match


class Turn:
    """un tour"""

    def __init__(self, turn_number, start_time=None, end_time=None, matches_table=None, index_in_base=0):
        """Initialise un tour"""
        if matches_table is None:
            matches_table = []
        self.turn_name = f"Round {turn_number}"
        self.start_time = start_time
        self.end_time = end_time
        self.matches_table: List[Match] = matches_table
        self.index_in_base = index_in_base

    def start_turn(self):
        """ajoute la date et heure de début"""
        self.start_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def end_turn(self):
        """ajoute la date te l'heure de fin"""
        self.end_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __repr__(self):
        """renvoi l'index de base"""
        return self.index_in_base
