print("Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()\n"
      " e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista \n"
      "e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.")
print("="*80)
from random import randint
from time import sleep

def sorteia(lista):
    print("\033[1;35m Sorteando 5 numeros da lista\033[m")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
    print("\033[1;35m PRONTO \033[m")


def soma1(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"unificando os valores pares da lista {lista} equivale a {soma}")


numeros = list()
sorteia(numeros)
soma1(numeros)