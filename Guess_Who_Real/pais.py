import random


class Pais:
    _paises = ["Brasil", "Estados Unidos", "Itália", "México", "Coreia do Sul"]

    @staticmethod
    def get_pais():
        return random.choice(Pais._paises)