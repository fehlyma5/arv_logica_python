print("Elabore um programa que jogue jo-ken-po com o computador")
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0 , 2)
print('''Suas opções:
\033[1;33m [0] PEDRA \033[m
\033[1;34m [1] PAPEL \033[m
\033[1;35m [2] TESOURA \033[m''')
jogador = int(input("Qual a sua Jogada: >>> "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print('-=' * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU, (Papel embrulha Pedra)")
    elif jogador == 2:
        print("COMPUTADOR VENCEU, (Pedra quebra tesoura)")
    else:
        print("\033[1;32m JOGADA INVALIDA. TENTE NOVAMENTE\033[m")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU, (Papel embrulha Pedra)")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE, (Tesoura corta Papel)")
    else:
         print("\033[1;32m JOGADA INVALIDA. TENTE NOVAMENTE\033[m")
elif computador == 2:
    if jogador == 0:
         print("JOGADOR VENCEU, (Pedra quebra Tesoura)")
    elif jogador == 1:
         print("COMPUTADOR VENCE, (Tesoura corta Papel)")
    elif jogador == 2:
         print("EMPATE")
    else:
         print("\033[1;32m JOGADA INVALIDA. TENTE NOVAMENTE\033[m")
