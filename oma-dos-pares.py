print("desenvolva um pg q leia 6 numeros inteiros, e mostre a soma apenas dos pares. Se fo impar, desconsiderar")
soma = 0
cont = 0
for par in range(1, 7):
    num = int(input("Entre com o valor {}: ".format(par)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print("A quantidade de numeros PARES foi {} e a soma dos numeros pares digitados foi {}".format(cont, soma))

#quando se vai trabalhar com for Lembrar de um CONTADOR e um SOMATORIO; Precisa declarar como variavel começando com 0