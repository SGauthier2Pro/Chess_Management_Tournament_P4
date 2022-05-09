"""classe vue player"""


from views.mainview import MainView

CHARACTERS_BY_LINE = 95


class PlayerView(MainView):
    """vue objet player héritée de MainView"""

    """ affichage pour menu principal"""

    def show_no_player_in_base(self):
        """affichier pas de joueur en base"""
        self.main_title()
        print("")
        print("Impossible d'effectuer cette opération !".center(CHARACTERS_BY_LINE))
        print("Il n'y a pas de joueur dans la base !".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    def show_not_enough_players(self):
        """affiche si pas assez de joueur en base"""
        self.main_title()
        print("")
        print("Impossible d'effectuer cette opération !".center(CHARACTERS_BY_LINE))
        print("Il n'y a pas assez de joueurs dans la base !".center(CHARACTERS_BY_LINE))
        self.print_line()
        self.show_pause()

    def show_wrong_player_id(self, wrong_message_string):
        """affiche si id player inexistant"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"{wrong_message_string} n'est pas un indice de joueur existant !".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def show_wrong_gender(self, wrong_message_string):
        """affiche si sexe erronée"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"Sexe : {wrong_message_string}".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def show_wrong_item(self, string_item, updated_information):
        """affiche si player item erronée"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"{string_item} : {updated_information}".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def show_wrong_ranking(self, wrong_message_string):
        """affiche si sexe erronée"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"Classement : {wrong_message_string}".center(CHARACTERS_BY_LINE))
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

    def show_create_player_prompt(self, player_display_informations):
        """affiche le menu 2.1 : Créer un joueur"""

        self.cls()
        self.main_title()
        print("")
        print("Creation d'un nouveau joueur".center(CHARACTERS_BY_LINE))
        print("")
        self.print_line()
        print("Detail du joueur :")
        for information_key, information_value in player_display_informations.items():
            print(f"{information_key} : {information_value}")
        self.print_line()

    def prompt_player_name(self):
        """affiche la demande du nom du joueur"""
        family_name = input("Entrer le nom de famille du joueur : ")

        return family_name

    def prompt_player_surname(self):
        """affiche la demande du prénom du joueur"""
        surname = input("Entrer le prénom du joueur : ")

        return surname

    def prompt_date_birth(self):
        """affiche la demande de date de naissance du joueur"""
        date_birth = input("Entrer la date de naissance du joueur : ")

        return date_birth

    def prompt_player_gender(self):
        """affiche la demande du genre du joueur"""
        gender = input("Entrer le sexe du joueur (H, F ou ND) : ")

        return gender

    def prompt_player_ranking(self):
        """affiche la demande du classement du joueur"""
        ranking = input("Entrer le classement du joueur : ")

        return ranking

    def prompt_create_another_player(self):
        """demande si on ajoute un nouveau joueur"""
        response_add_new_player = input("Voulez vous rentrer un nouveau joueur ? (o/n) :")

        return response_add_new_player

    def prompt_for_add_player(self):
        """entrer les indice de joueur"""
        player_index = input("entrer le numero du joueur : ")
        if not player_index:
            return None
        return int(player_index)

    def show_players_list(self, players_table):
        """affiche la liste des joueur de la base"""
        characters_number_in_id_label = 6
        characters_number_in_name_label = 22
        print("Liste de joueurs :")
        count_player = 0
        list_to_show = "||"
        for player in players_table:
            if count_player == 3:
                list_to_show += "\n||"
                count_player = 0
            player_id = f" {player.index_in_base}"
            player_name = f" {player.surname} {player.family_name}"
            list_to_show += player_id.center(characters_number_in_id_label) + "#" + player_name.center(
                characters_number_in_name_label) + "||"
            count_player += 1
        print(list_to_show)
        self.print_line()

    def prompt_id_player_in_db(self):
        """renvoi l'indice d'un joueur"""
        id_player_to_update = input("Entrer le numéro d'un joueur : ")

        return id_player_to_update

    def show_details_of_player(self, player):
        """affiche le détails d'un joueur en numérotant les items"""

        date_string = player.date_of_birth.replace("'[]", "")

        print("Informations personnelles du joueur :")
        print("")
        print(f" 1 # Nom de Famille : {player.family_name}")
        print(f" 2 # Prénom : {player.surname}")
        print(f" 3 # Date de naissance : {date_string}")
        print(f" 4 # Sexe : {player.gender}")
        print(f" 5 # Classement : {player.ranking}")
        print(" 6 # Sortie du Menu")
        print("")
        self.print_line()

    def prompt_player_item_to_update(self):
        """renvoi quel item du joueur doit être mis a jour"""
        player_item_to_update = input("Entrer le numéro de l'information à mettre à jour : ")

        return player_item_to_update

    def prompt_information_to_update(self, string_item):
        """renvoi l'information de mise a jour de l'item"""
        information_to_update = input(f"Entrer la nouvelle valeur pour {string_item} : ")

        return information_to_update

    def show_update_success(self, string_item):
        """affiche operation reussi"""
        print(f"Mise a jour de {string_item} effectué avec succès !")
        self.show_pause()

    def prompt_another_player(self):
        """renvoi si mise a jour d'un autre joueur"""
        response_another_player_to_update = input("Voulez-vous mettre a jour un autre joueur ?('o'=oui/'n'=non) : ")

        return response_another_player_to_update
