numeros = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        pares.append(valor)
        numeros.append(valor)
    else:
        impares.append(valor)
        numeros.append(valor)
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
print(f"Todos os números que você digitou foram: {numeros}")
print(f"Todos os números PARES que você digitou foram: {pares}")
print(f"Todos os números IMPARES que você digitou foram: {impares}")
