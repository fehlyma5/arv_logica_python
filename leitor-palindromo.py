print("execute um programa que identifique se a frase é ou nao um palindromo, desonsiderando os espaços")
frase = str(input("Entre com a frase: ")).strip().upper() #eliminou os epaços antes e depois e colocou tudo pra maiusculo
#tentei usar o reversed porem tomei um erro
palavras = frase.split() #gerou uma lista
junto = ''.join(palavras) #juntou tudo em estring so
inverso = ''
for pali in range (len(junto) -1, -1, -1): #foi da ultima letra ate a primeira voltando uma letra
    inverso += junto[pali]
print("o inverso de {} é {}".format(junto, inverso))
if inverso == junto: #aqui testou se era
    print("temos um palidromo")
else:
    print("A frase digitada nao é um palindromo")
