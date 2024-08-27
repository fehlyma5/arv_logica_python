print('Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista.\n'
      'Ja na posição correta de inserção (sem usar o sort), Mostrando no final a lista ordenada na tela.')
#vamos utilizar o metodo .insert()
# lista_numerica = []
# for lista in range(0,5):
#     lista_numerica.append(int(input('Informe um numero: ')))
#     pos = 0
#     while pos < len(lista_numerica):
#         if lista_numerica <= listanumerica[pos]:
#             lista_numerica.insert(pos, lista_numerica)
#             break
#         pos += 1
# print(lista_numerica)

#essa foi a minha tentativa de fazer sozinho
#VERSAO GUANABARA STUDIOS
lista_1 = []
for n in range(0,5):
    interacao_cliente = int(input('Digite um valor, vamos montar uma Lista: '))
    if n == 0 or interacao_cliente > lista_1[-1]:
        lista_1.append(interacao_cliente)
    else:
        posicao = 0
        while posicao < len(lista_1):
            if interacao_cliente <= lista_1[posicao]:
                lista_1.insert(posicao, interacao_cliente)
                break
            posicao += 1
print(lista_1)




