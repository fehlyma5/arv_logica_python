print("Crie um programa que calcule a soma entre todos os numeros impares q são multiplos de 3 (entre 1 e 500")
print("@-@"*10)
cont = 0
soma = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
        print(num, end=" ")
print("A soma de todos os numeros é {} os valores sao {}".format(cont, soma))
print("finished")
#a gente declarou cont +1 pra contar todos os valores multiplos de 3 entre a condição estabelecida de 1 a 500
#e fez as respectivas soma de cada um dos valores que apareceram numa condição dentro do If (soma + a variavel declarada no for que aqui foi num
