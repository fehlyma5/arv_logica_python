print('\033[1;33mCrie um Radar eletronico que verifique a velocidade  informe o motorista se ele esta em um limite aceitavel\n'
      'Ou se ultrapassou o limite estabelecido e calcule a multa por excesso de velocidade\033[m')

velocidade = float(input("qual a velocidade em que o veiculo esta?"))
if velocidade > 80:
    print("\033[4;31mO veiculo foi MULTADO por excesso de Velocidade. (Limite Permitido 80km/h)\033[m")
    multa = (velocidade - 80) * 7
    print("A multa por excesso deverá ser {}".format(multa))
print("\033[1;36mTenha um bom dia, Dirija sempre com Segurança!\033[m")