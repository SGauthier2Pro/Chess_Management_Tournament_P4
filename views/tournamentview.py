"""base de vue"""

import os

CHARACTERS_BY_LINE = 95


class TournamentView:
    """la vue"""

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

    def show_main_menu(self):
        """Affiche le menu principal"""
        self.cls()
        self.main_title()
        print("")
        print("Menu Principal :")
        print("     1 : Tournoi")
        print("     2 : Gestion des Joueurs")
        print("     3 : Rapport")
        print("     4 : Quitter")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice

    def prompt_confirmation(self, information_entry):
        """affiche une demande de confirmation d'entrée"""
        information_display = str(information_entry).replace("[]'", "")
        confirmation = input(
            f"Validez l'information entrée {information_display} (o:pour valider) : "
        )
        return confirmation

    """Affichage Menu Tournoi"""

    def show_tournament_menu(self, tournament):
        """affiche le menu 1: tournoi"""
        self.main_title()
        if tournament is not None:
            self.show_tournament_panel(tournament)
            self.print_line()
        print("")
        print("Menu Tournoi :")
        print("     1 : Créer un nouveau Tournoi")
        print("     2 : Charger un tournoi")
        print("     3 : Saisir des résultats")
        print("     4 : Retour au menu principal")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice

    def show_tournament_panel(self, tournament):
        """affiche le panneau de tournoi en cours"""

        date_to_show = ""

        print(" Tournoi : ".center(CHARACTERS_BY_LINE))
        print(f"     Nom : {tournament.tournament_name}".center(CHARACTERS_BY_LINE))
        print(f"     Lieu : {tournament.tournament_place}".center(CHARACTERS_BY_LINE))
        for date in tournament.tournament_dates:
            date_to_show += date + " | "
        date_to_show = date_to_show[:-2]
        print(f"     Date : {date_to_show}".center(CHARACTERS_BY_LINE))
        print(f"     Contrôle de temps : {tournament.time_control}".center(CHARACTERS_BY_LINE))

    def show_player_in_tournament(self, tournament_players):
        """affiche les joueur inscrit a un tournoi"""
        count_player = 0
        characters_number_in_name_label = 29
        list_to_show = "||"
        print("Joueurs inscrits au tournoi :")
        for player in tournament_players:
            if count_player == 3:
                list_to_show += "\n||"
                count_player = 0
            list_to_show += f"{player.surname} {player.family_name}".center(characters_number_in_name_label) + "||"
            count_player += 1
        print(list_to_show)

    def show_create_tournament_prompt(self, tournament_diplay_informations):
        """affiche le menu 1.1 : Créer un nouveau tournoi"""

        self.main_title()
        print("")
        print("Creation d'un nouveau tournoi")
        self.print_line()
        print("Detail du tournoi :")
        for information_key, information_value in tournament_diplay_informations.items():
            information_value = str(information_value).replace("[]'", "")
            print(f"{information_key} : {information_value}")
        self.print_line()

    def prompt_tournament_name(self):
        """affiche la demande du nom du tournoi"""
        name = input("Entrer le nom du tournoi : ")

        return name

    def prompt_tournament_place(self):
        """affiche la demande du lieu du tournoi"""
        place = input("Entrer le lieu du tournoi : ")

        return place

    def prompt_tournament_date(self):
        """affiche la demande d'une date pour le tournoi"""
        date = input("Entrer la date du tournoi : ")

        return date

    def prompt_another_tournament_date(self):
        """affiche la demande si autre date pour le tournoi"""
        other_date_for_tournament = input("Voulez-vous entrer une autre date ? ('n'=non) : ")

        return other_date_for_tournament

    def prompt_tournament_turns_number(self):
        """affiche la demande le nombre de tour du tournoi (4 par defaut)"""
        turns_number = input("Entrer le mombre de tours du tournoi (4 par defaut): ") or 4

        return turns_number

    def prompt_tournament_description(self):
        """affiche la demande d'une description pour le tournoi"""
        description = input("Enter la description du tournoi : ")

        return description

    def prompt_tournament_time_control(self, time_controls):
        """affiche la demande du controle de temps pour le tournoi"""
        print("Type de control de temps du tournoi (0 par défaut)")
        for time_control in time_controls:
            print(f"{time_controls.index(time_control)}: {time_control}")
        time_control = input("Entrer votre choix : ") or 0

        return time_control

    def prompt_for_add_player(self):
        """entrer les indice de joueur"""
        player_index = input("entrer le numero du joueur : ")
        if not player_index:
            return None
        return int(player_index)

    def show_tournament_choice_menu(self, tournaments_table):
        """affiche le menu 1.2: charger un tournoi"""

        self.main_title()
        print("")
        print("  Liste des tournois :")
        for tournament in tournaments_table:
            date_string = ""
            for date in tournament.tournament_dates:
                date_string += date + ", "

            date_string = date_string[:-2]

            print(f"  {tournament.index_in_base} # nom :{tournament.tournament_name} |"
                  f" date : {date_string} ")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice

    def show_tournament_management_menu(self, tournament):
        """affiche le menu 1.3: saisir les resultat un tournoi"""
        self.main_title()
        self.show_tournament_panel(tournament)
        self.print_line()
        self.show_player_in_tournament(tournament.tournament_players)
        self.print_line()

    def prompt_start_turn(self, turn):
        """demande si on démarre le tour"""
        print(f"{turn.turn_name}")
        start_tour_response = input("Voulez-vous lancer le tour ? (o=oui / n=non) : ")

        return start_tour_response

    def show_turn_started(self, turn):
        """confirme le démarrage du tour"""
        print(f"{turn.turn_name} est démarré !")
        self.show_pause()

    def prompt_enter_turn_results(self, turn):
        """demande si on entre les resultat du tour"""
        print(f"{turn.turn_name}")
        enter_turn_results_response = input("Voulez-vous entrer les résultats du tour ? (o=oui / n=non) : ")

        return enter_turn_results_response

    def prompt_who_is_match_winner(self, match, turn):
        """demande qui a gagner le match"""
        print(f"{turn.turn_name}")
        print(f"Match : {match.player1} contre {match.player2}")
        is_winner = input(f"Entrer le résultat ? 1: {match.player1} 2: {match.player2} 3: nul (Défaut : nul): ")

        return is_winner

    def show_no_active_tournament(self):
        """message stipulant qu'aucun tournoi n'est chargé"""
        self.cls()
        self.main_title()
        print("Aucun tournoi n'est chargé !!".center(CHARACTERS_BY_LINE))
        print("Choisissez le menu 1 : Créer un Tournoi ou 2 : Charger un tournoi".center(CHARACTERS_BY_LINE))
        print("avant de saisir des résultats.".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    def show_no_tournament_in_base(self):
        """affiche pas de tournoi en base"""
        self.cls()
        self.main_title()
        print("Aucun tournoi n'existe dans la base !!".center(CHARACTERS_BY_LINE))
        print("Choisissez le menu 1 : Créer un Tournoi".center(CHARACTERS_BY_LINE))
        print("avant de saisir des résultats.".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    def show_tournament_terminated(self, tournament):
        """affiche que le tournoi est terminé"""
        self.main_title()
        self.show_tournament_panel(tournament)
        self.print_line()
        print("Ce tournoi est terminé !".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    def show_tournament_results(self, tournament_results, tournament):
        """affiche les resultats du tournoi une fois terminé"""
        self.main_title()
        self.show_tournament_panel(tournament)
        self.print_line()
        print("Le tournoi est terminé !")
        print("Voici les résultats :")
        for result in tournament_results:
            print(result)
        self.print_line()
        self.show_pause()
