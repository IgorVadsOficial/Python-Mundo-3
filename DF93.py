jogador = dict()
gols = list()
dados = 0
soma = 0

jogador["nome"] = str(input("Nome do Jogador: ")).capitalize().strip()
jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(jogos):
    dados = int(input(f"Quantos gols na partida {i}? "))
    gols.append(dados)
jogador["gols"] = gols[:]
for i in gols:
    soma = soma + i
jogador["total"] = soma
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k,v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {jogador["nome"]} jogou {jogos} partidas.")
for i,g in enumerate(gols):
    print(f"=> na partida {i}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")