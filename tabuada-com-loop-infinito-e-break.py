print("\033[5;46m Faça um programa que mostre a tabuada de vários números, um de cada vez, \n"
      "para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. \033[m")
cont = tabuada = 1
while True:
    num = int(input("Digite o numero para ver sua tabuada: "))
    if num == -1: #aqui coloquei igual a -1 mas o ideal seria colocar < 0
              break
    for tabuada in range (1,11):
        print(f"{num} x {tabuada :2} = {num * tabuada}")
    novo = int(input("Deseja continuar, press [1 - para SIM / 2 - para NAO]: "))
    if novo == 1:
         print(num)
    else:
         print("Finalizando Programa ....")

print("finish")
