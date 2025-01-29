# Exercício 2: Busca Binária
# Dado o seguinte vetor ordenado de números inteiros:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# implemente uma função de busca binária para encontrar o número 7 neste vetor. Retorne o índice do número encontrado ou -1 se o número não estiver presente.

def BB(array, element, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <=end:
        m = (begin+end)//2
        if array[m] == element:
                return m
        if array[m] < element:
            return BB(arr, element, m+1, end)
        else:
            return BB(arr, element, begin, m-1)
    return -1
BB(arr, 7)