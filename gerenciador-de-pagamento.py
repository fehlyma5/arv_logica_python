print("Elabora um programa que calcule o valor a ser pago por um produto:\n"
      "considerando seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO, (DINHEIRO, CARTAO A/V OU A PRAZO")

produto1 = float(input("Entre com o valor do produto: R$"))
print('''Confirme a forma de pagamento:
\033[1;34m [1] a vista (dinheiro ou Pix)\033[m
\033[1;35m [2] cartao a vista (debito ou credito 1x)\033[m
\033[1;36m [3] cartao 2x\033[m
\033[1;32m [4] cartao 3x ou mais\033[m''')
opcao = int(input("Digite a forma dde pagamento desejada: "))
if opcao == 1:
    total = produto1 -(produto1 * 10 / 100)
    print("Voce ganhou Desconto de 10% pelo Pagamento a vista")
elif opcao == 2:
    total = produto1 - (produto1 * 5 / 100)
elif opcao == 3:
    total = produto1
    parcela = produto1 / 2
    print("O valor da compra permanece inalterado para pagamento em 2x sem Juros\n"
          "com 2 parcelas de {:.2f}".format(parcela))
elif opcao == 4:
    total = produto1 + (produto1 * 20 / 100)
    qtdd_parc = int(input("Digite em quantas vezes deseja realizar o pagamento (ex: 18x):>>> "))
    parcela = produto1 / qtdd_parc
    print("Voce optou por dividir sua compra em {}x. Ficando com parcelas de {:.2f}".format(qtdd_parc, parcela))
else:
    total = produto1
    print("\033[1;31m Opção Invalida, por favor tente novamente.\033[m")
print("Sua compra de R${} ficou por {:.2f} no final".format(produto1, total))
