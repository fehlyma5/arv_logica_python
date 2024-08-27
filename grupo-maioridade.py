print("crie um programa que leia 7 datas de nascimento, e separe se maior ou menor de idade")
print("x=x" * 10)
from datetime import date
ano = date.today().year
mais_velho = 0
mais_novo = 0
for dn in range (1, 8):
    ano_nasc = int(input("Data de Nascimento {}:  ".format(dn)))
    idade_atual = ano - ano_nasc
    if idade_atual >= 21:
        mais_velho += 1
    else:
        mais_novo += 1
print("\033[4;31m Há {} pessoas que serão agrupadas no grupo MAIOR IDADE\n"
      "E {} pessoas que farão parte do grupo MENOR IDADE\033[m".format(mais_velho, mais_novo))

#a gente obserca um erro que pode ser evitado no que se refere a quantidade de numeros digitados pelo usuario para representar ANO
#se a gente consegue criar uma lista a partir dos dados recebidos pra melhor identificar os grupos.