print("versao oficial do Guanabara para o jogo")
print("=" * 30)
from random import randint
vit = 0
while True:
    jogador = int(input("qual sua jogada: "))
    computador = randint(0 , 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("\033[1;32m Digite 'P' para PAR e 'I' para IMPAR \033[m")).strip().upper()[0]
    print(f"Jogador jogou {jogador} X Computador jogou {computador}. Resultado: {total}")
    print("Deu PAR" if total % 2 == 0 else "Deu Impar")
    if tipo == "P":
        if total % 2 == 0:
            print("\033[1;32m Voce VENCEU. Continue jogando...\033[m")
            vit += 1
        else:
            print("\033[1;31m Voce PERDEU.\033[m")
            break
    elif tipo == "I":
         if total % 2 == 1:
            print("\033[1;32m Voce VENCEU. Continue jogando...\033[m")
            vit += 1
         else:
            print("\033[1;31m Voce PERDEU.\033[m")
            break
    print("-=" * 30)
print(f"GAME OVER... \n"
      f"jogador venceu {vit} vezes")
