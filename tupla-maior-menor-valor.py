print("Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. \n"
      "Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla")
print("="*80)

from random import randint
number = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"The numbers drawn were: ", end=' ')
for n in number:
    print(f"\033[1;35m {n} \033[m")
print(f"The number with the highest value drawn was {max(number)} \n"
          f"The number with the lowest value was {min(number)}")
