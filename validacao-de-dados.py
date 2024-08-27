print("execute um PG, q leia o sexo de uma pessoa, mas só aceite se for M ou F, caso esteja errado, peça para reiniciar")
print("-+" * 10)
sexo = str(input("\033[1;34m Informe seu sexo (M/F): \033[m")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("\033[4;31m Dados Invalidos. Por Favor Informe seu Sexo: \033[m")).strip().upper()[0]
print("\033[1;35m Sexo {} regitrado com sucesso \033[m".format(sexo))
