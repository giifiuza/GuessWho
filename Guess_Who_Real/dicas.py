
class Dicas():
    _dicas = {
        "Brasil": ["É o país do futebol",
                   "Foi colonizado por Portugal",
                   "A bandeira tem verde, amarelo e azul",
                   "O idioma oficial é o português",
                   "Fica na América do Sul"],
        "Estados Unidos": ["A capital é Washington D.C.",
                           "Foi colonizado pelos ingleses",
                           "A bandeira tem listras e estrelas",
                           "O idioma oficial é o inglês",
                           "Fica na América do Norte"],
        "Itália": ["A capital é Roma",
                   "Famosa pela pizza e pelo macarrão",
                   "Faz parte da União Europeia",
                   "O idioma oficial é o italiano",
                   "Fica na Europa"],
        "México": ["A capital é Cidade do México",
                   "Famoso pelo tequila e pelos tacos",
                   "A bandeira tem as cores verde, branca e vermelha",
                   "O idioma oficial é o espanhol",
                   "Fica na América do Norte"],
        "Coreia do Sul": ["A capital é Seul",
                          "Famosa pelo K-pop e pela tecnologia",
                          "A bandeira tem o símbolo do yin-yang",
                          "O idioma oficial é o coreano",
                          "Fica na Ásia"]
    }

    @staticmethod
    def get_dica(pais, num_dica):
        return Dicas._dicas[pais][num_dica]


class Dicas_Serie():
    _dicas_series = {
        "The 100": ["Série de ficção científica pós-apocalíptica da netflix",
                    "Baseada em uma série de livros com o mesmo nome",
                    "O nome da série faz referência a quantidade de pessoas que tinha no grupo de jovens: 100",
                    "Envolve um grupo de jovens que retornam para terra para conferir se está habitável",
                    "A personagem principal chama Clarke Griffin"],
        "The vampire diaries": ["Conta a história de dois irmãos vampiros",
                                "Se passa na cidade fictícia Mystic Falls",
                                "Produzido pela CW, o seriado estreou em 2009",
                                "Um dos irmãos tem diarios que faz referencia ao nome da serie",
                                "Um dos personagens principais chama Damon Salvatore"],
        "Greys anatomy": ["Série de médicos cirurgiões",
                          "Tem 19 temporadas",
                          "Se passa em Seattle",
                          "Todos mundo morre",
                          "Personagem principal chama Meredith Grey"],
        "Friends": ["Conta a história de um grupo de amigos",
                    "Famoso pelo tequila e pelos tacos",
                    "É recomendada para aprender ingles",
                    "O idioma oficial é o espanhol",
                    "Fica na América do Norte"],
        "Game of thrones": ["A capital é Seul",
                            "Famosa pelo K-pop e pela tecnologia",
                            "A bandeira tem o símbolo do yin-yang",
                            "O idioma oficial é o coreano",
                            "Fica na Ásia"]
    }

    @staticmethod
    def get_dica_serie(serie_sort, num_tip):
        return Dicas_Serie._dicas_series[serie_sort][num_tip]


