"""classe controller"""

import datetime

from models.player import Player
from models.match import Match
from models.turn import Turn
from models.tournament import Tournament, TIME_CONTROL


NUMBER_OF_PLAYERS = 8
DEFAULT_TURNS_NUMBER_IN_TOURNAMENT = 4


class Controller:
    """controller principal du programme"""

    def __init__(self, data_base, view, match_management, report):
        """Initialise le programme avec la gestion de bas de donnée, les models et la vue"""
        self.data_base = data_base
        self.view = view
        self.match_management = match_management
        self.report = report

        self.serialized_players_from_db = self.data_base.get_all_players()
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()
        self.serialized_turns_from_db = self.data_base.get_all_turns()

        self.active_tournament = None
        self.active_turn = None

    def is_valid_date(self, date_to_test):
        """methode de test de date renvoi True ou False"""
        year = 0
        month = 0
        day = 0
        is_valid_date = True

        try:
            day, month, year = date_to_test.split('/')
        except ValueError:
            is_valid_date = False

        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            is_valid_date = False

        return is_valid_date

    """ methodes joueurs"""

    def add_player_in_db(self):
        """ajoute un joueur a la base de joueur"""
        wrong_message_string = ""

        is_valid_information = True

        serialized_player = self.view.prompt_add_player_in_db()

        if not self.is_valid_date(serialized_player['date_of_birth']):
            is_valid_information = False
            wrong_message_string += f"Date de naissance : {serialized_player['date_of_birth']} \n"

        if serialized_player['sex'] not in ["M", "F"]:
            is_valid_information = False
            wrong_message_string += f"Sexe : {serialized_player['sex']} \n"

        try:
            serialized_player['ranking'] = int(serialized_player['ranking'])
        except ValueError:
            is_valid_information = False
            wrong_message_string += f"Classement : {serialized_player['ranking']} \n"

        if is_valid_information:
            self.data_base.insert_player(serialized_player)
            self.serialized_players_from_db = self.data_base.get_all_players()
        else:
            self.view.show_wrong_response(wrong_message_string)

    def add_player_in_tournament(self, all_players):
        """ajout des joueur dans la liste pour le tournoi"""
        players_list_to_add_in_tournament = []
        temporary_player_indexes_list = []

        player_number = 0

        while player_number < NUMBER_OF_PLAYERS:

            self.view.main_title()
            self.view.show_players_list(all_players)
            self.view.show_player_in_tournament(players_list_to_add_in_tournament)

            id_player = self.view.prompt_for_add_player()

            for player_to_test in all_players:
                if player_to_test.doc_id not in temporary_player_indexes_list:
                    if player_to_test.doc_id == id_player:
                        player = Player(player_to_test["family_name"],
                                        player_to_test['surname'],
                                        player_to_test['date_of_birth'],
                                        player_to_test['sex'],
                                        player_to_test['ranking'],
                                        player_to_test.doc_id,
                                        player_to_test['total_points']
                                        )

                        players_list_to_add_in_tournament.append(player)
                        temporary_player_indexes_list.append(player_to_test.doc_id)
                        all_players.pop(all_players.index(player_to_test))
                        player_number += 1

        self.view.main_title()
        self.view.show_players_list(all_players)
        self.view.show_player_in_tournament(players_list_to_add_in_tournament)
        self.view.show_pause()

        return players_list_to_add_in_tournament

    def get_player_total_points(self, player, tournament):
        """renvoi le nombre total de point d'un joureur sur le tournoi"""
        total_points = 0.0
        for turn in tournament.tournament_turns:
            for match in turn.matches_table:
                if match.player1 == player:
                    total_points += match.player1_score
                if match.player2 == player:
                    total_points += match.player2_score

        return total_points

    def update_player_item_in_table(self, serialized_player_to_update, item_to_modify):
        """met a jour un item de joueur et remet a jour la base et la table"""

        must_be_update = False

        for serialized_player in self.serialized_players_from_db:

            if serialized_player.doc_id == serialized_player_to_update.doc_id:

                if item_to_modify != "6":
                    updated_information = self.view.prompt_information_to_update()

                    if item_to_modify == "1":
                        serialized_player['family_name'] = updated_information
                        must_be_update = True

                    elif item_to_modify == "2":
                        serialized_player['surname'] = updated_information
                        must_be_update = True

                    elif item_to_modify == "3":

                        if self.is_valid_date(updated_information):
                            serialized_player['date_of_birth'] = updated_information
                            must_be_update = True

                        else:
                            self.view.show_wrong_response(f"Date de Naissance : {updated_information}\n")
                            break

                    elif item_to_modify == "4":
                        if updated_information in ["M", "F"]:
                            serialized_player['sex'] = updated_information
                            must_be_update = True

                        else:
                            self.view.show_wrong_response(f"Sexe : {updated_information}\n")
                            break

                    elif item_to_modify == "5":
                        try:
                            serialized_player['ranking'] = int(updated_information)
                            must_be_update = True

                        except ValueError:
                            self.view.show_wrong_response(f"Classement : {updated_information}\n")

                            break
                else:
                    break

                if must_be_update:
                    self.data_base.update_players_table(self.serialized_players_from_db)
                    self.serialized_players_from_db = self.data_base.get_all_players()
                    return 0

    """Methodes Tournoi"""

    def create_tournament(self, tournament_informations):
        """crée un tournoi """
        index_time_control = int(tournament_informations['time_control']) - 1

        if tournament_informations['turns_number'] == "":
            tournament_informations['turns_number'] = DEFAULT_TURNS_NUMBER_IN_TOURNAMENT

        tournament_dates_string = (tournament_informations['tournament_date'])[:-1]
        tournament_dates = tournament_dates_string.split(",")

        created_tournament = Tournament(tournament_informations['tournament_name'],
                                        tournament_informations['tournament_place'],
                                        tournament_dates,
                                        tournament_informations['turns_number'],
                                        tournament_description=tournament_informations['tournament_description'],
                                        time_control=TIME_CONTROL[index_time_control])

        return created_tournament

    def load_tournament(self, tournament_id):
        """charge un tournoi par son ID de base"""

        active_tournament = None

        for tournament in self.serialized_tournaments_from_db:
            if tournament.doc_id == int(tournament_id):
                """crée l'objet tournoi"""
                active_tournament = Tournament(tournament['tournament_name'],
                                               tournament['tournament_place'],
                                               tournament['tournament_date'],
                                               tournament['turns_number'],
                                               index_in_base=tournament_id,
                                               tournament_description=tournament['tournament_description'],
                                               time_control=tournament['time_control'])

                """crée les objets joueur du tournoi"""
                for player_id in tournament['tournament_players']:
                    for player_from_db in self.serialized_players_from_db:
                        if player_from_db.doc_id == player_id:
                            active_tournament.tournament_players.append(Player(player_from_db['family_name'],
                                                                               player_from_db['surname'],
                                                                               player_from_db['date_of_birth'],
                                                                               player_from_db['sex'],
                                                                               player_from_db['ranking'],
                                                                               player_from_db.doc_id)
                                                                        )

                """crée les objets tour du tournoi"""
                turn_number = 1
                for turn in tournament['tournament_turns']:
                    for serialized_turn in self.serialized_turns_from_db:
                        if turn == serialized_turn.doc_id:
                            turn_to_add = self.load_turn(turn_number, serialized_turn, active_tournament)
                            active_tournament.tournament_turns.append(turn_to_add)
                            turn_number += 1

                """réaffecte les point des joueurs du tournoi"""
                for player in active_tournament.tournament_players:
                    player.total_points = self.get_player_total_points(player, active_tournament)

        return active_tournament

    def add_tournament_in_table(self, tournament):
        """ajoute le tournoi au tableau de tournoi"""
        tournament_id_players_list = []
        tournament_id_turns_list = []

        for player_to_add in tournament.tournament_players:
            tournament_id_players_list.append(player_to_add.index_in_base)

        for turn_to_add in tournament.tournament_turns:
            tournament_id_turns_list.append(turn_to_add.index_in_base)

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

        self.data_base.insert_tournament(serialized_tournament)
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()

    def update_tournament_turns_in_table(self, tournament):
        """met a jour le tournoi dans la base et la table"""
        turns_list = []

        for turn in tournament.tournament_turns:
            turns_list.append(turn.index_in_base)

        for tournament_to_update in self.serialized_tournaments_from_db:

            if tournament_to_update.doc_id == int(tournament.index_in_base):
                tournament_to_update['tournament_turns'] = turns_list

        self.data_base.update_tournaments_table(self.serialized_tournaments_from_db)
        self.serialized_tournaments_from_db = self.data_base.get_all_tournaments()

    """ methode tour"""

    def load_turn(self, turn_number, serialized_turn, tournament):
        """charger un tour par son ID de base"""

        turn_to_add = Turn(turn_number,
                           start_time=serialized_turn['turn_start_time'],
                           end_time=serialized_turn['turn_end_time'],
                           index_in_base=serialized_turn.doc_id
                           )

        """crée les objets match du tour"""
        tuples_matches_list = list(eval(serialized_turn['list_matches']))

        player1 = None
        player2 = None

        for match_tuple in tuples_matches_list:

            for player in tournament.tournament_players:

                if player.index_in_base == int(match_tuple[0][0]):
                    player1 = player

                if player.index_in_base == int(match_tuple[1][0]):
                    player2 = player
            player1_score = float(match_tuple[0][1])
            player2_score = float(match_tuple[1][1])

            turn_to_add.matches_table.append(Match(player1, player2, player1_score, player2_score))

        return turn_to_add

    def add_turn_in_table(self, tournament, turn):
        """ajout le tour au tableau de tours"""
        matches_list = ""

        for match_tuple in turn.matches_table:
            matches_list += (match_tuple.__str__() + ",")

        matches_list = matches_list[:-1]

        serialized_turn = {
            'tournament_ID': tournament.index_in_base,
            'turn_name': turn.turn_name,
            'turn_start_time': turn.start_time,
            'turn_end_time': turn.end_time,
            'list_matches': matches_list
        }

        self.data_base.insert_turn(serialized_turn)
        self.serialized_turns_from_db = self.data_base.get_all_turns()

    def update_turn_in_table(self, turn):
        """met a jour le tournoi dans la base et la table"""
        matches_list = ""

        for match_tuple in turn.matches_table:
            matches_list += (match_tuple.__str__() + ",")

        matches_list = matches_list[:-1]

        for turn_to_update in self.serialized_turns_from_db:

            if turn_to_update.doc_id == turn.index_in_base:
                turn_to_update['turn_start_time'] = turn.start_time
                turn_to_update['turn_end_time'] = turn.end_time
                turn_to_update['list_matches'] = matches_list

        self.data_base.update_turns_table(self.serialized_turns_from_db)
        self.serialized_turns_from_db = self.data_base.get_all_turns()

    def set_match_result(self, match, winner):
        """implemente les scores selon le resultat du match"""
        if winner == "1":
            match.player1_score = 1.0

        elif winner == "2":
            match.player2_score = 1.0

        else:
            match.player1_score = 0.5
            match.player2_score = 0.5

        match.player1.total_points += match.player1_score
        match.player2.total_points += match.player2_score

    def get_tournament_result(self, tournament):
        """calcul des resultat du tournoi"""
        results_table = []
        for player in tournament.tournament_players:
            results_table.append(f"{player} : {self.get_player_total_points(player, tournament)}")
        self.view.show_tournament_results(results_table, tournament)

    def run(self):
        """lancement du programme"""

        main_menu_response = ""

        while main_menu_response != "sortir du programme":

            main_menu_response = self.view.show_main_menu()

            if main_menu_response == "1":
                """menu 1 : Tournoi"""
                tournament_menu_response = ""

                while tournament_menu_response != "4":
                    tournament_menu_response = self.view.show_tournament_menu(self.active_tournament)

                    if tournament_menu_response == "1":
                        """Menu 1.1 Creer un tournoi"""
                        tournament_informations = self.view.prompt_create_tournament()

                        """verification de données"""
                        wrong_message_string = ""
                        is_valid_data_tournament = True

                        dates = (tournament_informations['tournament_date'][:-1]).split(",")

                        for date in dates:
                            if not self.is_valid_date(date):
                                is_valid_data_tournament = False
                                wrong_message_string += f"Date : {tournament_informations['tournament_date']}\n"

                        try:
                            int(tournament_informations['turns_number'])

                        except ValueError:
                            is_valid_data_tournament = False
                            wrong_message_string += f"Nombre de tour : {tournament_informations['turns_number']}\n"

                        try:
                            int(tournament_informations['time_control'])

                        except ValueError:
                            is_valid_data_tournament = False
                            wrong_message_string += f"Control de Temps : {tournament_informations['time_control']}\n"

                        if is_valid_data_tournament:
                            self.active_tournament = self.create_tournament(tournament_informations)

                            """récupérer la liste des joueur du tournoi"""
                            tournaments_players_to_add = self.add_player_in_tournament(
                                self.serialized_players_from_db)

                            for player in tournaments_players_to_add:
                                self.active_tournament.tournament_players.append(player)

                            self.add_tournament_in_table(self.active_tournament)
                            self.active_tournament.index_in_base = self.serialized_tournaments_from_db[-1].doc_id

                        else:
                            self.view.show_wrong_response(wrong_message_string)

                    elif tournament_menu_response == "2":
                        """menu 1.2: charger un tournoi"""
                        tournament_id_to_load = self.view.show_tournament_choice_menu(
                            self.serialized_tournaments_from_db)

                        self.active_tournament = self.load_tournament(tournament_id_to_load)

                    elif tournament_menu_response == "3":
                        """menu 1.3: Saisir des resultats"""
                        if self.active_tournament is not None:
                            self.view.show_tournament_management_menu(self.active_tournament)

                            turn_number = len(self.active_tournament.tournament_turns)

                            if turn_number != 0:
                                for turn in self.active_tournament.tournament_turns:

                                    if (turn.start_time is not None) and (turn.end_time is None):
                                        self.active_turn = turn
                                        turn_number -= 1

                                    elif (turn.start_time is None) and (turn.end_time is None):
                                        self.active_turn = turn
                                        turn_number -= 1

                            if turn_number == 4:
                                self.view.show_tournament_terminated(self.active_tournament)

                            while turn_number < int(self.active_tournament.turns_number):
                                if self.active_turn is None:
                                    turn_number_name = turn_number + 1
                                    self.active_turn = Turn(turn_number_name)

                                    """creation des match dans le tour selon la methode déclaré"""
                                    self.active_turn.matches_table = self.match_management.get_matches(
                                        self.active_tournament.tournament_players,
                                        self.active_turn.turn_name
                                    )

                                    """mise a jour de la table des tours"""
                                    self.add_turn_in_table(self.active_tournament, self.active_turn)
                                    self.active_turn.index_in_base = self.serialized_turns_from_db[-1].doc_id

                                    """mise a jour de la table des instance ronde de l'objet tournoi"""
                                    self.active_tournament.tournament_turns.append(self.active_turn)

                                turn_number = len(self.active_tournament.tournament_turns)

                                if self.active_turn.start_time is None:
                                    self.view.show_tournament_management_menu(self.active_tournament)
                                    start_turn_response = self.view.prompt_start_turn(self.active_turn)

                                    if start_turn_response == "o":
                                        """demarrer le tour"""
                                        self.active_turn.start_turn()
                                        self.view.show_turn_started(self.active_turn)

                                    else:
                                        self.update_turn_in_table(self.active_turn)
                                        self.update_tournament_turns_in_table(self.active_tournament)
                                        self.active_turn = None
                                        break

                                if self.active_turn.start_time is not None:
                                    self.view.show_tournament_management_menu(self.active_tournament)
                                    enter_turn_result = self.view.prompt_enter_turn_results(self.active_turn)

                                    if enter_turn_result == "o":
                                        """entrer des resultat de chaque match"""
                                        for match in self.active_turn.matches_table:
                                            self.view.show_tournament_management_menu(self.active_tournament)
                                            winner = self.view.prompt_who_is_match_winner(match, self.active_turn)

                                            self.set_match_result(match, winner)

                                        self.active_turn.end_turn()
                                        self.update_turn_in_table(self.active_turn)

                                        self.active_turn = None

                                        self.update_tournament_turns_in_table(self.active_tournament)

                                        self.view.show_pause()

                                    else:
                                        self.update_turn_in_table(self.active_turn)
                                        self.update_tournament_turns_in_table(self.active_tournament)
                                        self.active_turn = None
                                        break

                            if turn_number == 4:
                                self.get_tournament_result(self.active_tournament)

                        else:
                            self.view.show_no_active_tournament()

            elif main_menu_response == "2":
                """menu 2 : Gestion des joueurs"""

                player_menu_response = ""

                while player_menu_response != "3":

                    player_menu_response = self.view.show_players_menu()

                    if player_menu_response == "1":
                        """menu 2.1 : Entrer un nouveau joueur"""
                        response_add_player = "o"

                        while response_add_player == "o":
                            self.add_player_in_db()
                            response_add_player = self.view.prompt_add_another_player_in_db()

                    elif player_menu_response == "2":
                        """menu 2.2 : Mise à jour d'un joueur"""
                        for_update = True
                        response_update_another_player = "o"
                        while response_update_another_player == "o":

                            self.view.main_title()
                            self.view.show_players_list(self.serialized_players_from_db)
                            id_player_to_modify = self.view.prompt_update_player_in_db()

                            for serialized_player in self.serialized_players_from_db:

                                if serialized_player.doc_id == int(id_player_to_modify):
                                    response_update_another_player_item = "o"

                                    while response_update_another_player_item == "o":
                                        self.view.main_title()
                                        self.view.show_details_of_player(serialized_player, for_update)

                                        item_to_modify = self.view.prompt_player_item_to_update()

                                        if item_to_modify in ["1", "2", "3", "4", "5"]:
                                            result_update = self.update_player_item_in_table(serialized_player,
                                                                                             item_to_modify)

                                            if result_update == 0:
                                                response_update_another_player_item =\
                                                    self.view.prompt_another_player_item()

                                        else:
                                            response_update_another_player_item = "n"

                            response_update_another_player = self.view.prompt_another_player()

            elif main_menu_response == "3":
                """Menu 3 : Rapport"""
                reporting_menu_response = ""

                while reporting_menu_response != "6":

                    reporting_menu_response = self.view.show_reporting_menu()

                    if reporting_menu_response == "1":
                        """3.1 : Liste de tous les joueurs de la base"""
                        players_to_report = []

                        for player in self.serialized_players_from_db:
                            players_to_report.append(Player(player['family_name'],
                                                            player['surname'],
                                                            player['date_of_birth'],
                                                            player['sex'],
                                                            player['ranking'],
                                                            player.doc_id))

                        sorting_type = self.view.prompt_for_sorting_type()

                        if sorting_type in ["1", "2"]:
                            self.view.show_players_reporting_title(sorting_type)
                            self.report.list_players_reporting(
                                players_to_report, sorting_type, self.view)
                            self.view.show_pause()

                        else:
                            self.view.show_wrong_response(f"Type de tri : {sorting_type}")

                    elif reporting_menu_response == "2":
                        """3.2 : Liste des joueurs d'un tournoi"""
                        tournament_id_list = []

                        for tournament in self.serialized_tournaments_from_db:
                            tournament_id_list.append(tournament.doc_id)

                        tournament_id_to_report = self.view.show_tournament_choice_menu(
                            self.serialized_tournaments_from_db)

                        if tournament_id_to_report == "":
                            tournament_id_to_report = "Vide"

                        try:
                            if int(tournament_id_to_report) in tournament_id_list:
                                tournament_to_report = self.load_tournament(tournament_id_to_report)
                                sorting_type = self.view.prompt_for_sorting_type()

                                if sorting_type in ["1", "2"]:
                                    self.view.show_players_reporting_title(sorting_type)
                                    self.report.list_all_players_in_tournament_reporting(
                                        tournament_to_report,
                                        sorting_type,
                                        self.view
                                    )
                                    self.view.show_pause()

                                else:
                                    self.view.show_wrong_response(f"Type de Tri : {sorting_type}")

                            else:
                                self.view.show_wrong_response(f"ID de tournoi : {tournament_id_to_report}")

                        except ValueError:
                            self.view.show_wrong_response(f"ID de tournoi : {tournament_id_to_report}")

                    elif reporting_menu_response == "3":
                        """3 : Liste des tournois"""
                        tournaments_list = []

                        self.view.main_title()

                        for tournament in self.serialized_tournaments_from_db:
                            tournaments_list.append(self.load_tournament(tournament.doc_id))

                        self.report.list_of_tournaments_reporting(tournaments_list, self.view)

                        self.view.show_pause()

                    elif reporting_menu_response == "4":
                        """4 : Liste des tours d'un tournoi"""
                        tournament_id_list = []

                        for tournament in self.serialized_tournaments_from_db:
                            tournament_id_list.append(tournament.doc_id)

                        self.view.main_title()

                        tournament_id_to_report = self.view.show_tournament_choice_menu(
                            self.serialized_tournaments_from_db)

                        if tournament_id_to_report == "":
                            tournament_id_to_report = "Vide"

                        try:
                            if int(tournament_id_to_report) in tournament_id_list:
                                tournament_to_report = self.load_tournament(tournament_id_to_report)
                                self.view.main_title()

                                self.report.turns_list_of_tournament(tournament_to_report, self.view)
                                self.view.show_pause()

                        except ValueError:
                            self.view.show_wrong_response(f"ID de tournoi : {tournament_id_to_report}")

                    elif reporting_menu_response == "5":
                        """5 : Liste des match d'un tournoi"""
                        tournament_id_list = []

                        for tournament in self.serialized_tournaments_from_db:
                            tournament_id_list.append(tournament.doc_id)

                        self.view.main_title()

                        tournament_id_to_report = self.view.show_tournament_choice_menu(
                            self.serialized_tournaments_from_db)

                        if tournament_id_to_report == "":
                            tournament_id_to_report = "Vide"

                        try:
                            if int(tournament_id_to_report) in tournament_id_list:
                                self.view.main_title()
                                tournament_to_report = self.load_tournament(tournament_id_to_report)
                                self.report.match_list_of_tournament_reporting(tournament_to_report, self.view)
                                self.view.show_pause()

                        except ValueError:
                            self.view.show_wrong_response(f"ID de tournoi : {tournament_id_to_report}")

            elif main_menu_response == "4":
                """Menu 4 : Sortie du programme"""
                exit_response = self.view.show_exit_menu()

                if exit_response == "1":
                    main_menu_response = "sortir du programme"

                else:
                    pass
