print("Elabore um programa q leia o nome e o preço  de varios produtos\n"
      "[a] qual o total gasto na compra;\n"
      "[b] quantos produtos custam mais de 1000;\n"
      "[c] qual é o nome do produto mais barato.")
print("-=" * 40)
totgast = tot1000 = totbarat = cont = 0
barato = " "
while True:
    produto = str(input("Informe o nome do produto: "))
    valor = float(input("Informe O preço do produto: R$ "))
    cont += 1
    totgast += valor
    if valor > 1000:
        tot1000 += 1
    if cont == 1 or valor < totbarat:
        totbarat  = valor
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("\033[1;33m Deseja continuar : (S/N): \033[m")).strip().upper()[0]
    if resp == "N":
        break
print("O total gasto na compra foi de R${}\n"
      "{} foram os produtos acima de 1000;\n"
      "e o item mais barato foi {} que custa R${:.2f} reais .".format(totgast, tot1000, barato, totbarat))
