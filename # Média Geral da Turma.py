# Média Geral da Turma 

numero_de_alunos = int(input("Digite o número de alunos a serem avaliados (máximo 5): "))
if numero_de_alunos > 5:
    print("Número máximo de alunos é 5. Ajustando para 5.")
    numero_de_alunos = 5
dados_brutos = []
for i in range(numero_de_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota_pratica = int(input(f"Digite a nota do trabalho prático de {nome}: "))
    nota_teorica = int(input(f"Digite a nota da prova teórica de {nome}: "))
    dados_brutos.append(nome)
    dados_brutos.append(nota_pratica)
    dados_brutos.append(nota_teorica)
soma_medias = 0
alunos_acima_media = 0
for j in range(0, len(dados_brutos), 3):
    nome_aluno = dados_brutos[j]
    nota_pratica = int(dados_brutos[j + 1])
    nota_teorica = int(dados_brutos[j + 2])
    media = (nota_pratica * 0.6) + (nota_teorica * 0.4)
    soma_medias += media
    if media > 7.0:
        alunos_acima_media += 1
        print(f"{nome_aluno} - Situação: Excelente (Média: {media:.2f})")
    elif 5.0 <= media <= 7.0:
        print(f"{nome_aluno} - Situação: Necessita Revisão (Média: {media:.2f})")
    else:
        print(f"{nome_aluno} - Situação: Reprovado.")
media_geral = soma_medias / numero_de_alunos
print(f"Média Geral da Turma: {media_geral:.2f}")
print(f"Total de Alunos Acima da Média: {alunos_acima_media}")