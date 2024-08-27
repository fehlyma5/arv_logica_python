temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append((float(input('PESO: '))))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('DESEJA CONTINUAR [S/N]: '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O peso maior foi {maior}kg ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}kg ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()