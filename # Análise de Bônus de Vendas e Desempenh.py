# Análise de Bônus de Vendas e Desempenho

V_base = float(input("Digite o valor base do bônus (R$): "))
P_ind = float(input("Digite a pontuação de performance individual (0 a 100): "))
P_equipe = float(input("Digite a pontuação da meta da equipe (0 a 100): "))

if P_ind > 90:
    FAP = 1.25
elif P_ind > 70:
    FAP = 1.10
elif P_ind > 50:
    FAP = 1.00
else:
    FAP = 0.80

B_ajustado = V_base * FAP


if P_equipe > 85:
    
    if P_ind > 95 or B_ajustado > 5000:
        print("\nBônus Máximo (30% Extra).")
        B_final = B_ajustado * 1.30
    else:
        print("\nBônus Padrão (10% Extra).")
        B_final = B_ajustado * 1.10

elif 60 <= P_equipe <= 85:
   
    if P_ind < 60:
        print("\nPenalidade por Desempenho Individual (15% de Redução).")
        B_final = B_ajustado * 0.85
    else:
        print("\nSem Alteração Adicional.")
        B_final = B_ajustado
else:
    
    print("\nPenalidade Severa (25% de Redução).")
    B_final = B_ajustado * 0.75

print(f"Valor Base do Bônus: R$ {V_base:.2f}")
print(f"Fator de Ajuste Aplicado (FAP): {FAP:.2f}")
print(f"Bônus Ajustado (antes da meta): R$ {B_ajustado:.2f}")
print(f"Bônus Final (após ajustes): R$ {B_final:.2f}")