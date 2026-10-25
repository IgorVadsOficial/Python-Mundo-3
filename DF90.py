aluno = dict()
aluno["nome"] = str(input("Nome: ")).capitalize().strip()
aluno["media"] = float(input("Media: "))

print("-=" * 30)
print(f"- Nome do aluno é igual a {aluno["nome"]}")
print(f"- Média é igual a {aluno["media"]}")

if aluno["media"] < 5.0:
    print("Situação: REPROVADO")
elif aluno["media"] >= 5.0 and aluno["media"] < 7.0:
    print("Situação: RECUPERAÇÃO")
elif aluno["media"] >= 7.0:
    print("Situação: APROVADO")
