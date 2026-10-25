lista = []
maior = menor = 0

for i in range(0,5):
    n = int(input(f"Digite um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado no final da lista...")
    elif n < lista[0]:
        lista.insert(0,n)
        print(f"Adicionado na posição 0 da lista...")
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos +=1
print("-=-" * 30)
print(f"Os valores digitados em ordem foram: {lista}")