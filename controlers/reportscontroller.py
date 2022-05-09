"""classe des rapport"""

from controlers import valuechecker
from views.reportsview import ReportView


class ReportsController:
    """un rapport"""

    def __init__(self):
        """initialisation du rapport avec sa vu"""
        self.view = ReportView()

    def list_players_reporting(self, players_list):
        """affiche tous les joueurs de la base avec leurs informations selon le tri stipulé"""

        sorting_type = self.view.prompt_for_sorting_type()

        if sorting_type == "1":
            self.view.show_players_reporting_title(sorting_type)
            sorted_players = sorted(players_list, key=lambda player: player.family_name)

            for player_to_show in sorted_players:
                self.view.show_details_of_player_reporting(player_to_show)

        elif sorting_type == "2":
            self.view.show_players_reporting_title(sorting_type)
            sorted_players = sorted(players_list, key=lambda player: player.ranking)

            for player_to_show in sorted_players:
                self.view.show_details_of_player_reporting(player_to_show)
        else:
            self.view.show_wrong_response(f"Type de tri : {sorting_type}")

    def list_all_players_in_tournament_reporting(self, tournament_controller):
        """affiche tous les joueurs par ordre alphabetique d'un tournoi"""
        id_tournament_found = False
        while not id_tournament_found:

            tournament_id = tournament_controller.view.show_tournament_choice_menu(
                tournament_controller.tournaments_table
            )

            if valuechecker.is_valid_int(tournament_id):
                for tournament in tournament_controller.tournaments_table:

                    if tournament.index_in_base == int(tournament_id):
                        id_tournament_found = True
                        self.view.print_line()
                        self.view.show_tournament_to_report(tournament)
                        self.list_players_reporting(tournament.tournament_players)

                if not id_tournament_found:
                    tournament_controller.view.show_wrong_tournament_id(tournament_id)
            else:
                self.view.show_wrong_response(tournament_id)

    def list_of_tournaments_reporting(self, tournament_controller):
        """rapport listant tous les tournois de la base avec détails"""
        for tournament in tournament_controller.tournaments_table:
            self.view.show_tournament_details_reporting(tournament)

    def turns_list_of_tournament(self, tournament_controller):
        """rapport listant tous les tours d'un tournoi"""
        id_tournament_found = False
        while not id_tournament_found:

            tournament_id = tournament_controller.view.show_tournament_choice_menu(
                tournament_controller.tournaments_table
            )

            if valuechecker.is_valid_int(tournament_id):
                for tournament in tournament_controller.tournaments_table:
                    if tournament.index_in_base == int(tournament_id):
                        id_tournament_found = True

                        self.view.cls()
                        self.view.print_line()
                        tournament_controller.view.show_tournament_panel(tournament)
                        self.view.print_line()

                        for turn in tournament.tournament_turns:
                            self.view.show_turn_details_reporting(turn)

                if not id_tournament_found:
                    tournament_controller.view.show_wrong_tournament_id(tournament_id)

            else:
                self.view.show_wrong_response(tournament_id)

    def match_list_of_tournament_reporting(self, tournament_controller):
        """rapport listant les matchs d'un tournoi"""
        id_tournament_found = False
        while not id_tournament_found:

            tournament_id = tournament_controller.view.show_tournament_choice_menu(
                tournament_controller.tournaments_table
            )

            if valuechecker.is_valid_int(tournament_id):

                for tournament in tournament_controller.tournaments_table:
                    if tournament.index_in_base == int(tournament_id):
                        id_tournament_found = True

                        self.view.print_line()
                        tournament_controller.view.show_tournament_panel(tournament)

                        for turn in tournament.tournament_turns:
                            self.view.print_line()
                            self.view.show_turn_details_reporting(turn)

                            for match in turn.matches_table:
                                self.view.show_match_details_reporting(match)

                if not id_tournament_found:
                    tournament_controller.view.show_wrong_tournament_id(tournament_id)

            else:
                self.view.show_wrong_response(tournament_id)
