import random
from dicas import Dicas


class Paises(Dicas):
    #, , 'México', 'Itália', 'Coréia do Sul'
    def __init__(self):
        self.palavras = ['BRASIL', 'ESTADOS UNIDOS']

    def sorteio_palavra(self):
        sorteado = random.choice(self.palavras)
        return sorteado



