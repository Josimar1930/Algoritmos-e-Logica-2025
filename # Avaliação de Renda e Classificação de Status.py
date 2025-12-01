# Avaliação de Renda e Classificação de Status

nomes = []
rendas = [] 
status_aprovacao = []
while True:
    nome = input("Digite o nome do candidato (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    renda = float(input("Digite a renda do candidato: "))
    
    nomes.append(nome)
    rendas.append(renda)
    
    if renda > 2500.00:
        status_aprovacao.append("Aprovado")
    else:
        status_aprovacao.append("Reprovado")

soma_rendas_aprovadas = 0
contador_aprovados = 0
for i in range(len(nomes)):
    if status_aprovacao[i] == "Aprovado":
        soma_rendas_aprovadas += rendas[i]
        contador_aprovados += 1
if contador_aprovados > 0:
    media_rendas_aprovadas = soma_rendas_aprovadas / contador_aprovados 
else:
    media_rendas_aprovadas = 0

print("Vetor de Nomes:", nomes)
print("Vetor de Status:", status_aprovacao)
print("Média das Rendas Aprovadas: R$", round(media_rendas_aprovadas, 2))