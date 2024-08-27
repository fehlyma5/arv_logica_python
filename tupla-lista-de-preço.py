print('Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. \n'
      'No final, mostre uma listagem de preços, organizando os dados em forma tabular.')

listagem = ('lápis', 1.75,
            'borracha',2,
            'caderno', 19.90,
            'estojo', 5,
            'mochila', 99,
            'caneta', 12.99)

def asterisco():
      print('-' * 80)


asterisco()
print(f'{"LISTA DE COMPRAS":^40}')
asterisco()
for pos in range (0, len(listagem)):
      if pos % 2 == 0:
            print(f'{listagem[pos]:.<30}', end='')
      else:
            print(f'R${listagem[pos]:>7.2f}')
asterisco()
