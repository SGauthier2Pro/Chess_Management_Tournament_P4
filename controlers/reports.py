"""classe des rapport"""


class Report:
    """un rapport"""

    def list_players_reporting(self, players, sorting_type, view):
        """affiche tous les joueurs de la base avec leurs informations selon le tri stipulé"""
        sorted_players = []

        if sorting_type == "1":
            sorted_players = sorted(players, key=lambda player: player.family_name)

        elif sorting_type == "2":
            sorted_players = sorted(players, key=lambda player: player.ranking)

        for player_to_show in sorted_players:
            view.show_details_of_player_reporting(player_to_show)

    def list_all_players_in_tournament_reporting(self, tournament, sorting_type, view):
        """affiche tous les joueurs par ordre alphabetique d'un tournoi"""
        view.show_tournament_to_report(tournament)
        self.list_players_reporting(tournament.tournament_players, sorting_type, view)

    def list_of_tournaments_reporting(self, tournaments, view):
        """rapport listant tous les tournois de la base avec détails"""
        for tournament in tournaments:
            view.show_tournament_details_reporting(tournament)

    def turns_list_of_tournament(self, tournament, view):
        """rapport listant tous les tours d'un tournoi"""
        view.show_tournament_details_reporting(tournament)

        for turn in tournament.tournament_turns:
            view.show_turn_details_reporting(turn)

    def match_list_of_tournament_reporting(self, tournament, view):
        """rapport listant les matchs d'un tournoi"""
        view.show_tournament_panel(tournament)

        for turn in tournament.tournament_turns:
            view.print_line()
            view.show_turn_details_reporting(turn)

            for match in turn.matches_table:
                view.show_match_details_reporting(match)
