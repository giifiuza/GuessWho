from pais import Pais


class Dicas(Pais):
    _dicas = {
        "Brasil": ["É o país do futebol", "Foi colonizado por Portugal", "A bandeira tem verde, amarelo e azul",
                   "O idioma oficial é o português", "Fica na América do Sul"],
        "Estados Unidos": ["A capital é Washington D.C.", "Foi colonizado pelos ingleses",
                           "A bandeira tem listras e estrelas", "O idioma oficial é o inglês",
                           "Fica na América do Norte"],
        "Itália": ["A capital é Roma", "Famosa pela pizza e pelo macarrão", "Faz parte da União Europeia",
                   "O idioma oficial é o italiano", "Fica na Europa"],
        "México": ["A capital é Cidade do México", "Famoso pelo tequila e pelos tacos",
                   "A bandeira tem as cores verde, branca e vermelha", "O idioma oficial é o espanhol",
                   "Fica na América do Norte"],
        "Coreia do Sul": ["A capital é Seul", "Famosa pelo K-pop e pela tecnologia",
                          "A bandeira tem o símbolo do yin-yang", "O idioma oficial é o coreano", "Fica na Ásia"]
    }

    @staticmethod
    def get_dica(pais, num_dica):
        return Dicas._dicas[pais][num_dica]