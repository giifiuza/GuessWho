from pais import Pais
from dicas import Dicas
from time import sleep


class Game:
    def __init__(self):
        self.__player = input("What's your name: ")
        print("Opening the game..")
        sleep(1)
        self.pontos = 0

    @property
    def get_player(self):
        return self.__player

    def play(self):
        pais = Pais.get_pais()
        dicas = Dicas()
        print("\x1b[2J\x1b[1;1H", end="")
        print("|---------------------------------------------|\n"
              f"             WELCOME \033[1;31m{self.__player}\033[m\n"
              "|---------------------------------------------|\n"
              "|                                             |\n"
              "| The game consists of you guessing the secret|\n"
              "|word according to the hints that will appear.|\n"
              "|There will be 5 hints per word, and each time|\n"
              "|you make a mistake you lose a point. If you  |\n"
              "|get the first tip right, you get 5 points.   |\n"
              "|                                             |\n"
              "|---------------------------------------------|\n"
              "|             \033[1;33mGUESS THE COUNTRY\033[m               |\n"
              "|---------------------------------------------|\n")

        acertou = False
        num_dica = 0

        while not acertou and num_dica < 5:

            palpite = input(f"\n\033[1;34mTip {num_dica + 1}\033[m: {dicas.get_dica(pais, num_dica)}\nGuess: ")
            acertou = palpite.capitalize() == pais.capitalize()
            if acertou:
                self.pontos = 5 - num_dica
                print(f"\nCongratulations, {self.__player}! You guessed it {pais}. Won {self.pontos} points!")
            else:
                print("Wrong guess. Try again. You lose one point")
                num_dica += 1
                self.pontos = 5 - num_dica
                print(f"Points: {self.pontos}")

        if num_dica == 5:
            print(f"\n\033[1;31mGame Over, {self.__player}!\033[m \nYou don't guess the country \033[1;33m{pais}\033[m.\n")

    def jogar_denovo(self):
        op = input("Do you wanna play again? (Y/N) ").upper()
        if op == 'Y':
            jogo.play()
        else:
            print("Exiting...")
            sleep(2)
            exit()


jogo = Game()
jogo.play()
jogo.jogar_denovo()

