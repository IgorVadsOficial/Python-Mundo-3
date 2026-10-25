from time import sleep
alunos = []
dados = []
aluno = 0

while True:
    nome = str(input("Nome: ")).capitalize().strip()
    dados.append(nome)
    
    n1 = float(input("Nota 1: "))
    dados.append(n1)
    
    n2 = float(input("Nota 2: "))
    dados.append(n2)
    
    alunos.append(dados[:])
    dados.clear()
    
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper() [0]
    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        while continuar not in ["S","N"]:
            continuar = str(input("Quer continuar? [S/N] ")).strip().upper() [0]
            if continuar == "S":
                continue
            elif continuar == "N":
                break
print("-=" * 20)
print(f'{"N°"}    {"NOME"}       {"MÉDIA"}')
print("=" * 30)
for i in range(0, len(alunos)):
    print("{}    {}      {:.1f}".format(i,alunos[i][0],(alunos[i][1] + alunos[i][2]) / 2))
print("=" * 30)
while aluno != 999:
    aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if aluno == 999:
        break
    print(f"Notas de {alunos[aluno][0]} são {alunos[aluno][1:]} " )
print("FINALIZANDO...")
sleep(1)
print("<<< VOLTE SEMPRE >>>")