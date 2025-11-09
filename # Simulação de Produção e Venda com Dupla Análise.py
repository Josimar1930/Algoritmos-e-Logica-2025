# Simulação de Produção e Venda com Dupla Análise

numero_lotes = int(input("Informe a quantidade de lotes a serem simulados: "))

custo_fixo = 100

# lista vazia
lista_custo_por_lote = []

# Laço de repetição
for i in range (1,numero_lotes + 1):
    numero_unidades_produzidas = int(input(f"Informe o número de unidades produzidas no lote {i}: "))
    if numero_unidades_produzidas > 50:
        c_var_unidade = 1.50
    elif 20 <= numero_unidades_produzidas <= 50:
        c_var_unidade = 2.00
    else:
        c_var_unidade = 3.00
    custo_lote = custo_fixo + (numero_unidades_produzidas * c_var_unidade)

    lista_custo_por_lote .append (custo_lote)

# Parte 2 
p_base_venda_unid = 5.00

# variaveis
lucro_total_acumulado = 0
lotes_com_lucro_alto = 0

for i in range (len(lista_custo_por_lote)):
    custo_lote = lista_custo_por_lote[i]

    receita = 50 * p_base_venda_unid
    lucro = receita - custo_lote
    lucro_total_acumulado += lucro

    if lucro > 100:
        lotes_com_lucro_alto += 1
        print(f"Lote {i+1} Aprovado: Lucro Alto.")
    elif lucro > 0:
        print(f"Lote {i+1} Aceitável: Lucro Mínimo.")
    else:
        print(f"Lote {i} Reprovado: Prejuízo.")

print(f"Lucro Total Acumulado: R$ {lucro_total_acumulado:.2f}")
print(f"Quantidade de Lotes com Lucro Alto: {lotes_com_lucro_alto}")
