print('fazendo uma progressao artmetica com razao, mostrando os 10 primeiros termos')
primeiro = int(input("entre com o primeiro termo: "))
razao = int(input("entre com a razao da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razao
    cont += 1
print("FIM")