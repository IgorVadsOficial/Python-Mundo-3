from datetime import datetime

funcionario = dict()

funcionario["nome"] = str(input("Nome: ")).capitalize().strip()
funcionario["idade"] = int(input("Ano de nascimento: "))
funcionario["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if funcionario["ctps"] == 0:
    print(funcionario)
else:
    funcionario["contratação"] = int(input("Ano de Contratação: "))
    funcionario["salario"] = float(input("Salário: R$"))
    funcionario["aposentadoria"] = (
        (funcionario["contratação"] + 35) - datetime.now().year
    ) + funcionario["idade"]

print("-=" * 30)
for k, v in funcionario.items():
    print(f"{k} tem valor: {v}")
