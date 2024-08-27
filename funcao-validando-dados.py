def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;031m ERROR!!! Digite um numero INTEIRO para continuar. \033[m")
        if ok:
            break
    return valor


#programa principal
n = leiaInt("Informe um numero: ")
print(f"o numero digitado foi {n}")