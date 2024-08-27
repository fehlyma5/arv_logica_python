print("Crie uma logica que verifique em qual classificação do IMC o peso do usuario esta\n"
      "dada a formula peso(Kg) / (altura x altura) em metros")

genero = int(input('''Qual a classificação do seu Genero: \n"
[1] MASCULINO
[2] FEMININO
[3] OUTROS
Digite o numero correspondente a sua resposta: >>>'''))
print("Voce digitou a opção {}".format(genero))
if genero > 3:
    print("Opção invalida, Tente Novamente.")

peso = float(input("Entre com o valor do Peso: "))
altura = float(input("Entre com o valor da Altura: "))
imc = peso / (altura ** 2)
print("Seu Indice de massa corporal é {:.2f}".format(imc))
if imc > 40:
    print("Grupo de Obesidade grau III. Procure orientação médica IMEDIATAMENTE")
elif imc >=35:
    print("Grupo de Obesidade grau II. Procure fazer adequações na dieta e busque praticar exercicios")
elif imc >=30:
    print("Grupo de Obesidade grau I. Buque cuidar mais de si")
elif imc >= 25:
    print("Grupo de Sobrepeso. Pratique exercicios")
elif imc >= 18.5:
    print("Grupo Normal. Mantenha seus cuidados em dia.")
else:
    print("\033[1;37m Grupo Magreza. Busque orientação médica\033[m")