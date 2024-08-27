print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, \n'
      ' mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')

ficha = list()
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('1º NOTA: '))
    nota2 = float(input('2º NOTA: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja Continuar - [S/N]: '))
    if resp in 'Nn:':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar Nota e Qual Aluno(a)? [999 interromper]: '))
    if opc == 999:
        print('Finalizando ...')
        break
    if opc <= len(ficha) - 1:
        print(f'Nota de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte Sempre')

