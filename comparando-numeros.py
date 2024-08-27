print("compare dois numeros e indique qual dos dois ´maior, e em caso de empate informar que sao iguais")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
if num1 > num2:
    print("O numero maior é o {}".format(num1))
elif num1 < num2:
    print("o numero maior é o {}".format(num2))
else:
    print("Os numero sao iguais")