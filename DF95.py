jogadores = list()

while True:
    jogador = dict()
    gols = list()
    continuar = "S"

    nome = str(input("Nome do Jogador: ")).strip().capitalize()
    jogador["nome"] = nome

    jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador["jogos"] = jogos

    for i in range(1, jogos + 1):
        dados = int(input(f"Quantos gols na partida {i}? "))
        gols.append(dados)

    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)

    jogadores.append(jogador)

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
    elif continuar == "S":
        continue
    else:
        while continuar not in ["S", "N"]:
            continuar = (
                str(input("Por favor, digite apenas Sim ou Não! ")).strip().upper()[0]
            )

print("-=" * 30)
print(f"{'cod':<4}{'nome':<25}{'gols':<20}{'total':<5}".center(60))
print("-" * 60)
for i, jogador in enumerate(jogadores):
    print(
        f"{i:<4}{jogador['nome']:<25}{jogador['gols']!s:<20}{jogador['total']:<5}".center(
            60
        )
    )
print("-" * 60)
cod = 0
while cod != 999:
    cod = int(input("Quer mostrar dados de qual jogador? (999 para parar) "))
    if cod == 999:
        break
    elif cod < 0 or cod >= len(jogadores):
        print(f"ERRO! Não existe jogador com o código {cod}!")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[cod]['nome']}.")
        for i, gols in enumerate(jogadores[cod]["gols"], start=1):
            print(f"No jogo {i} fez {gols} gols.".center(60))
