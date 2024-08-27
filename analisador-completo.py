print('''Produza um analisador completo que consiga interpretar:
[1] nome do homem mais velho;
[2] o valor da idade media ddo grupo;
[3] quantas mulheres tem menos de 20 anos''')
print("x-"*10)
somaid = 0
mediaid = 0
m_i_h = 0
nomevelho = ''
totmulher20 =0
outros = "Genero não Relacionado"
for p in range (1, 5):
    print("----- {}º PESSOA----".format(p))
    nome = str(input("Digite o NOME: ")).strip()
    idade = int(input("Informe a IDADE: "))
    genero = str(input("Informe GENERO (M/F):")).strip()
    somaid += idade
    if p == 1 and genero in "Mm":
        m_i_h = idade
        nomevelho = nome
    if genero in "Mm" and idade > m_i_h:
        m_i_h = idade
        nomevelho = nome
    if genero in "Ff" and idade < 20:
        totmulher20 += 1

mediaid = somaid / 4
print("A media de idade do grupo é de {} anos\n"
      "O nome do Homem mais velho é {} e sua idade é {}\n"
      "No grupo há {} mulheres com idade inferior a 20 anos".format(mediaid, nomevelho, m_i_h, totmulher20))

#nao consegui entender muito bem a linha 18 a 23, porque basicamente se repetiu o cod