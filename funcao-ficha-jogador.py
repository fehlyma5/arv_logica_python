print("Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:\n"
      " o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, \n"
      "mesmo que algum dado não tenha sido informado corretamente.")
print("="*100)

def ficha (jog ="desconhcido", gol = 0):
      print(f"o jogador {jog}  fez {gol} gols")


njogador = str(input("digite nomedo jogador: "))
gol = str(input("Informe a quantidade de gols marcados"))
if gol.isnumeric():
      gol = int(gol)
else:
      gol = 0
if njogador.strip() == '':
      ficha(gol = gol)
else:
      ficha(njogador, gol)

