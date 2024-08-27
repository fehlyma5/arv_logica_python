def area (larg, comp):
    a = larg * comp
    print(f"o valor da area com {larg} largura X {comp}comprimento é igual a {a} metros quadrados")

l = float(input("Informe o valor de largura: (m) "))
c = float(input("Informe o valor de comprimento: (m) "))
area(l, c) #tem que chamar dentro dos parenteses as variaveis corresponentes as propriedades declaradas na função
print("fim do programa")