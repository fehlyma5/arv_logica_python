print("Crie um programa que leia duas noas do aluno e calcule sua media. Mostrando mensagem no final se o aluno foi Aprovado, reprovado, ou esta de recuperação")

aluno = float(input("Entre com a nota 1: "))
aluno2 = float(input("Entre com a nota 2: "))
media = (aluno + aluno2) / 2
if media == 10.0:
    print("Seu rendimento foi Perfeito. Parabens voce foi APROVADO com a media final maxima {}".format(media))
elif 9.0 > media >= 7.0:
    print("Sua media foi Boa. Parabens voce foi aprovado com a media {}".format(media))
elif 6.9 > media >= 4.5:
    print("voce esta de RECUPERAÇÃO, sua media de {} foi regular".format(media))
else:
    print("Voce foi REPROVADO, sua media foi de {}".format(media))

# APRENDI com o Guanabara a usar 9 > media >= 7  ou tbm seria possivel: media >= 4 and < 7

