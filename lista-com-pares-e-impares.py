print('Crie um programa onde o usuario posa digitar 7 valores numericos e cadastre-os em 1 lista \n'
      'unica q mantenha separdos os valores pares e impares, motrando essa lista no final em ordem crescente.')

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'os valores PARES são: {num[0]} \n'
      f'valors IMPARES {num[1]}')
