# Faça um programa que use o método de busca binária para encontrar e imprimir a
# posição de um determinado elemento no vetor. Se o elemento não existir, seu
# programa deve imprimir o valor -1.
def busca_binaria(array, element, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2 #calcula meio
        if array[m] == element:
            return m
        if array[m] < element:
            return busca_binaria(array, element, begin=m+1, end=None)
        else:
            return busca_binaria(array, element, begin, end=m-1)
    return None
lista = [1,2,3,4,5]
elemento = 5
busca = busca_binaria(lista, elemento)
print(busca)