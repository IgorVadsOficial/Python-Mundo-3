# valores = [int(input(f"Digite o 1° valor: ")),int(input(f"Digite o 2° valor: ")),int(input(f"Digite o 3° valor: ")),int(input(f"Digite o 4° valor: ")),int(input(f"Digite o 5° valor: "))]
valores = []
maior = menor = 0
pos_final_maior = pos_final_menor = 0
pos = 0

for i in range(0, 5):
    valores.append(int(input(f"Digite o valor para a posição {pos}: ")))
    if pos == 0:
        maior = valores[i]
        menor = valores[i]
    if valores[i] > maior:
        maior = valores[i]
        pos_final_maior = pos
    if valores[i] < menor:
        menor = valores[i]
        pos_final_menor = pos
    pos += 1
print("=-=" * 40)
print(f"Você digitou os valores: {valores}")
print(f"\nO maior valor foi {maior} na posições ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}... ", end="")
print(f"\nO menor valor foi {menor} na posições ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}... ", end="")
