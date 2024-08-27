print("Fazendo uma analise para saber se 3 valores podem formar um triangulo,  qual seria o tipo:\n"
      "dada a informação:\n"
      "[1] ISOSCELES: dois lados iguaiS e um diferente\n"
      "[2] EQUILATERO: todos os lados sao iguais\n"
      "[3] ESCALENO: todos os lados sao diferentes.")

lado1 = float(input("Digite o valor um: "))
lado2 = float(input("Digite o  valor dois: "))
lado3 = float(input("Digite o valor tres: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print("Os segmentos acima podem formar um triangulo  ", end='')
    if lado1 != lado2 != lado3:
        print("ESCALENO")
    elif lado1 == lado2 == lado3:
        print("EQUILATERO")
    else:
        print("ISOSCELES")
else:
    print("As informações não formam um triangulo")
