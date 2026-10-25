numeros = []
cont = 0

while True:
    valor = int(input("Digite um valor: "))
    numeros.append(valor)
    cont += 1
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper() [0]
    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        while continuar not in ["S","N"]:
            continuar = str(input("Quer continuar? [S/N] ")).strip().upper() [0]
            if continuar == "S":
                continue
            elif continuar == "N":
                break

numeros.sort(reverse=True)

print("-=-" * 22)
print(f"Você digitou {cont} elementos.")

print(f"Os valores em ordem decrescente são: {numeros}")

if 5 in numeros :
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")