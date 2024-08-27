print("print um programa que execute um numero fatorial")
print("-=" * 10)
from math import factorial
n = int(input("Digite um numero p calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))
#aqui importamos um modulo da biblioteca d matematica chamada math
