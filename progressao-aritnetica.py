print("==" * 10, end="\n"
                     "10 termos de uma PA\n"
                     "")
print("==" * 10)
termo1 = int(input("Digite primeiro termo: "))
termo2 = int(input("Digite segundo termo: "))
dec = termo1 + (10 -1) * termo2
for pa in range (termo1, dec, termo2):
    print("{}".format(pa), end="- ")
print("Finish")

#termo2 no caso é a razao da pa (ou seja é quem informa quantas casas serão puladas

