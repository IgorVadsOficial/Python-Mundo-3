expressao = str(input("Digite a expressão: ")).strip()
cont = cont2 = 0

for i in expressao:
    if i == "(":
        cont += 1
    if i == ")":
        cont2 += 1

if cont == cont2:
    print("Sua expressão está valida!")
else:
    print("Sua expressão está errada!")