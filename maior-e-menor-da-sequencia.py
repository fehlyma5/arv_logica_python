print("um pg q lleia o peso de 5 pessoas e identifique qual o maior e qual o menor")
print("=-"*10)
maior = 0
menor = 0
for p in range (1, 6):
    valor = float(input("Entre com {} do usuario: ".format(p)))
    if p == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print("O MENOR peso estabelecido foi de {}kg \n"
      "Já o MAIOR peso foi de {}kg".format(menor, maior))

#usamos dois IF dentro de um ELSE, para utilizarmos o primeiro valor dado como referencia para os proximos
