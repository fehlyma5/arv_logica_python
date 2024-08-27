print("Um programa q leia um numero qualquer e peça para o usuario escolher qual a base de conversao")

num = int(input("Digite um numero inteiro: "))
print('''Escolha uma opção de conversão:"
"\033[1;33m [1] para octal\033[m"
"\033[1;32m [2] para hexadecimal\033[m"
"\033[1;35m [3]para binario\033[m''')
opcao = int(input("\033[4;36m Sua opção é: \033[m"))
if opcao == 1:
    print("\033[4;33m {} o numero escolhido, convertido para octal fica {}\033[m".format(num, oct(num) [2:]))
elif opcao == 2:
    print("\033[4;32m {} o numero escolhido, convertido para hexadecimal fica {}\033[m".format(num, hex(num)[2:]))
elif opcao == 3:
    print("\033[4;35m {} o numero escolhido convertido para binario fica {}\033[m".format(num, bin(num) [2:]))
else:
    print("\033[1;31m Opção invalida, tente novamente.\033[m")

