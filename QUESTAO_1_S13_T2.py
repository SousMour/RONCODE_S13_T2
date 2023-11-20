#Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). 
# Depois, leia um valor inteiro constante. 
# O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.
lista=[]

while True:
    numero = int(input())
    if numero == 0:
        break 
    lista.append(numero)
constante = int(input())
multiplicado= [valor * constante for valor in lista]
print(multiplicado)


