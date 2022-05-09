"""classe tournament_manager"""

from models.tournament import Tournament, TIME_CONTROL
from controlers import valuechecker

NUMBER_OF_PLAYERS = 8
DEFAULT_TURNS_NUMBER_IN_TOURNAMENT = 4


def create_tournament(serialized_tournament,
                      player_controller=None,
                      turn_controller=None
                      ):
    """crée un tournoi a partir des données serialisé"""
    if type(serialized_tournament) is dict:
        index_in_base = 0
    else:
        index_in_base = serialized_tournament.doc_id

    active_tournament = Tournament(
        serialized_tournament['tournament_name'],
        serialized_tournament['tournament_place'],
        serialized_tournament['tournament_date'],
        serialized_tournament['turns_number'],
        index_in_base=index_in_base,
        tournament_description=serialized_tournament['tournament_description'],
        time_control=serialized_tournament['time_control']
    )

    if (player_controller is not None) and (turn_controller is not None):

        """récupère les objets joueur du tournoi"""
        if serialized_tournament['tournament_players']:
            for player_id in serialized_tournament['tournament_players']:
                for player_from_db in player_controller.players_table:
                    if player_from_db.index_in_base == player_id:
                        active_tournament.tournament_players.append(player_from_db)

        """récupère les objets tour du tournoi"""
        if serialized_tournament['tournament_turns']:
            for turn_id in serialized_tournament['tournament_turns']:
                for turn_from_db in turn_controller.turns_table:
                    if turn_from_db.index_in_base == turn_id:
                        active_tournament.tournament_turns.append(turn_from_db)

    return active_tournament


