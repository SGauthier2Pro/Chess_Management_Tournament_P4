from controlers.maincontroller import MainController
from controlers.tinydbmanagement import TinyDBManagement

from views.mainview import MainView
from views.tournamentview import TournamentView
from views.playerview import PlayerView
import os


def main():
    main_directory = os.getcwd()
    main_db_file = "Chess_Tournament_Manager_db.json"
    main_view = MainView()
    tournament_view = TournamentView()
    player_view = PlayerView()
    data_base = TinyDBManagement(main_db_file, main_directory)

    main_controller = MainController(data_base, main_view, tournament_view, player_view)

    main_controller.run()


if __name__ == "__main__":
    main()
