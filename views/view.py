"""base de vue"""

import os

CHARACTERS_BY_LINE = 95


class View:
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

        print(" Tournoi en cours : ".center(CHARACTERS_BY_LINE))
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

    def prompt_create_tournament(self):
        """affiche le menu 1.1 : Créer un nouveau tournoi"""

        other_date_for_tournament = "o"
        date = ""

        self.main_title()
        print("")
        print("Creation d'un nouveau tournoi")
        name = input("Entrer le nom du tournoi : ")
        place = input("Entrer le lieu du tournoi : ")
        while other_date_for_tournament == "o":
            date_answer = input("Entrer la date du tournoi : ")
            date += date_answer + ","
            other_date_for_tournament = input("Voulez-vous entrer une autre date ? ('o'=oui/'n'=non) : ")
        turns_number = input("Entrer le mombre de tours du tournoi (4 par defaut): ") or 4
        description = input("Enter la description du tournoi : ")
        time_control = input("Entrer le Type de control de temps du tournoi "
                             "(1: Bullet(par défaut), 2: Blitz ou 3: Rapide) : ") or "1"
        self.print_line()

        return {'tournament_name': name,
                'tournament_place': place,
                'tournament_date': date,
                'turns_number': turns_number,
                'tournament_description': description,
                'time_control': time_control
                }

    def show_tournament_choice_menu(self, tournaments_table):
        """affiche le menu 1.2: charger un tournoi"""

        self.main_title()
        print("")
        print("  Liste des tournois :")
        for tournament in tournaments_table:
            date_string = ""
            for date in tournament['tournament_date']:
                date_string += date + ", "

            date_string = date_string[:-2]

            print(f"  {tournament.doc_id} # nom :{tournament['tournament_name']} |"
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
        """message stipulant qu'aucun tournoin'est chargé"""
        self.cls()
        self.main_title()
        print("Aucun tournoi n'est chargé !!".center(CHARACTERS_BY_LINE))
        print("Choisissez le menu 1 : Créer un Tournoi ou 2 : Charger un tournoi".center(CHARACTERS_BY_LINE))
        print("avant de saisir des résultat.".center(CHARACTERS_BY_LINE))
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

    """Affichage du menu joueur"""

    def show_players_menu(self):
        """affiche le menu 2: Gestion des joueur"""
        self.main_title()
        print("")
        print("Menu Gestion des Joueurs :")
        print("     1 : Entrer un nouveau joueur")
        print("     2 : Mise à jour d'un joueurs")
        print("     3 : Retour au menu précédent")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice

    def prompt_add_player_in_db(self):
        """affiche les demande d'item pour créer un joueur"""
        self.cls()
        self.main_title()
        print("")
        print("Creation d'un nouveau joueur :")
        family_name = input("Nom de famille :")
        surname = input("Prénom :")
        date_birth = input("Date de naissance :")
        sex = input("Sex (M ou F) :")
        ranking = input("Entrer le classement du joueur :")
        print("")
        self.print_line()

        return {'family_name': family_name,
                'surname': surname,
                'date_of_birth': date_birth,
                'sex': sex,
                'total_points': 0,
                'ranking': ranking
                }

    def prompt_add_another_player_in_db(self):
        """demande si on ajoute un nouveau joueur"""
        response_add_new_player = input("Voulez vous rentrer un nouveau joueur ? (o/n) :")

        return response_add_new_player

    def prompt_for_add_player(self):
        """entrer les indice de joueur"""
        player_index = input("entrer le numero du joueur : ")
        if not player_index:
            return None
        return int(player_index)

    def show_players_list(self, serialized_players):
        """affiche la liste des joueur de la base"""
        characters_number_in_id_label = 6
        characters_number_in_name_label = 22
        print("Liste de joueurs :")
        count_player = 0
        list_to_show = "||"
        for player in serialized_players:
            if count_player == 3:
                list_to_show += "\n||"
                count_player = 0
            player_id = f" {player.doc_id}"
            player_name = f" {player['surname']} {player['family_name']}"
            list_to_show += player_id.center(characters_number_in_id_label) + "#" + player_name.center(
                characters_number_in_name_label) + "||"
            count_player += 1
        print(list_to_show)
        self.print_line()

    def prompt_update_player_in_db(self):
        """renvoi l'indice du joueur a mettre a jour"""
        id_player_to_update = input("Entrer le numéro du joueur a modifier : ")

        return id_player_to_update

    def show_details_of_player(self, serialized_player, for_update):
        """affiche le détails d'un joueur en numérotant les items"""

        date_string = serialized_player['date_of_birth'].replace("'[]", "")

        print("Informations personnelles du joueur :")
        print("")
        print(f" 1 # Nom de Famille : {serialized_player['family_name']}")
        print(f" 2 # Prénom : {serialized_player['surname']}")
        print(f" 3 # Date de naissance : {date_string}")
        print(f" 4 # Sexe : {serialized_player['sex']}")
        print(f" 5 # Classement : {serialized_player['ranking']}")
        if for_update:
            print(" 6 # Aucune modification")
        print("")
        self.print_line()

    def prompt_player_item_to_update(self):
        """renvoi quel item du joueur doit être mis a jour"""
        player_item_to_update = input("Entrer le numéro de l'information à "
                                      "mettre à jour (6 : pour sortir sans modification) : ")

        return player_item_to_update

    def prompt_information_to_update(self):
        """renvoi l'information de mise a jour de l'item"""
        information_to_update = input("Entrer la nouvelle valeur : ")

        return information_to_update

    def prompt_another_player_item(self):
        """renvoi si on met a jour un autre item du joueur"""
        response_another_player_item_to_update = input(
            "Voulez-vous mettre a jour une autre information du joueur ? ('o'=oui/'n'=non) : "
        )

        return response_another_player_item_to_update

    def prompt_another_player(self):
        """renvoi si mise a jour d'un autre joueur"""
        response_another_player_to_update = input("Voulez-vous mettre a jour un autre joueur ?('o'=oui/'n'=non) : ")

        return response_another_player_to_update

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
        self.main_title()
        print("")
        if sort_type == "1":
            print("Liste des joueurs par Ordre Alphabetique".center(CHARACTERS_BY_LINE))
        elif sort_type == "2":
            print("Liste des Joueurs par Classement".center(CHARACTERS_BY_LINE))
        print("")

    def show_tournament_to_report(self, tournament):
        """affiche le nom du tournoi """
        print("")
        print(f"{tournament.tournament_name}".center(CHARACTERS_BY_LINE))
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

    """Affichage du menu sortie du programme"""

    def show_exit_menu(self):
        """affiche le menu 5: quitter"""
        self.cls()
        self.main_title()
        print("")
        print("Etes-vous sûr de vouloir quitter le programme ?")
        print("     1 : Quitter")
        print("     2 : Retour au menu principal")
        print("")
        self.print_line()
        menu_choice = input("Entrer votre choix : ")

        return menu_choice
