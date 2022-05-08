from controlers.maincontroller import MainController
from controlers.datamanagement import TinyDBManagement

from views.mainview import MainView
from views.tournamentview import TournamentView
from views.playerview import PlayerView


def main():
    main_view = MainView()
    tournament_view = TournamentView()
    player_view = PlayerView()
    data_base = TinyDBManagement("Chess_Tournament_Manager_db.json")

    main_controller = MainController(data_base, main_view, tournament_view, player_view)

    main_controller.run()


if __name__ == "__main__":
    main()
