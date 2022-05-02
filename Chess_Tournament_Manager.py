from controlers.controller import Controller
from controlers.datamanagement import TinyDBManagement
from controlers.matchmanagement import SwissSystemManagementMatch
from controlers.reports import Report

from views.view import View


def main():
    view = View()
    data_base = TinyDBManagement("Chess_Tournament_Manager_db.json")
    match_management = SwissSystemManagementMatch()
    report = Report()

    main_controller = Controller(data_base, view, match_management, report)

    main_controller.run()


if __name__ == "__main__":
    main()
