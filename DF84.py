pesadas = []
leves = []
maior = menor = 0
cont = 0

while True:
    nome = str(input("Nome: ")).capitalize().split()
    peso = float(input("Peso: "))
    cont += 1

    if cont == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
        pesadas.clear()
        pesadas.append(nome)
    elif peso == maior:
        pesadas.append(nome)

    if peso < menor:
        menor = peso
        leves.clear()
        leves.append(nome)
    elif peso == menor:
        leves.append(nome)

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        while continuar not in ["S", "N"]:
            continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
            if continuar == "S":
                continue
            elif continuar == "N":
                break

print("-=" * 30)
print(f"Ao todo, você cadastrou {cont} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de {pesadas[:]}.")
print(f"O menor peso foi de {menor}Kg. Peso de {leves[:]}.")
