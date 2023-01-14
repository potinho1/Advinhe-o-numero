import random

jogadas = 0

while True:
    computador = random.randint(1, 11)

    jogador = int(input("Teste acertar o número que o computador está pensando de 1 a 10\n"))

    if computador == jogador:
        print("Acertou!")
        break
    
    elif computador != jogador:
        jogadas += 1
        print("Teste novamente\n")

print(f"Demorou {jogadas+1} rodadas para acertar!")