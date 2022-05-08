"""Gestion  de creation des match"""

from typing import List

from models.match import Match
from models.player import Player


def get_swiss_system_matches(tournament_players_list: List[Player], turn_name):
    """renvoi la liste des match d'un tour selon la methode suisse"""
    match_list = []

    if turn_name == "Round 1":
        tournament_players_list.sort(key=lambda player: player.ranking, reverse=True)

    else:
        tournament_players_list.sort(key=lambda player: player.ranking, reverse=True)
        tournament_players_list.sort(key=lambda player: player.total_points, reverse=True)

    if (len(tournament_players_list) % 2) == 0:
        half = len(tournament_players_list) // 2
        upper_ranking_players_list = tournament_players_list[:half]
        lower_ranking_players_list = tournament_players_list[half:]
        for i in range(len(upper_ranking_players_list)):
            match_list.append(Match(upper_ranking_players_list[i], lower_ranking_players_list[i]))

    return match_list


def set_match_result(match, winner):
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
