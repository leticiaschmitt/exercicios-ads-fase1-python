print("\nEXERCÍCIO 1 - VOTAÇÃO DO MELHOR DIA PARA A LIVE\n")

dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
votos = [0, 0, 0, 0, 0]

while True:
    try:
        qtd_colaboradores = int(input("Informe o número de colaboradores: "))
        if qtd_colaboradores > 0:
            break
        else:
            print("O número de colaboradores deve ser maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas um número inteiro.\n")

for i in range(qtd_colaboradores):
    while True:
        voto = input(f"Colaborador {i+1}, escolha um dia da semana para a live (ex: terça-feira): ").lower().strip()

        if voto in dias_semana:
            indice = dias_semana.index(voto)
            votos[indice] += 1
            break
        else:
            print("Dia inválido! Por favor, digite exatamente: segunda-feira, terça-feira, quarta-feira, quinta-feira ou sexta-feira.\n")

print("\nResultado da votação:")
for i in range(len(dias_semana)):
    print(f"{dias_semana[i].capitalize()}: {votos[i]} voto(s)")

maior_voto = max(votos)
dias_vencedores = [dias_semana[i] for i in range(len(votos)) if votos[i] == maior_voto]

if len(dias_vencedores) > 1:
    print(f"\nEmpate entre os dias: {', '.join([dia.capitalize() for dia in dias_vencedores])}")
else:
    print(f"\nDia escolhido para a live: {dias_vencedores[0].capitalize()}")