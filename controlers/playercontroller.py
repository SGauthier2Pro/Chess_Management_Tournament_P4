"""classe player manager"""

from models.player import Player
from controlers import valuechecker


def create_player(serialized_player):
    """créer un objet player"""
    if type(serialized_player) is dict:
        index_in_base = 0
    else:
        index_in_base = serialized_player.doc_id

    player = Player(serialized_player['family_name'],
                    serialized_player['surname'],
                    serialized_player['date_of_birth'],
                    serialized_player['gender'],
                    int(serialized_player['ranking']),
                    index_in_base=index_in_base
                    )

    return player


class PlayerController:
    """player manager"""

    def __init__(self, player_view, data_base):
        """initialisation avec vue et data base management"""

        self.data_base = data_base
        self.view = player_view
        self.serialized_players_from_db = self.data_base.get_all_players()

        self.players_table = []

        for player in self.serialized_players_from_db:
            self.players_table.append(create_player(player))

    def update_player_item(self, player_to_update, item_to_modify):
        """met a jour un item de joueur et remet a jour la base et la table"""

        string_item = ""
        updated_information = ""
        could_be_updated = False

        if item_to_modify == "1":
            string_item = "Nom de Famille"
            updated_information = self.view.prompt_information_to_update(string_item)
            player_to_update.family_name = updated_information
            could_be_updated = True

        elif item_to_modify == "2":
            string_item = "Prénom"
            updated_information = self.view.prompt_information_to_update(string_item)
            player_to_update.surname = updated_information
            could_be_updated = True

        elif item_to_modify == "3":
            string_item = "Date de naissance"
            updated_information = self.view.prompt_information_to_update(string_item)
            if valuechecker.is_valid_date(updated_information):
                player_to_update.date_of_birth = updated_information
                could_be_updated = True

            else:
                could_be_updated = False

        elif item_to_modify == "4":
            string_item = "Sexe"
            updated_information = self.view.prompt_information_to_update(string_item)
            if valuechecker.is_valid_gender(updated_information):
                player_to_update.gender = updated_information
                could_be_updated = True

            else:
                could_be_updated = False

        elif item_to_modify == "5":
            string_item = "Classement"
            updated_information = self.view.prompt_information_to_update(string_item)
            if valuechecker.is_valid_int(updated_information):
                player_to_update.ranking = int(updated_information)
                could_be_updated = True

            else:
                could_be_updated = False

        if could_be_updated:
            self.save_players()
        else:
            self.view.show_wrong_response(f"{string_item} : {updated_information}\n")

    def update_player(self):
        """menu mise a jour d'un joueur"""
        self.view.show_players_list(self.players_table)
        id_player = self.view.prompt_id_player_in_db()

        for player in self.players_table:
            if valuechecker.is_valid_int(id_player):
                if player.index_in_base == int(id_player):
                    update_another_player_item = ""

                    while update_another_player_item != "n":
                        self.view.main_title()
                        self.view.show_details_of_player(player)

                        item_to_modify = self.view.prompt_player_item_to_update()

                        if item_to_modify in ["1", "2", "3", "4", "5"]:

                            self.update_player_item(
                                player,
                                item_to_modify
                            )

                        elif item_to_modify == "6":
                            update_another_player_item = "n"

                        else:
                            self.view.show_wrong_response(f"{item_to_modify} n'est pas une réponse valide !")

            else:
                self.view.show_wrong_response(f"{id_player} n'est pas une réponse valide !")
                break

    def create_new_player(self):
        """ajoute un joueur a la base de joueur"""

        """saisie des données de joueur"""
        player_creation_display = {}
        player_informations = {}
        player_informations_completed = False

        while not player_informations_completed:

            player_name_done = False
            while not player_name_done:
                self.view.show_create_player_prompt(player_creation_display)

                player_name = self.view.prompt_player_name()
                confirmation = self.view.prompt_confirmation(player_name)
                if confirmation == "o":
                    player_informations['family_name'] = player_name
                    player_creation_display['Nom de famille'] = player_name
                    player_name_done = True
                    player_informations_completed = True
                else:
                    player_informations_completed = False

            player_surname_done = False
            while not player_surname_done:
                self.view.show_create_player_prompt(player_creation_display)

                player_surname = self.view.prompt_player_surname()
                confirmation = self.view.prompt_confirmation(player_surname)
                if confirmation == "o":
                    player_informations['surname'] = player_surname
                    player_creation_display['Prénom'] = player_surname
                    player_surname_done = True
                    player_informations_completed = True
                else:
                    player_informations_completed = False

            player_date_birth_done = False
            while not player_date_birth_done:
                self.view.show_create_player_prompt(player_creation_display)

                date_answer = self.view.prompt_date_birth()
                if valuechecker.is_valid_date(date_answer):
                    confirmation = self.view.prompt_confirmation(date_answer)
                    if confirmation == "o":
                        player_informations['date_of_birth'] = date_answer
                        player_creation_display['Date de naissance'] = date_answer
                        player_date_birth_done = True
                        player_informations_completed = True
                    else:
                        player_informations_completed = False
                else:
                    self.view.show_wrong_response(f"Date : {date_answer}")

            player_gender_done = False
            while not player_gender_done:
                self.view.show_create_player_prompt(player_creation_display)

                gender = self.view.prompt_player_gender()
                if valuechecker.is_valid_gender(gender):
                    confirmation = self.view.prompt_confirmation(gender)
                    if confirmation == "o":
                        player_informations['gender'] = gender
                        player_creation_display['Sexe'] = gender
                        player_gender_done = True
                        player_informations_completed = True
                    else:
                        player_informations_completed = False
                else:
                    self.view.show_wrong_response(f"Sexe : {gender}")

            player_ranking_done = False
            while not player_ranking_done:
                self.view.show_create_player_prompt(player_creation_display)

                ranking = self.view.prompt_player_ranking()
                if valuechecker.is_valid_int(ranking):
                    confirmation = self.view.prompt_confirmation(ranking)
                    if confirmation == "o":
                        player_informations['ranking'] = ranking
                        player_creation_display['Classement'] = ranking
                        player_ranking_done = True
                        player_informations_completed = True
                    else:
                        player_informations_completed = False
                else:
                    self.view.show_wrong_response(f"Classement : {ranking}")

        if player_informations_completed:
            created_player = create_player(player_informations)

            self.players_table.append(created_player)
            self.save_players()
            created_player.index_in_base = self.serialized_players_from_db[-1].doc_id

    def save_players(self):
        """sauvegarde la table des joueurs en base"""
        serialized_players = []

        for player in self.players_table:

            serialized_player = {
                "family_name": player.family_name,
                "surname": player.surname,
                "date_of_birth": player.date_of_birth,
                "gender": player.gender,
                "ranking": player.ranking
            }

            serialized_players.append(serialized_player)

        self.data_base.update_players_table(serialized_players)
        self.serialized_players_from_db = self.data_base.get_all_players()
