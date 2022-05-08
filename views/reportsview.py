"""vue des rapport"""

import os

CHARACTERS_BY_LINE = 95


class ReportView:
    """ affichages globaux du programme"""

    def cls(self):
        """nettoie l'affichage"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_title(self):
        """affiche le bandeau principal du programme"""
        title = "Chess Tournament Manager"
        self.cls()
        self.print_line()
        print("")
        print(title.center(CHARACTERS_BY_LINE))
        print("")
        self.print_line()

    def print_line(self):
        """ affiche une ligne de séparation"""
        line_to_print = ""
        characters_count = 0
        while characters_count < CHARACTERS_BY_LINE:
            line_to_print += "#"
            characters_count += 1
        print(line_to_print)

    def show_pause(self):
        """affiche une pause"""
        input("appuyer sur entrer pour continuer :")

    def show_wrong_response(self, wrong_message_string):
        """affiche si la réponse n'etait pas attendu"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"{wrong_message_string}".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def show_no_info_in_base(self):
        """affiche pas de donnée dans la base"""
        self.main_title()
        print("")
        print("Impossible de charger les rapport !".center(CHARACTERS_BY_LINE))
        print("aucune donnée dans la base !".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    """affichage des rapports"""

    def show_reporting_menu(self):
        """affiche le menu 3 : Rapport"""
        self.main_title()
        print("")
        print("Menu Rapport :")
        print("     1 : Liste de tous les joueurs de la base")
        print("     2 : Liste des joueurs d'un tournoi")
        print("     3 : Liste des tournois")
        print("     4 : Liste des tours d'un tournoi")
        print("     5 : Liste des match d'un tournoi")
        print("     6 : Retour au menu principal")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice

    def prompt_for_sorting_type(self):
        """demande quel type de tri appliquer"""
        self.main_title()
        print("")
        print("Quel type de tri voulez vous appliquer ? : ")
        print("     1 : Par ordre Alphabetique (par défaut)")
        print("     2 : Par ordre de Classement")
        print("")
        self.print_line()
        sort_type = input("Entrez votre choix (1 ou 2) : ") or 1

        return sort_type

    def show_players_reporting_title(self, sort_type):
        """affiche l'en-tête de rapport de tous les joueurs"""
        print("")
        if sort_type == "1":
            print("Liste des joueurs par Ordre Alphabetique".center(CHARACTERS_BY_LINE))
        elif sort_type == "2":
            print("Liste des Joueurs par Classement".center(CHARACTERS_BY_LINE))
        print("")

    def show_tournament_to_report(self, tournament):
        """affiche le nom du tournoi """
        print("")
        print(f"Nom du tournoi : {tournament.tournament_name}".center(CHARACTERS_BY_LINE))
        print("")
        self.print_line()

    def show_tournament_details_reporting(self, tournament):
        """affiche les details d'un tournoi"""
        tournament_dates_string = ""
        for date in tournament.tournament_dates:
            tournament_dates_string += date + ", "
        tournament_dates_string = tournament_dates_string[:-2]

        print("")
        print(f"nom du tournoi : {tournament.tournament_name}")
        print(f"lieu du tournoi : {tournament.tournament_place}")
        print(f"Date(s) du tournoi : {tournament_dates_string}")
        print(f"Nombre de tours : {tournament.turns_number}")
        print(f"Control de Temps : {tournament.time_control}")
        print("")
        self.print_line()

    def show_turn_details_reporting(self, turn):
        """Affiche les détails d'un tour"""
        print("")
        print(f"nom du tour : {turn.turn_name}")
        print(f"Horodatage début : {turn.start_time}")
        print(f"Horodatage fin : {turn.end_time}")
        print("")
        self.print_line()

    def show_match_details_reporting(self, match):
        """affiche les details d'un match"""
        print("")
        print(f"match : {match.player1} contre {match.player2}")
        print(f"    scores {match.player1} : {match.player1_score}")
        print(f"    scores {match.player2} : {match.player2_score}")
        print("")
        self.print_line()

    def show_details_of_player_reporting(self, player):
        """affiche le détails d'un joueur en numérotant les items"""

        date_string = player.date_of_birth.replace("'[]", "")

        print("Informations personnelles du joueur :")
        print("")
        print(f"    Nom de Famille : {player.family_name}")
        print(f"    Prénom : {player.surname}")
        print(f"    Date de naissance : {date_string}")
        print(f"    Sexe : {player.sex}")
        print(f"    Classement : {player.ranking}")
        print("")
        self.print_line()
