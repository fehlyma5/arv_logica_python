print("crie um programa que leia x numeros da sequencia de fibonacci")
#o que se entende da sequencia de Fibonacci, q ele a partir de 0 e 1 passa a somar os 2 valores adjascentes gerando um terceiro resultado e assim suscetivamente ate o infinito
n1 = int(input("quantos termos vc quer mostrar: "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end="")
cont = 3 #contador ta recebendo 3 pk já informamos os dois primeiros termos
while cont <= n1:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2 #o antigo valor de t2 passa a ser t1
    t2 = t3 #o antigo valor de t3 passa agora ser t2 - PARA PODER IR CALCULANDO OS 2 ultimos termos
    cont += 1
print("-> fIM")