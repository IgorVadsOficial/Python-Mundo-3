valores = ((int(input(f"Digite o 1° número: "))),(int(input(f"Digite o 2° número: ",))),(int(input(f"Digite o 3° número: ",))),(int(input(f"Digite o 4° número: ",))))

if 9 in valores:
    print(f"O número 9 apareceu: {valores.count(9)} vezes.")
else:
    print(f"O número 9 apareceu 0 vezes.")

if 3 in valores:
    print(f"O número 3 apareceu primeiro na {valores.index(3)+1}° posição.")
else: 
    print("O valor 3 não foi digitado em nenhuma posição.")

print("Os númemros pares foram: ")
for i in valores:
    if i % 2 == 0:
        print(end=f"{i} ")

