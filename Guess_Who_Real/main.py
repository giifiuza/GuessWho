from pais import Pais
from dicas import Dicas, Dicas_Serie
from time import sleep
from series import Series


class Game:
    def __init__(self):
        self.__player = input("What's your name: ")
        print("Opening the game..")
        sleep(1)
        self.pontos = 0
        self.menu()
        self.options()

    @property
    def get_player(self):
        return self.__player

    def menu(self):
        print("|---------------------------------------------|\n"
              f"              WELCOME \033[1;31m{self.__player}\033[m\n"
              "|---------------------------------------------|\n"
              "|                                             |\n"
              "| The game consists of you guessing the secret|\n"
              "|word according to the hints that will appear.|\n"
              "|There will be 5 hints per word, and each time|\n"
              "|you make a mistake you lose a point. If you  |\n"
              "|get the first tip right, you get 5 points.   |\n"
              "|                                             |\n"
              "|---------------------------------------------|\n"
              "|      \033[1;33mGUESS THE COUNTRY OR THE SERIE\033[m         |\n"
              "|                                             |\n"
              "|               \033[1;36mYOU CAN CHOOSE\033[m                |\n"
              "|---------------------------------------------|\n\n")

    def options(self):
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
              "                 CHOOSE ONE                   \n"
              "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
              "[1] - COUNTRY                                \n"
              "[2] - SERIES                                 \n"
              "[3] - EXIT                                   \n")

        chosen = int(input("I choose: "))

        match chosen:
            case 1:
                self.play_pais()
            case 2:
                self.play_serie()
            case 3:
                exit()

    def play_serie(self):
        serie = Series.serie_sorteada()
        dicas = Dicas_Serie()

        acertou = False
        num_tip = 0

        sleep(1)

        while not acertou and num_tip < 5:
            palpite = input(f"\n\033[1;34mTip {num_tip + 1}\033[m: {dicas.get_dica_serie(serie, num_tip)}\nGuess: ")
            acertou = palpite.capitalize() == serie.capitalize()
            if acertou:
                self.pontosTotal = 5 - num_tip
                print(f"\nCongratulations, {self.__player}! You guessed it {serie}. ")
                print(f"Won {self.pontosTotal} points!")
                self.pontos = self.pontos + self.pontosTotal
                self.jogar_denovo()
            else:
                print("Wrong guess. You lose one point. Try again.")
                num_tip += 1
                self.pontosTotal = 5 - num_tip
                print(f"Points: {self.pontos}")

        if num_tip == 5:
            print(
                f"\n\033[1;31mGame Over, {self.__player}!\033[m \nYou don't guess the country \033[1;33m{serie}\033[m.\n")
            self.jogar_denovo()

    def play_pais(self):
            pais = Pais.get_pais()
            dicas = Dicas()

            acertou = False
            num_dica = 0

            sleep(1)

            while not acertou and num_dica < 5:
                palpite = input(f"\n\033[1;34mTip {num_dica + 1}\033[m: {dicas.get_dica(pais, num_dica)}\nGuess: ")
                acertou = palpite.capitalize() == pais.capitalize()
                if acertou:
                    self.pontosTotal = 5 - num_dica
                    print(f"\nCongratulations, {self.__player}! You guessed it {pais}. ")
                    print(f"Won {self.pontosTotal} points!")
                    self.pontos = self.pontos + self.pontosTotal
                    self.jogar_denovo()
                else:
                    print("Wrong guess. You lose one point. Try again.")
                    num_dica += 1
                    self.pontosTotal = 5 - num_dica
                    print(f"Points: {self.pontosTotal}")

            if num_dica == 5:
                print(f"\n\033[1;31mGame Over, {self.__player}!\033[m \nYou don't guess the country \033[1;33m{pais}\033[m.\n")
                self.pontos = self.pontos + self.pontosTotal
                self.jogar_denovo()

    def jogar_denovo(self):
        op = input("\nDo you wanna play again? (Y/N) ").upper()
        if op == 'Y':
            self.options()
        else:
            print(f"\nYou did {self.pontos} points!!")
            print("Exiting...")
            sleep(2)
            exit()


jogo = Game()

