# Somatória de Pares até o Zero

soma_pares = 0
numero_digitado = 1 

while numero_digitado != 0:
        numero_digitado = int(input("Digite um número inteiro (ou 0 para encerrar): "))

        if numero_digitado != 0:  # Verifica se não é o zero de parada
            if numero_digitado % 2 == 0:  # Verifica se o número é par
                soma_pares += numero_digitado  # Adiciona à soma dos pares
                print(f"Número {numero_digitado} é par e foi adicionado à soma.")
            else:
                print(f"Número {numero_digitado} é ímpar e foi ignorado.")

    
print(f"A soma total dos números pares digitados é: {soma_pares}")