#Escreva um programa que ler a nota de 50 alunos. 
# Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).

notas= []
for i in range(50):
    nota = float(input())
    notas.append(nota)

indices = [i for i, nota in enumerate(notas) if nota >= 6]

print(indices)
