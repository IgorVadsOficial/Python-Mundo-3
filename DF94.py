pessoas = []
mulheres = []
soma_idade = 0
cont = 0

while True:
    Continuar = "S"
    dados = dict()
    nome = str(input("Nome: ")).strip().capitalize()
    dados["nome"] = nome
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while sexo not in ["M", "F"]:
        sexo = str(input("Por favor, digite apenas M ou F ")).strip().upper()[0]
    dados["sexo"] = sexo
    idade = int(input("Idade: "))
    dados["idade"] = idade
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    soma_idade = soma_idade + idade
    cont += 1
    media = soma_idade / cont
    pessoas.append(dados)
    if sexo == "F":
        mulheres.append(nome)
    if continuar == "N":
        break
    elif continuar == "S":
        continue
    else:
        while continuar not in ["S", "N"]:
            continuar = (
                str(input("Por favor, digite apenas Sim ou Não! ")).strip().upper()[0]
            )

print("-=" * 30)
print(f"A) Ao todo temos {cont} pessoas cadastradas.")
print(f"B) A média de idade foi de {media:.2f} anos.")
mulheres = sorted(mulheres)
for mulher in mulheres:
    print(f"C) As mulheres cadastradas foram {' '.join(mulheres)}" )
print("D) Lista das pessoas que estão acima da média: ")
for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(pessoa)
print("<< ENCERRADO >>")
