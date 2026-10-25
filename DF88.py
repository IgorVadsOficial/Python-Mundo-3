from time import sleep
from random import randint

jogo = []

print("=" * 45)
print("           JOGA NA MEGA SENA")
print("=" * 45)

jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(1, jogos + 1):
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    print(f"Jogo {i}: {sorted(jogo)}")
    sleep(1)
    jogo.clear()
print("-=-=-=-= < BOA SORTE! > -=-=-=-=")
