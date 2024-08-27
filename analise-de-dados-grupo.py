#cont = 0
#while True:
#    id = int(input("entre com a idade: "))
#    genero = str(input("Informe Sexo M/F: ")).strip().upper()[0]
#    media = str(input("Deseja Continuar [S/N]: ")).strip().upper()[0]
#    while media == "S":
#        id = int(input("entre com a idade: "))
#        genero = str(input("Informe Sexo M/F: ")).strip().upper()[0]
#        media = str(input("Deseja Continuar [S/N]: ")).strip().upper()[0]
#    if
#    else:
#        print("Encerrando o programa...")
#        break
print("="*30)
contM20 = cont18 = contM = 0
while True:
    idade = int(input("informe idade: "))
    sexo = " "
    while sexo not in "MF": #enquanto o sexo nao for M ou F ele repete a pergunta
        sexo = str(input("Qual seu genero: M/F: ")).strip().upper()[0]
    if idade <= 18:
        cont18 += 1
    if sexo == "M":
        contM += 1
    if sexo == "F" and idade < 20:
        contM20 += 1
    resp = " "
    while resp not in "S/N":
        resp = str(input("Deseja continuar: (S/N): ")).strip().upper()[0]
    if resp == "N":
            break
print("No grupo há {} homens \n"
      "{} mulheres com menos de 20\n"
      "e {} menores que 18 anos.".format(contM, contM20, cont18))

