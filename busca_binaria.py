#algoritmo de busca binaria 
def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        me = (begin + end)//2
        if array[me] == item:
            return me
        if array[me] < item:
            return binary_search(array, item, me + 1, end)  
        else:
            return binary_search(array, item, begin, me - 1)  
    return None
lista = [2, 3, 4, 5]
busca = binary_search(lista, 5)
print(busca)
