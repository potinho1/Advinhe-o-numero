import random

jogadas = 0


while True:
    jogador = int(input("""Tente acertar o número que o computador está pensando!
    Números de 1 a 10\n"""))

    computador = random.randint(1, 11)

    if computador == jogador:
        print("Acertou!")
        break
    
    elif computador != jogador:
        jogadas += 1
        print("Tente novamente...\n")

print(f"Demorou {jogadas+1} rodadas para acertar!")