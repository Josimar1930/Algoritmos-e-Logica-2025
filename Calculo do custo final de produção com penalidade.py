#Calculo do custo final de produção com penalidade

custo_inicial = float(input("Digite o custo inicial do material: "))
Q = int(input("Digite a quantidade de itens produzidos: "))
dias  = int(input("Digite o número de dias de atraso: "))
defeito = float(input("Digite o percentual de defeitos: "))

if Q > 1000 and custo_inicial > 5000:
    fator = 1.15
else:
    fator = 1.05

c_corrigido = custo_inicial * fator

if defeito > 0.10 or dias > 5:
    print("Penalidade Alta: 20% de redução no lucro.")
    c_final = c_corrigido * 1.25
elif 0.05 <= defeito <= 0.10 and dias >0:
    print("Penalidade média: 10% de redução no lucro:")
    c_final = c_corrigido * 1.10
else:
    print("Sem penalidade. Custo final apenas com correção.")
    c_final = c_corrigido

print(f"Custo Base corrigido: R${c_corrigido:.2f} ")
print(f"Custo final do lote: R${c_final}")