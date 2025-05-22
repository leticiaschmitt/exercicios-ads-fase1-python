print("\nEXERCÍCIO 2 - TABELA DE PARCELAMENTO DO CARRO\n")

while True:
    try:
        valor_carro = float(input("Informe o valor do carro (ex: 25000): R$ "))
        if valor_carro > 0:
            break
        else:
            print("O valor deve ser maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite um valor numérico válido (ex: 25000).\n")

desconto_vista = valor_carro * 0.20
preco_vista = valor_carro - desconto_vista
print(f"\nPara pagamento à vista, o valor com 20% de desconto é R$ {preco_vista:,.2f}")

parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
percentuais = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print("\nConfira as opções de parcelamento:\n")

for i in range(len(parcelas)):
    acrescimo = valor_carro * (percentuais[i] / 100)
    preco_final = valor_carro + acrescimo
    valor_parcela = preco_final / parcelas[i]
    print(f"O preço final parcelado em {parcelas[i]}x é de R$ {preco_final:,.2f}, com parcelas de R$ {valor_parcela:,.2f}")
