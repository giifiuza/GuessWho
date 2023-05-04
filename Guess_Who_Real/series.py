import random


class Series:
    _lista_serie = ["The 100", "The vampire diaries", "Greys anatomy", "Friends", "Game of thrones"]

    @staticmethod
    def serie_sorteada():
        return random.choice(Series._lista_serie)