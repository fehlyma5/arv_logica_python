print("crie um programa que indique se o numero digitado é primo ou nao.")
num = int(input("Digite o numero: "))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print("\033[33m", end= " ")
        tot += 1
    else:
        print("\033[34m", end= " ")
    print("{}".format(c), end= " ")
print("\n \033[m O Numero {} é divisivel {} vezes".format(num, tot))
if tot == 2:
    print("E por isso o numero é PRIMO")
else:
    print("O numero digitado nao é PRIMO")

#é legal ver a contrução de um codigo maior