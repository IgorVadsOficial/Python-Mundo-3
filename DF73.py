tabela = (
	"Palmeiras",
	"Flamengo",
	"Athletico-PR",
	"Fluminense",
	"Bahia",
	"Bragantino",
	"Cruzeiro",
	"Botafogo",
	"Corinthians",
	"Atlético-MG",
	"Coritiba",
	"São Paulo",
	"EC Vitória",
	"Mirassol",
	"Santos",
	"Internacional",
	"Grêmio",
	"Vasco da Gama",
	"Remo",
	"Chapecoense",
)
print("-=-" * 30)
print(f"Lista de times: {tabela}")
print("-=-" * 30)
print(f"Os 5 primeiros colocados: {tabela[0:5]}")
print("-=-" * 30)
print(f"Os últimos 4 colocados da tabela: {tabela[16:]}")
print("-=-" * 30)
print(f"Times em ordem alfábetica: {sorted(tabela)}")

for pos, time in enumerate(tabela):
    if time == "Chapecoense":
        print("-=-" * 30)
        print(f"A {time} está na {pos+1}° posição.")
        print("-=-" * 30)