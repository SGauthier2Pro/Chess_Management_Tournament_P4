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
                    serialized_player['sex'],
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
                player_to_update.sex = updated_information
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
        wrong_message_string = ""

        is_valid_information = True

        serialized_player = self.view.prompt_add_player_in_db()

        if not valuechecker.is_valid_date(serialized_player['date_of_birth']):
            is_valid_information = False
            wrong_message_string += f"Date de naissance : {serialized_player['date_of_birth']} \n"

        if not valuechecker.is_valid_gender(serialized_player['sex']):
            is_valid_information = False
            wrong_message_string += f"Sexe : {serialized_player['sex']} \n"

        if not valuechecker.is_valid_int(serialized_player['ranking']):
            is_valid_information = False
            wrong_message_string += f"Classement : {serialized_player['ranking']} \n"

        if is_valid_information:

            created_player = create_player(serialized_player)

            self.players_table.append(created_player)
            self.save_players()
            created_player.index_in_base = self.serialized_players_from_db[-1].doc_id

        else:
            self.view.show_wrong_response(wrong_message_string)

    def save_players(self):
        """sauvegarde la table des joueurs en base"""
        serialized_players = []

        for player in self.players_table:

            serialized_player = {
                "family_name": player.family_name,
                "surname": player.surname,
                "date_of_birth": player.date_of_birth,
                "sex": player.sex,
                "ranking": player.ranking
            }

            serialized_players.append(serialized_player)

        self.data_base.update_players_table(serialized_players)
        self.serialized_players_from_db = self.data_base.get_all_players()
