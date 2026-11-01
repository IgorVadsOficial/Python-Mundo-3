from time import sleep


def contador(a, b, c):

    for i in range(a, b, c):
        print(f"{i}", end=(" "))
        sleep(0.5)
    print("FIM!")


print("-=" * 30)
print("Contagem de 1 até 10 de 1 em 1")
for i in range(1, 11, 1):
    print(f"{i}", end=(" "))
    sleep(0.5)
print("FIM!")
print("-=" * 30)

print("Contagem de 10 até 0 de 2 em 2")
for i in range(10, -1, -2):
    print(f"{i}", end=(" "))
    sleep(0.5)
print("FIM!")
print("-=" * 30)

print("Agora é sua vez de personalizar a contagem! ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("-=" * 30)
print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
contador(inicio, fim, passo)
print("-=" * 30)
