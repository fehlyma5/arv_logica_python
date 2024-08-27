print("\033[1;33;46m Exercício Python 099: Faça um programa que tenha uma função chamada maior(), \n"
      "que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.\033[m")
def asterisco():
    print("="*80)
from time import sleep
asterisco()
def maior(* num):
    cont = maior = 0
    asterisco()
    print(" analisando os numeros repassados ...")
    for valor in num:
        print(f"{valor} ", end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"foram informados {cont} valores ao todo.\n"
          f"O maior valor informado foi {maior}.")


maior(9, 4, 2, 1, 7, 5)
maior(5, 4, 8, 2)
maior(1, 2, 5)
maior(0, 1)
maior()

#o questionamento é  se da pra ter uma interação com o usuario: p q ele digite os numeros e a função leia e interprete.