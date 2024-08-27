print("\033[1;45mCrie um programa que leia números inteiros pelo teclado. \n"
      "O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. \n"
      "No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).\033[m")
cont = soma = 0
while True: #aqui tow declarando que o loop é infinito enquanto for verdadeiro
      n = int(input("Entre com o numero [aperte 999 para pausar]: "))
      if n == 999:
            break #aqui tow dizendo pro programa parar qdo chegar nessa condição
      cont += 1
      soma += n
print(f"a soma dos valores digitados é {soma}")
