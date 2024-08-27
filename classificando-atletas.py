print("A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento \n"
      "de um atleta e mostre sua categoria, de acordo com a idade:")

from datetime import date
atual = date.today().year
dn = int(input("Entre com o ano de nascimento (ex: 1993): "))
if dn < 1950:
      print("Data não corresponde, Favor tentar novamente.")
idade = atual - dn
if idade <= 9:
      print("o Atleta tem {} anos, e concorre pela categoria: MIRIM". format(idade))
elif idade <= 14:
      print("O atleta tem {} anos, e faz parte da classe: INFANTIL".format(idade))
elif idade <=19:
      print("O atleta tem {} anos, compoe os competidores da classe: JUNIOR".format(idade))
elif idade <= 25:
      print("o Atleta tem {} anos, e ira concorrer pela categoria: SENIOR".format(idade))
else:
      print("o Atleta tem {} anos, e participa do grupo: MASTER".format(idade))
