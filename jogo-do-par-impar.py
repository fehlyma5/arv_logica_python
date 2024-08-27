print("\033[44m Faça um programa que jogue par ou ímpar com o computador. \n"
      "O jogo só será interrompido quando o jogador perder, \n"
      "mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.\033[m")
from random import randint
computador = randint(0, 10)
palpite = 0
while True:
    jogador = int(input("jogue o numero desejado: "))
    result = jogador + computador
    if jogador == False:
        print("GAME OVER. Voce PERDEU.")
    palpite += 1
    print(f"Computador jogou {computador} e Jogador jogou {jogador} \n")
print("Jogador acertou {} vezes".format(result))
#nao prestou meu cod, pk nao rodou conforme a solucao para o problema, no primeiro teste logico computador so jogava 4