class TournamentController:
    """Tournament Manager"""

    def __init__(self, view, data_base, player_controller, turn_controller):
        """initialistation du manager de tournoi avec vue"""

        self.view = view
        self.data_base = data_base
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()

        self.tournaments_table = []

        for tournament in self.serialized_tournaments_from_db:
            self.tournaments_table.append(create_tournament(tournament, player_controller, turn_controller))

        self.active_tournament = None

    """Methodes Tournoi"""

    def create_new_tournament(self, player_controller):
        """crée un tournoi en base"""

        """saisie des données de tournoi"""
        tournament_creation_display = {}
        tournament_informations = {}
        tournament_informations_completed = False

        while not tournament_informations_completed:

            tournament_name_done = False
            while not tournament_name_done:
                self.view.show_create_tournament_prompt(tournament_creation_display)

                tournament_name = self.view.prompt_tournament_name()
                confirmation = self.view.prompt_confirmation(tournament_name)
                if confirmation == "o":
                    tournament_informations['tournament_name'] = tournament_name
                    tournament_creation_display['Nom du tournoi'] = tournament_name
                    tournament_name_done = True
                    tournament_informations_completed = True
                else:
                    tournament_informations_completed = False

            tournament_place_done = False
            while not tournament_place_done:
                self.view.show_create_tournament_prompt(tournament_creation_display)

                tournament_place = self.view.prompt_tournament_place()
                confirmation = self.view.prompt_confirmation(tournament_place)
                if confirmation == "o":
                    tournament_informations['tournament_place'] = tournament_place
                    tournament_creation_display['Lieu du Tournoi'] = tournament_place
                    tournament_place_done = True
                    tournament_informations_completed = True
                else:
                    tournament_informations_completed = False

            tournament_date_done = False
            while not tournament_date_done:
                dates = []
                dates_string = ""
                another_date = True

                while another_date:
                    self.view.show_create_tournament_prompt(tournament_creation_display)
                    date_answer = self.view.prompt_tournament_date()
                    if valuechecker.is_valid_date(date_answer):
                        if not valuechecker.compare_dates(dates, date_answer):
                            dates.append(date_answer)
                            confirmation = self.view.prompt_confirmation(date_answer)
                            if confirmation == "o":
                                tournament_informations['tournament_date'] = dates
                                for date in dates:
                                    dates_string = str(date) + ","
                                tournament_creation_display['Date(s) du Tournoi'] = dates_string[:-1]
                            another_date_answer = self.view.prompt_another_tournament_date()
                            if another_date_answer == "n":
                                another_date = False
                                tournament_date_done = True
                                tournament_informations_completed = True
                            else:
                                tournament_informations_completed = False
                        else:
                            self.view.show_wrong_response(f"Date : {date_answer} déja saisie pour ce tournoi !")
                    else:
                        self.view.show_wrong_date(date_answer)

            turns_number_done = False
            while not turns_number_done:
                self.view.show_create_tournament_prompt(tournament_creation_display)

                turns_number = self.view.prompt_tournament_turns_number()

                if turns_number == "":
                    turns_number = DEFAULT_TURNS_NUMBER_IN_TOURNAMENT

                if valuechecker.is_valid_int(turns_number):
                    confirmation = self.view.prompt_confirmation(turns_number)
                    if confirmation == "o":
                        tournament_informations['turns_number'] = turns_number
                        tournament_creation_display['Nombre de tours'] = turns_number
                        turns_number_done = True
                        tournament_informations_completed = True
                    else:
                        tournament_informations_completed = False
                else:
                    self.view.show_wrong_turn_number(turns_number)

            tournament_description_done = False
            while not tournament_description_done:
                self.view.show_create_tournament_prompt(tournament_creation_display)

                tournament_description = self.view.prompt_tournament_description()
                confirmation = self.view.prompt_confirmation(tournament_description)
                if confirmation == "o":
                    tournament_informations['tournament_description'] = tournament_description
                    tournament_creation_display['Description'] = tournament_description
                    tournament_description_done = True
                    tournament_informations_completed = True
                else:
                    tournament_informations_completed = False

            time_control_done = False
            while not time_control_done:
                self.view.show_create_tournament_prompt(tournament_creation_display)

                time_control = self.view.prompt_tournament_time_control(TIME_CONTROL)
                if valuechecker.is_valid_int(time_control):
                    if int(time_control) < len(TIME_CONTROL):
                        confirmation = self.view.prompt_confirmation(time_control)
                        if confirmation == "o":
                            tournament_informations['time_control'] = TIME_CONTROL[int(time_control)]
                            time_control_done = True
                            tournament_informations_completed = True
                        else:
                            tournament_informations_completed = False

                    else:
                        tournament_informations_completed = False
                else:
                    self.view.show_wrong_time_control(time_control)

            if tournament_informations_completed:

                created_tournament = create_tournament(tournament_informations)

                """récupérer la liste des joueur du tournoi"""
                tournaments_players_to_add = self.add_player_in_tournament(player_controller)

                for player in tournaments_players_to_add:
                    created_tournament.tournament_players.append(player)

                self.tournaments_table.append(created_tournament)
                self.save_tournaments()
                created_tournament.index_in_base = self.serialized_tournaments_from_db[-1].doc_id

                return created_tournament

    def add_player_in_tournament(self, player_controller):
        """ajout des joueurs dans la liste pour le tournoi"""
        all_players = player_controller.players_table
        players_list_to_add = []

        player_number = 0

        while player_number < NUMBER_OF_PLAYERS:

            self.view.main_title()
            player_controller.view.show_players_list(all_players)
            self.view.show_player_in_tournament(players_list_to_add)

            id_player = self.view.prompt_for_add_player()

            for player_to_test in all_players:
                if player_to_test not in players_list_to_add:
                    if player_to_test.index_in_base == int(id_player):
                        players_list_to_add.append(player_to_test)
                        all_players.pop(all_players.index(player_to_test))
                        player_number += 1

        self.view.main_title()
        player_controller.view.show_players_list(all_players)
        self.view.show_player_in_tournament(players_list_to_add)
        self.view.show_pause()

        return players_list_to_add

    def load_tournament(self):
        """charge un tournoi par son ID de base"""

        tournament_id = self.view.show_tournament_choice_menu(
            self.tournaments_table)

        active_tournament = None

        for tournament in self.tournaments_table:
            if tournament.index_in_base == int(tournament_id):
                """récupère l'objet tournoi"""
                active_tournament = tournament

                """réaffecte les point des joueurs du tournoi"""
                for player in active_tournament.tournament_players:
                    player.total_points = self.get_player_total_points(player, active_tournament)

        return active_tournament

    def save_tournaments(self):
        """ajoute le tournoi au tableau de tournoi"""
        serialized_tournaments = []

        for tournament in self.tournaments_table:
            tournament_id_players_list = []
            tournament_id_turns_list = []

            for player in tournament.tournament_players:
                tournament_id_players_list.append(player.index_in_base)

            for turn in tournament.tournament_turns:
                tournament_id_turns_list.append(turn.index_in_base)

            serialized_tournament = {
                'tournament_name': tournament.tournament_name,
                'tournament_place': tournament.tournament_place,
                'tournament_date': tournament.tournament_dates,
                'turns_number': tournament.turns_number,
                'tournament_turns': tournament_id_turns_list,
                'tournament_players': tournament_id_players_list,
                'tournament_description': tournament.tournament_description,
                'time_control': tournament.time_control
            }

            serialized_tournaments.append(serialized_tournament)

        self.data_base.update_tournaments_table(serialized_tournaments)
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()

    def get_tournament_result(self, tournament):
        """calcul des resultat du tournoi"""
        results_table = []
        for player in tournament.tournament_players:
            results_table.append(f"{player} : {self.get_player_total_points(player, tournament)}")
        self.view.show_tournament_results(results_table, tournament)

    def get_player_total_points(self, player, tournament):
        """renvoi le nombre total de point d'un joueur sur le tournoi"""
        total_points = 0.0
        for turn in tournament.tournament_turns:
            for match in turn.matches_table:
                if match.player1 == player:
                    total_points += match.player1_score
                if match.player2 == player:
                    total_points += match.player2_score

        return total_points

    def run_tournament(self, active_tournament, turn_controller):
        """lance le tournoi"""
        self.active_tournament = active_tournament

        turn_number = len(self.active_tournament.tournament_turns)

        if turn_number != 0:
            for turn in self.active_tournament.tournament_turns:

                if (turn.start_time is not None) and (turn.end_time is None):
                    turn_controller.active_turn = turn
                    turn_number -= 1

                elif (turn.start_time is None) and (turn.end_time is None):
                    turn_controller.active_turn = turn
                    turn_number -= 1

        if turn_number == 4:
            self.view.show_tournament_terminated(self.active_tournament)

        while turn_number < int(self.active_tournament.turns_number):
            if turn_controller.active_turn is None:
                turn_number_name = turn_number + 1
                turn_controller.active_turn = turn_controller.create_new_turn(
                    turn_number_name,
                    self.active_tournament
                )

                """mise a jour de la table des instance ronde de l'objet tournoi"""
                self.active_tournament.tournament_turns.append(turn_controller.active_turn)

            turn_number = len(self.active_tournament.tournament_turns)

            if turn_controller.active_turn.start_time is None:
                self.view.show_tournament_management_menu(self.active_tournament)
                start_turn_response = self.view.prompt_start_turn(turn_controller.active_turn)

                if start_turn_response == "o":
                    """demarrer le tour"""
                    turn_controller.active_turn.start_turn()
                    self.view.show_turn_started(turn_controller.active_turn)

                else:
                    turn_controller.save_turns()
                    self.save_tournaments()
                    break

            if turn_controller.active_turn.start_time is not None:
                self.view.show_tournament_management_menu(self.active_tournament)
                enter_turn_result = self.view.prompt_enter_turn_results(turn_controller.active_turn)

                if enter_turn_result == "o":
                    """entrer des resultat de chaque match"""
                    for match in turn_controller.active_turn.matches_table:
                        self.view.show_tournament_management_menu(self.active_tournament)
                        winner = self.view.prompt_who_is_match_winner(match, turn_controller.active_turn)

                        turn_controller.set_match_result(match, winner)

                    turn_controller.active_turn.end_turn()
                    turn_controller.save_turns()

                    self.save_tournaments()

                    self.view.show_pause()

                    turn_controller.active_turn = None

                    if turn_number == 4:
                        self.get_tournament_result(self.active_tournament)

                else:
                    turn_controller.save_turns()
                    self.save_tournaments()
                    break
