print("recrie o jogo de adivinhação so que aora com a melhoria do laço de repetição")
from random import randint
computador = randint(0, 10)
print("Sou seu Computador, Acabei de pensar em um numero entre 0 e 10.\n"
      "Será que voce consegue adivinhar qual foi?")
acertos = False
palpite = 0
while not acertos:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertos = True
    else:
        if jogador < computador:
            print("Mais... tente novamente")
        elif jogador > computador:
            print("Menos. Tente novamente")
print("Acertou com {} tentativas".format(palpite))
