"""classe controller"""

from controlers.tournamentcontroller import TournamentController
from controlers.playercontroller import PlayerController
from controlers.turncontroller import TurnController
from controlers.reportscontroller import ReportsController


NUMBER_OF_PLAYERS = 8
DEFAULT_TURNS_NUMBER_IN_TOURNAMENT = 4


class MainController:
    """controller principal du programme"""

    def __init__(self, data_base, main_view, tournament_view, player_view):
        """Initialise le programme avec la gestion de bas de donnée, les models et la vue"""
        self.data_base = data_base
        self.view = main_view
        self.tournament_view = tournament_view
        self.player_view = player_view

        self.serialized_players_from_db = self.data_base.get_all_players()
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()
        self.serialized_turns_from_db = self.data_base.get_all_turns()

        self.player_controller = PlayerController(
            self.player_view,
            self.data_base
        )

        self.turn_controller = TurnController(
            self.view,
            self.data_base,
            self.player_controller
        )

        self.tournament_controller = TournamentController(
            self.tournament_view,
            self.data_base,
            self.player_controller,
            self.turn_controller
        )

        self.reports_controller = ReportsController()

        self.active_tournament = None
        self.active_turn = None

    def run(self):
        """lancement du programme"""

        main_menu_response = ""

        while main_menu_response != "sortir du programme":

            main_menu_response = self.view.show_main_menu()

            if main_menu_response == "1":
                """menu 1 : Tournoi"""
                tournament_menu_response = ""

                while tournament_menu_response != "4":
                    tournament_menu_response = self.tournament_controller.view.show_tournament_menu(
                        self.tournament_controller.active_tournament
                    )

                    if tournament_menu_response == "1":
                        """Menu 1.1 Creer un tournoi"""
                        if self.player_controller.players_table:
                            if len(self.player_controller.players_table) >= NUMBER_OF_PLAYERS:
                                self.tournament_controller.active_tournament = \
                                    self.tournament_controller.create_new_tournament(
                                        self.player_controller
                                    )
                            else:
                                self.player_controller.view.show_not_enough_players()
                        else:
                            self.player_controller.view.show_no_player_in_base()

                    elif tournament_menu_response == "2":
                        """menu 1.2: charger un tournoi"""
                        if self.tournament_controller.tournaments_table:
                            self.tournament_controller.active_tournament = self.tournament_controller.load_tournament()

                        else:
                            self.tournament_controller.view.show_no_tournament_in_base()

                    elif tournament_menu_response == "3":
                        """menu 1.3: Saisir des resultats"""
                        if self.tournament_controller.active_tournament is not None:
                            self.tournament_controller.run_tournament(
                                self.tournament_controller.active_tournament,
                                self.turn_controller
                            )
                        else:
                            self.tournament_controller.view.show_no_active_tournament()

                    elif tournament_menu_response == "4":
                        pass

                    else:
                        self.view.show_wrong_response(tournament_menu_response)

            elif main_menu_response == "2":
                """menu 2 : Gestion des joueurs"""

                player_menu_response = ""

                while player_menu_response != "3":

                    player_menu_response = self.player_controller.view.show_players_menu()

                    if player_menu_response == "1":
                        """menu 2.1 : Entrer un nouveau joueur"""

                        self.player_controller.create_new_player()

                    elif player_menu_response == "2":
                        """menu 2.2 : Mise à jour d'un joueur"""

                        if self.player_controller.players_table:

                            self.player_controller.update_player()

                        else:
                            self.player_controller.view.show_no_player_in_base()

                    elif player_menu_response == "3":
                        pass

                    else:
                        self.view.show_wrong_response(player_menu_response)

            elif main_menu_response == "3":
                """Menu 3 : Rapport"""
                if self.tournament_controller.tournaments_table or self.player_controller.players_table:
                    reporting_menu_response = ""

                    while reporting_menu_response != "6":

                        reporting_menu_response = self.reports_controller.view.show_reporting_menu()

                        if reporting_menu_response == "1":
                            """3.1 : Liste de tous les joueurs de la base"""
                            if self.player_controller.players_table:
                                self.reports_controller.list_players_reporting(
                                    self.player_controller.players_table
                                )
                                self.view.show_pause()
                            else:
                                self.player_controller.view.show_no_player_in_base()

                        elif reporting_menu_response == "2":
                            """3.2 : Liste des joueurs d'un tournoi"""
                            if self.tournament_controller.tournaments_table:
                                self.reports_controller.list_all_players_in_tournament_reporting(
                                    self.tournament_controller
                                )
                                self.view.show_pause()
                            else:
                                self.tournament_controller.view.show_no_tournament_in_base()

                        elif reporting_menu_response == "3":
                            """3 : Liste des tournois"""
                            if self.tournament_controller.tournaments_table:
                                self.view.main_title()
                                self.reports_controller.list_of_tournaments_reporting(self.tournament_controller)
                                self.view.show_pause()
                            else:
                                self.tournament_controller.view.show_no_tournament_in_base()

                        elif reporting_menu_response == "4":
                            """4 : Liste des tours d'un tournoi"""
                            if self.tournament_controller.tournaments_table:
                                self.view.main_title()
                                self.reports_controller.turns_list_of_tournament(self.tournament_controller)
                                self.view.show_pause()
                            else:
                                self.tournament_controller.view.show_no_tournament_in_base()

                        elif reporting_menu_response == "5":
                            """5 : Liste des match d'un tournoi"""
                            if self.tournament_controller.tournaments_table:
                                self.view.main_title()
                                self.reports_controller.match_list_of_tournament_reporting(self.tournament_controller)
                                self.view.show_pause()
                            else:
                                self.tournament_controller.view.show_no_tournament_in_base()

                        elif reporting_menu_response == "6":
                            pass

                        else:
                            self.view.show_wrong_response(reporting_menu_response)
                else:
                    self.reports_controller.view.show_no_info_in_base()

            elif main_menu_response == "4":
                """Menu 4 : Sortie du programme"""
                exit_response = self.view.show_exit_menu()

                if exit_response == "1":
                    self.data_base.backup_db_file()
                    main_menu_response = "sortir du programme"

                elif exit_response == "2":
                    pass
                else:
                    self.view.show_wrong_response(exit_response)
            else:
                """reponse non valide"""
                self.view.show_wrong_response(main_menu_response)
