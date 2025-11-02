# Avaliação de Estoque com Fator de Risco

num_produtos = int(input("Digite o número total de produtos a serem analisados: "))

valor_total_estoque = 0.0
produtos_alto_risco = 0

for i in range(1, num_produtos + 1):
    print(f"Produto {i}:")
    preco_unitario = float(input("Digite o preço unitário (R$): "))
    quantidade_estoque = int(input("Digite a quantidade em estoque: "))

    
    valor_bruto = preco_unitario * quantidade_estoque

   
    if quantidade_estoque > 100:
        
        valor_total_estoque += valor_bruto * 1.05
    elif preco_unitario > 50 and quantidade_estoque <= 10:
        
        produtos_alto_risco += 1
        valor_total_estoque += valor_bruto
    else:
        
        valor_total_estoque += valor_bruto
print(f"Valor Total Final do Estoque: R$ {valor_total_estoque:.2f}")
print(f"Número de Produtos de Alto Risco: {produtos_alto_risco}")