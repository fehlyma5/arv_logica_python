print("Crie um programa que crie um menu de opções para interação com o usuario")
print("!-"*10)
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print('''Digite a opção desejada:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] REFAZER
    [5] SAIR''')
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        print(n2 + n1)
    elif opcao == 2:
        print(n2 * n1)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('o maiorentre {} e {} é {}'. format(n1, n2, maior))
    elif opcao == 4:
        print("informe novamente o numeros: ")
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("finalizando ...")
    else:
        print("Opcao invalida, tente novamente. >>> ")
    print("-=" * 10)
print("-----finish ------")
#itens a considerar tipo se o usuario digitar um float
#se ele digitar numeros iguais como vai funcionar a opçao 3