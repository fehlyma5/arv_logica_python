print("melhore o programa de progressao aritmetica, perguntando se o usuario quer inluir mais termos, ate q ele informe que nao quer mais digitando 0")
primeiro = int(input("Entre com o valor incial da PA: "))
razao = int(input("Entre com o valor da Razao: "))
termo = primeiro
cont = 1
total = 0
mais = 10 #ta recebendo 10 pk a pa já deve mostrar logo de inicio os 10 primeiros termos e depois perguntar se quer mais
while mais != 0: #enquanto a variavel MAIS for diferente de 0
    total += mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        cont += 1
    print("\033[34m PAUSA\033[m")
    mais = int(input("\033[4;36m Quantos termos voce quer adcionar a mais?\033[m >>> "))
print("\033[1;31m progressao finalizada com {} termos\033[m".format(total))

#nao entendi como foi colocado no segundo while cont menor ou igual a total
#e o print usou o Termo no format
#aqui aprendemos que condições whiles tambem podem ser aninhadas dentro de outro while, as possibilidades são muitas