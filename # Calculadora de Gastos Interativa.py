# Calculadora de Gastos Interativa

gastos_semanais = []
continuar = "sim"   
while continuar.lower() == "sim":
    gasto = float(input("Digite o valor do gasto do dia: "))
    gastos_semanais.append(gasto)
    continuar = input("Deseja adicionar outro gasto? (sim/não): ")  

gasto_total = 0       
for gasto in gastos_semanais:
    gasto_total += gasto

print("Gastos Semanais:", gastos_semanais)  
print("Gasto Total da Semana: R$", gasto_total)