print('Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:'
'''A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista''')

valores = []
while True:
    valores.append(int(input('insira um numero ')))
    resp = str(input('Deseja continuar: S/N '))
    if resp in 'Nn':
        break
print(f'A quantidade de  numeros digitados foram {len(valores)} elementos')
valores.sort(reverse=True)
print(f'A lista dos valores em ordem derescente é {valores}')
if 5 in valores:
    print('O numero 5 esta contido na lista')
else:
    print('o 5 nao foi digitado')

#o programa ta rodando porem a resposta de S/N ta aceitando receber valores tipo inteiro o que atrapalha o programa