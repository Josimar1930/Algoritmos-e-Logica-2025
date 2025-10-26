# Cálculo de Imposto sobre Notas Fiscais

numer_de_notas = int(input("Digite a quantidade de notas fiscais: "))
soma_das_notas = 0.0
for _ in range(numer_de_notas):

    valor_nota = float(input("Digite o valor da nota fiscal: R$ "))
    soma_das_notas += valor_nota

if soma_das_notas <= 100.00:
    aliquota = 0.05    

elif 1000.00 <= soma_das_notas <= 4999.99:
    aliquota = 0.09 

elif 5000.00 <= soma_das_notas <= 14999.99:
    aliquota = 0.12

else:
    aliquota = 0.16 

valor_imposto = soma_das_notas * aliquota
print(f"Valor total das notas: R$ {soma_das_notas:.2f}")   
print(f"Alíquota aplicada: {aliquota * 100:.2f}%")

valor_imposto = soma_das_notas * aliquota
print(f"Valor total do imposto a ser pago: R$ {valor_imposto:.2f}")