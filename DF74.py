from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maior = 0
menor = 0

print("\n") 
print(f"Numeros = {numeros}")

for pos, i in enumerate(numeros):
    if pos == 0:
        maior = i
        menor = i
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print("\n")        
print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print("\n") 