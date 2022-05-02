"""classe de joueur"""


class Player:
    """Un Joueur"""

    def __init__(self, family_name, surname, date_of_birth, sex, ranking, index_in_base, total_points=0.0):
        """Initialise le joueur avec son nom et son age"""
        self.family_name = family_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking
        self.index_in_base = index_in_base
        self.total_points = total_points

    def __str__(self) -> str:
        """remonte le nom du joueur"""
        return f"{self.surname} {self.family_name}"

    def __repr__(self):
        """renvoi l'id du joueur comme représentation de l'objet"""
        return self.index_in_base
