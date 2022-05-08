"""classe turn manager"""

from models.turn import Turn
from models.match import Match
import controlers.matchcontroller


def create_turn(serialized_turn):
    """crée un tour"""
    turn_number = serialized_turn['turn_name'][-1]

    turn = Turn(
        turn_number,
        serialized_turn['turn_start_time'],
        serialized_turn['turn_end_time'],
        serialized_turn['list_matches'],
        serialized_turn.doc_id
    )

    return turn


class TurnController:
    """turn manager"""

    def __init__(self, turn_view, data_base, player_controller):
        """initialisation du turn manager"""
        self.view = turn_view
        self.data_base = data_base
        self.serialized_turns_from_db = self.data_base.get_all_turns()

        self.turns_table = []
        self.active_turn = None

        for turn in self.serialized_turns_from_db:
            self.turns_table.append(self.load_turn(turn, player_controller))

    def save_turns(self):
        """sauvegarde la table des tour en base"""
        serialized_turns = []

        for turn in self.turns_table:

            matches_list = ""

            for match_tuple in turn.matches_table:
                matches_list += (match_tuple.__str__() + ",")

            matches_list = matches_list[:-1]

            serialized_turn = {
                'turn_name': turn.turn_name,
                'turn_start_time': turn.start_time,
                'turn_end_time': turn.end_time,
                'list_matches': matches_list
            }

            serialized_turns.append(serialized_turn)

        self.data_base.update_turns_table(serialized_turns)
        self.serialized_turns_from_db = self.data_base.get_all_turns()

    def load_turn(self, serialized_turn, player_controller):
        """charger un tour par son ID de base"""

        turn_number = serialized_turn['turn_name'][-1]

        turn_to_load = Turn(turn_number,
                            start_time=serialized_turn['turn_start_time'],
                            end_time=serialized_turn['turn_end_time'],
                            index_in_base=serialized_turn.doc_id
                            )

        """crée les objets match du tour"""
        tuples_matches_list = list(eval(serialized_turn['list_matches']))

        player1 = None
        player2 = None

        for match_tuple in tuples_matches_list:

            for player in player_controller.players_table:

                if player.index_in_base == int(match_tuple[0][0]):
                    player1 = player

                if player.index_in_base == int(match_tuple[1][0]):
                    player2 = player
            player1_score = float(match_tuple[0][1])
            player2_score = float(match_tuple[1][1])

            turn_to_load.matches_table.append(Match(player1, player2, player1_score, player2_score))

        return turn_to_load

    def create_new_turn(self, turn_number, tournament):
        """crée un tour"""

        turn = Turn(turn_number)

        """creation des match dans le tour selon la methode déclaré"""
        turn.matches_table = controlers.matchcontroller.get_swiss_system_matches(
            tournament.tournament_players,
            turn.turn_name
        )

        self.turns_table.append(turn)
        self.save_turns()
        turn.index_in_base = self.serialized_turns_from_db[-1].doc_id

        return turn

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
