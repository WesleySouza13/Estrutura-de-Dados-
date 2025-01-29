#Exercício 1: Busca Linear
# Dado o seguinte vetor de números inteiros:
arr = [3, 5, 7, 9, 2, 8, 6, 4]
elemento = 10
# Implemente uma função de busca linear para encontrar o número 8 neste vetor. Retorne o índice do número encontrado ou -1 se o número não estiver presente.

def BL(array, element):
    for i in range(len(array)):
        if arr[i] == element:
            return i
        
    return None
a = BL(arr, element=elemento)
print(a)