#funçao busca linear
def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return None

lista = [1, 3, 4, 5, 5, 7]
elemento = 5
linear = linear_search(lista, elemento)
if linear is not None:
    print(f'o indice do elemento é {linear} na lista {lista}')
else:
    print('nao esta na lista')

