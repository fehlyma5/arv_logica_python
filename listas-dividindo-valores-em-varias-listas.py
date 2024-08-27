print('Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas\n'
      ' listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. \n'
      'Ao final, mostre o conteúdo das três listas geradas')

valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Informe um dado: ')))
    resp = str(input('Deseja continuar: S/N')).strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'os valores digitados foram {valores}')
print(pares)
print(impares)
