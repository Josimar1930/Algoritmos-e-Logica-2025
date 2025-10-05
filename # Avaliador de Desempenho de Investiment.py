# Avaliador de Desempenho de Investimento 

R_investimento = float(input("Informe o retorno do investimento (%): "))
R_livre = float(input("Informe a taxa livre de risco (%): "))
sigma = float(input("Informe o desvio-padrão da volatilidade (%): "))

if sigma == 0:
    print("Erro: Sigma não pode ser zero para cálculo de sharp Ratio.")
else:
    sharp = (R_investimento - R_livre)/ sigma
    spread = R_investimento - R_livre

if sharp > 1.5 and spread > 0.05:
    classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
elif 0.5 <= sharp <= 1.5 or spread > 0.02:
    classificacao = "Investimento Bom: Risco e retorno moderados."

elif sharp < 0.5 and R_investimento > 0:
    classificacao = "Investimento Aceitavel: Retorno poditivo, mas risco alto para o ganho."
else:
    classificacao = "Ivestimento Ruim: Não recomendado."

print(f"Sharp Ratio: {sharp:.2f}")
print(classificacao)