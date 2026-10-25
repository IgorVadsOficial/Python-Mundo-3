matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor [{i}] [{j}]: "))

print("-=" * 30)
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
