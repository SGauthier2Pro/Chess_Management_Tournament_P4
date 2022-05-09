"""base de vue"""

import os

CHARACTERS_BY_LINE = 95


class MainView:
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
        input("appuyer sur entrer pour continuer...")

    def show_wrong_response(self, wrong_message_string):
        """affiche si la réponse n'etait pas attendu"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"{wrong_message_string} n'est pas un choix possible !".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def show_wrong_date(self, wrong_message_string):
        """affiche si date erronée"""
        self.main_title()
        print("")
        print("Entrée invalide !".center(CHARACTERS_BY_LINE))
        print("")
        print(f"Date : {wrong_message_string}".center(CHARACTERS_BY_LINE))
        self.show_pause()

    def prompt_confirmation(self, information_entry):
        """affiche une demande de confirmation d'entrée"""
        information_display = str(information_entry).replace("[]'", "")
        confirmation = input(
            f"Validez l'information entrée {information_display} (o:pour valider) : "
        )
        return confirmation

    """affichage des menu du main controller"""

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
