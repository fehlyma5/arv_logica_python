print("Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo")


ano_base = 2022
dn = int(input("Informe ano do nascimento: "))
sexo = int(input('''Informe orientação sexual: 
[1] Masculino.
[2] Feminino
[3] Outros
>>>'''))

ano_atual = (dn - 2022) * (-1)

if sexo == 1:
    print("Sigamos com as informações: ")
    if ano_atual == 18:
        print("quem nasceu em {} tem {} anos em {}\n"
              "voce deve se alistar IMEDIATAMENTE".format(dn, ano_atual, ano_base))
    elif ano_atual > 18:
        saldo = ano_atual - 18
        data_do_alistamento = dn + saldo
        print("quem nasceu em {} tem {} anos em {}\n"
              "Voce ja deveria ter se Alistado a {}.\n"
              "seu alistamento foi {}".format(dn, ano_atual, ano_base, saldo, data_do_alistamento))
    else:
        saldo = 18 - ano_atual
        data_do_alistamento = ano_atual + saldo
        print("quem nasceu em {} tem {} anos em {}\n"
              "Curta sua infancia, mas nao esqueça de se alistar daqui a {} anos.\n"
              "seu alistamento será {}".format(dn, ano_atual, ano_base, saldo, data_do_alistamento))
elif sexo == 3:
    print("Nesse caso deseja continuar com a guia de alistamento?")
    condicao = int(input("tecle [1] SIM; [2]NAO >>>"))
    if condicao == 1:
        if ano_atual == 18:
            print("quem nasceu em {} tem {} anos em {}\n"
                  "voce deve se alistar IMEDIATAMENTE".format(dn, ano_atual, ano_base))
        elif ano_atual > 18:
            saldo = ano_atual - 18
            data_do_alistamento = dn + saldo
            print("quem nasceu em {} tem {} anos em {}\n"
                  "Voce ja deveria ter se Alistado a {}.\n"
                  "seu alistamento foi {}".format(dn, ano_atual, ano_base, saldo, data_do_alistamento))
        else:
            saldo = 18 - ano_atual
            data_do_alistamento = dn + saldo
            print("quem nasceu em {} tem {} anos em {}\n"
                  "Curta sua infancia, mas nao esqueça de se alistar daqui a {} anos.\n"
                  "seu alistamento será {}".format(dn, ano_atual, ano_base, saldo, data_do_alistamento))
    elif condicao == 2:
        print("Respeitamos sua escolha, obrigado por nos visitar.")
elif sexo == 2:
    print("pessoas do sexo feminino não precisam fazer alistamento obrigatorio no exercito.")
else:
    print("Opção invalida, tente novamente.")


