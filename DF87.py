matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_c = 0
maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor [{i}] [{j}]: "))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma_c += matriz[i][j]
        if i == 1 and j == 0:
            maior = matriz[i][j]
        if i == 1 and matriz[i][j] > maior:
            maior = matriz[i][j]
print("-=" * 30)
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
print("-=" * 30)
print(f"Soma de todos os valores = {soma}")
print(f"Soma de todos os valores da terceira coluna = {soma_c}")
print(f"O maior valor da segunda linha = {maior}")
