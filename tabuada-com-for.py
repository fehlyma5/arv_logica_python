print("a formula correta de fazer tabuada")
from time import sleep
tab = int(input("Entre com o numero: "))
for tabuada in range (1, 11):
    print("{} x {:2} = {}".format(tab, tabuada, tab*tabuada))
    sleep(0.5)
print("finish")
#se compararmos com a primeira versao do execicio qu foi feita de forma sequencial. Temos uma otimização em termos de codigos e linhas
#no print colocamos a variavel tab, para rodar de forma estatica
#na sequencia declaramos a variavel do for aqui no caso tabuada que traduzida roda os numeros de 1 a 10
#na terceira formatação do .format colocamos a multiplicação para rodar entre as variaveis TAB e TABUADA
