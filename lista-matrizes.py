print('Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores \n'
      'lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
