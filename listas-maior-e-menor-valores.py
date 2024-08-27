print('Faça um programa que leia 5 valores numericos e guarde-os em uma lista. NO final, mostre qual foi o maior \n'
      'e o menor valor digitado e as suas respectivas posiçoes na lista')
listanum = []
maximo = 0 #TAVA TENTANDO USAR A MERDA DO METODO MAX() MAS NAO DEU CERTO
minimo = 0
for i in range(5):
    listanum.append(int(input('Digite um numero para montar-mos uma lista: '))) #SEM O APPEND NAO TAVA DANDO PARA GERAR UMA LISTA
    if i == 0:
        maximo = minimo = listanum[i] #aqui estamos declarando que nao se sabe qual o valor menor e o maior se o numero é inicial
    else:
        if listanum[i] > maximo:
            maximo = listanum[i] #aqui estamos especificando a partir do numero inicial
        if listanum[i] < minimo:
            minimo = listanum[i]
print(f'\033[33m Sua lista com os valores digitados é {listanum}')
print( f'O valor maximo digitado foi {maximo} nas posições: ', end='')
for c, v in enumerate(listanum): #aqui
    if v == maximo:
        print(f'{c}...', end='')
print(f'\n O valor de menor destaque foi {minimo} nas posições: \033[m', end='')
for c, v in enumerate(listanum):
    if v == minimo:
        print(f'{c}...', end='')
print() #aqui ele quebra de linha indicando final do programa

# lista2 = listanum ...>>> NAO CONSEGUI DEIXAR ESSA POHA EM ORDEM CRESCENTE
# lista2.sort(listanum)
# print(lista2)
