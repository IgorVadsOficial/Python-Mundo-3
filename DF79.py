numeros = []

while True:
    valor = int(input("Digite um valor: "))
    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado, Não vou adicionar...")
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

ordem_numeros = sorted(numeros)
print(f"Valores digitados: {ordem_numeros}")
