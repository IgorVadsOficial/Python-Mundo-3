valores = [[], []]

for i in range(1, 8):
    n = int(input(f"Digite o {i}° valor: "))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print("-=" * 30)
print(f"Pares: {sorted(valores[0])}")
print(f"Impares: {sorted(valores[1])}")
