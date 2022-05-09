"""gestion de base de donnée"""
import os

from tinydb import TinyDB
import shutil
from pathlib import Path
from datetime import datetime


class TinyDBController:
    """gestion des base en TinyDB"""

    def __init__(self, db_file, main_directory):
        """Initialisation de la base TinyDB"""
        self.db_file = db_file
        self.data_base = TinyDB(self.db_file)
        self.main_directory = main_directory

        self.players_table = self.data_base.table('players')
        self.tournaments_table = self.data_base.table('tournaments')
        self.turns_table = self.data_base.table('turns')

    def insert_player(self, player_informations):
        """insert un joueur dans la table players"""
        self.players_table.insert(player_informations)

    def insert_turn(self, turn_informations):
        """insert un tour dans la table turns"""
        self.turns_table.insert(turn_informations)

    def insert_tournament(self, tournament_informations):
        """insert un tournoi dans la table tournament"""
        self.tournaments_table.insert(tournament_informations)

    def get_all_players(self):
        """renvoi la base de joueurs serialisé"""
        return self.players_table.all()

    def get_all_tournaments(self):
        """renvoi la base de joueurs serialisé"""
        return self.tournaments_table.all()

    def get_all_turns(self):
        """renvoi la base de joueurs serialisé"""
        return self.turns_table.all()

    def update_tournaments_table(self, serialized_tournaments_table):
        """met a jour la table des tournois"""
        self.tournaments_table.truncate()
        self.tournaments_table.insert_multiple(serialized_tournaments_table)

    def update_turns_table(self, serialized_turns_table):
        """met a jour la table des tours"""
        self.turns_table.truncate()
        self.turns_table.insert_multiple(serialized_turns_table)

    def update_players_table(self, serialized_players_table):
        """met a jour la table des tours"""
        self.players_table.truncate()
        self.players_table.insert_multiple(serialized_players_table)

    def backup_db_file(self):
        """créer une copie de la base"""
        backup_directory = str(self.main_directory + "\\Backup")

        if not Path(backup_directory).exists():
            os.makedirs(Path(backup_directory))

        file_source = str(self.main_directory + "\\" + self.db_file)
        date_now = datetime.now().strftime("%d%m%Y_%H%M%S")
        file_destination = str(backup_directory + "\\" + date_now + "_" + self.db_file)

        shutil.copyfile(file_source, file_destination)
