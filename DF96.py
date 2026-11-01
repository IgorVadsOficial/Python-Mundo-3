def area(l, c):
    a = l * c
    print(f"A área de um terreno {l:.1f}x{c:.1f} é {a:.1f}m².")


print("Controle de Terrenos".center(20))
print("-" * 20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
