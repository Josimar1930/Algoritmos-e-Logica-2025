# Calculadora de investimento com rentabilidade condicional

P = float(input("Digite o valor inicial do investimento: "))
T = int(input("Qual o prazo do investimento em mêses: "))

if T < 6:
    J = 0.005
elif T >= 6 and T <= 12:
    J = 0.008
elif T > 12:
    J = 0.012
rendimento_total = P * J * T

print(f"Taxa de juros= {J}%")
print(f"Rendimento = {rendimento_total}")