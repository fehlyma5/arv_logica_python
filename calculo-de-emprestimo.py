print('\033[1;32m Crie um programa para aprovar um emprestimo bancario para compra de uma casa\n'
      'considerando valor da casa, salario do comprador e quantidade de tempo\033[m')

Valor_Casa = float(input("Diga-nos qual valor da casa pretende financiar: "))
Salario_Base = float(input("Conte-nos qual sua faixa salarial: "))
Qtde_Tempo = int(input("Agora Informe em quanto tempo pretende quitar as prestações: "))
Condição = (Salario_Base / 100) * 30
#print(Condição)
Calculo = (Valor_Casa / Qtde_Tempo)
if Condição >= Calculo:
    print("Seu Financiamento foi Aprovado, Parabens!!!")
else:
    print("\033[4;31m Seu Financiamento não atende os requisitos minimos, tente na proxima \033[m")
#teve a mesma logica seguida pelo Guanabara. Mas foi uma resolução muito básica, do tipo "sou filho da minha mae e do meu pai"
#dava pra ter colocado um print autoexplicativo que informasse as condições. Dava pra incluir som de acordo com o resultado, dava pra calcular juros, podia ter colocado o simbolo do dinheiro
