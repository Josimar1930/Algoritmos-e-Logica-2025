# Cálculo de Imposto sobre Notas Fiscais

numero_notas_fiscais = int(input("Digite a quantidade de notas fiscais: "))

soma_das_notas = 0.0


for i in range(numero_notas_fiscais):
    nota = float (input(f"Digite o valor da nota fiscal {i + 1}: "))
    soma_das_notas += nota 
if soma_das_notas <= 100:
    aliquota = 0.05
elif soma_das_notas >= 1000 and soma_das_notas<= 4999.99:
    aliquota = 0.09
elif soma_das_notas >= 5000 and soma_das_notas <= 14999.99:
    aliquota = 0.12
else:
    aliquota = 0.16
valor_imposto = soma_das_notas * aliquota

print(f"Valor total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota * 100:.2f}%")
print(f"Valor total do imposto a ser pago: R$ {valor_imposto:.2f}")