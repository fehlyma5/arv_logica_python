print("Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante \n"
      "'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')")

print("0-"*100)

def leiaInt(msg):
    while leiaInt() == int:
        leiaInt = int(input()).strip().upper(0)
    else:
        print("\033[1;32m Digite um numero em formato INTEIRO, para validar o procedimento. (Ex:22)\033[m")

n = leiaInt("digite um numeor inteiro: ")
print(f"Voce digitou o numero {n}")
#a logica saiu quase certa com o uso certame da função > while > else,mas  a execução das infomações foi inadequada