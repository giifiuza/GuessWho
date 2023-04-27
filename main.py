from paises import Paises


def game():

    paises = Paises()
    lista = paises.palavras
    sorteado = paises.sorteio_palavra()
    tips = paises.dicas(sorteado)
    player = input("Input your name: ")
    print(sorteado)
    print(tips[0])
    pontos = 0
    chances = 5

    while True:

        guess = input("Input your guess: ").upper()

        if guess == sorteado:
            print("Congratulations!! You guessed")
            pontos += 5
            sorteado = paises.sorteio_palavra()

        if guess != sorteado:
            print("Wrong word.")
            print(tips[1])
            chances -= 1





game()