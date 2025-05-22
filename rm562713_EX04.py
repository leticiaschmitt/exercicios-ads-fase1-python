print("\nEXERCÍCIO 4 - RESGATE DE INVESTIMENTO\n")

while True:
    print("Tipo de investimento:\n1 - CDB\n2 - LCI\n3 - LCA")
    try:
        tipo = int(input("Escolha o tipo de investimento (1, 2 ou 3): "))
        if tipo in [1, 2, 3]:
            break
        else:
            print("Tipo inválido! Digite 1, 2 ou 3.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

while True:
    try:
        valor = float(input("Informe o valor a ser resgatado: R$ "))
        if valor > 0:
            break
        else:
            print("O valor deve ser maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite um valor numérico.\n")

while True:
    try:
        dias = int(input("Informe o número de dias aplicados: "))
        if dias > 0:
            break
        else:
            print("O número de dias deve ser maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.\n")

if tipo == 1:
    if dias <= 180:
        aliquota = 22.5
    elif dias <= 360:
        aliquota = 20
    elif dias <= 720:
        aliquota = 17.5
    else:
        aliquota = 15

    ir = valor * (aliquota / 100)
    valor_liquido = valor - ir

    print(f"\nTipo: CDB")
    print(f"Valor Bruto: R$ {valor:.2f}")
    print(f"Imposto de Renda ({aliquota}%): R$ {ir:.2f}")
    print(f"Valor Líquido do Resgate: R$ {valor_liquido:.2f}")

else:
    tipo_nome = "LCI" if tipo == 2 else "LCA"
    print(f"\nTipo: {tipo_nome}")
    print("Investimentos em LCI e LCA são isentos de IR.")
    print(f"Valor Resgatado: R$ {valor:.2f}")