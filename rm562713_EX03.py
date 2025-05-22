print("\nEXERCÍCIO 3 - TABELA DE EMPRÉSTIMOS\n")

while True:
    try:
        valor_divida = float(input("Informe o valor da dívida (ex: 25000): R$ "))
        if valor_divida > 0:
            break
        else:
            print("O valor deve ser maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite um valor numérico válido (ex: 25000).\n")

print("\nTabela de opções de parcelamento:")
print(f"{'Parcelas':>10} | {'Juros':>6} | {'Valor Juros':>12} | {'Total Dívida':>14} | {'Valor Parcela':>15}")
print("-" * 65)

parcelas_juros = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

for parcelas, juros in parcelas_juros:
    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    print(f"{parcelas:>10} | {juros:>5}% | R$ {valor_juros:10.2f} | R$ {valor_total:12.2f} | R$ {valor_parcela:13.2f}")
