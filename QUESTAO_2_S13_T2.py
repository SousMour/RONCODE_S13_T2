#Escreva um programa que leia uma lista com 100 números. 
# Ao término da leitura o programa deve fazer a ordenação dos números lidos. 
# Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5. 
# DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.
lista=[]

for _ in range(100):
    numeros = int(input())
    lista.append(numeros)
    lista.sort()

resultado = [valor * 3 if indice % 2 == 0 else valor * 5 for indice, valor in enumerate(lista)]

print(resultado)


