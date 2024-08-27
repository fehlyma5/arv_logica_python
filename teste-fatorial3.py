n = int(input('entre com o numero:'))
c = n
f = 1
print("calulando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))

#o na versao anterior desse mesmo ex. tava errando pk tava colando o fatorial (F) para receber - = 1
#testei com o fatorial de 1 milhao mas demora muito, porem funciona