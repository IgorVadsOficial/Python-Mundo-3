numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

numeros_t = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

n = int(input("Digite um número entre 0 e 20: "))

while not 0 <= n <= 20:
    n = int(input("Tente novamente. Digite um número entre 0 e 20: "))

for i in numeros:
    if n == i:
        print(f"Você digitou o número {numeros_t[i]}.")
