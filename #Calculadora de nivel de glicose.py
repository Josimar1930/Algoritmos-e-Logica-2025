#Calculadora de nivel de glicose

valor = float(input("Digite o valor da glicose em jejum: "))

if valor < 100:
    print("Glicemia normal.")
elif valor >= 100 and valor <= 125:
    print("Pré-Diabetes: Risco Moderado.")
else:
    print("Diabetes: Nivel Alto.")