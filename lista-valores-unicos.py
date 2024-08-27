print('Crie um programa onde o usuario possa digitar vario valores numericos e cadastre-os em uma lista\n'
      'Caso o nº já exisa, ele ñ deve ser adicionado. No final, serão retornados os valores unicos em ordem crescente')
listanum =[]
while True:
    listanum.append(int(input('Digite um Valor: ')))
    user = str(input('Deseja continuar? [S] - sim// [N] - nao >>> '))
    if user == 's':
        listanum.append(int(input('Digite um Valor: ')))
        user = str(input('Deseja continuar? [S] - sim// [N] - nao >>> '))
    else:
        break
listanum.sort()
print(listanum)

#solução GUANABARA
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros: #nessa condicional "SE N NAO ESTIVER INCLUSO EM NUMEROS, inclua-o
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado!Não será readicionado')
    resposta = str(input('Dseja continuar? [S/N] '))
    if resposta in 'Nn': #aqui ele sintetizou o tamanho da condicional, dispensando um possivel else.
        break
numeros.sort()
print(f'voce digitou os valores {numeros}')