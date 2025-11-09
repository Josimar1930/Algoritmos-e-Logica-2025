# Import random
import random

numero_secreto = random.randint(1, 10) 
tentativas = 0
acertou = False
palpite_usuario = 0 

print("Tente adivinhar o número secreto (entre 1 e 10).")


while not acertou:
    
    palpite_usuario = int(input("Seu palpite: "))
    
    if palpite_usuario < 1 or palpite_usuario > 10:
        print("Palpite fora do intervalo. Tente um número entre 1 e 10.")
        continue

    tentativas += 1

    if palpite_usuario == numero_secreto:
        acertou = True 
        print("\n*** Parabéns! Você acertou! ***")
    else:
    
        print("Errado. Tente novamente.")

print(f"O número sorteado era: {numero_secreto}")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")