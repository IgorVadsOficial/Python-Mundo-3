palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)

for p in palavras:
    print(f"\nNa palavra {p} temos: ", end="")
    for l in p:
        if l.lower() in "aeiou":
            print(l, end=" ")
