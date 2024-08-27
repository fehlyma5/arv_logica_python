print('=' * 30)
print('        {BANCO CEV}        ')
print('=' * 30)
while True:
    inicio = str(input('Deseja realizar uma operação de Saque: (S- sim / N- nao)')).strip().upper()[0]
    if inicio == "S":
        saque = int(input('Informe o Valor que deseja Sacar: R$ '))
        tot = saque
        ced = 100
        totced = 0
        while tot >= ced:
            tot -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'O total de cedulas foram {totced} de R${ced}')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            elif ced == 2:
                op = str(input('deseja realizar outra Operação: (S- sim / N - nao)')).strip().upper()[0]
                resp = ' '
                while resp not in 'SN':
                    resp = str('deseja realizar outra Operação: (S- sim / N - nao)').strip().upper()[0]
                    if resp == 'S':
                        saque = int(input('Informe o Valor que deseja Sacar: R$ '))
                    elif resp == 'N':
                        break
    elif inicio == 'N':
        break
print('=' * 30)
print('\033[1;36m Obrigado por usar o BANCO CEV\n'
      'VOlTE SEMPRE\033[m')
