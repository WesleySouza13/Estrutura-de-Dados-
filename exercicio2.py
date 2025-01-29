#dado uma lista x e um elemento y, retorne onde esse elemento esta utilizando a busca linear
x = [3,9,12,9,0,8,7]
y = 8

def busca_linear(x,y): #onde x é lista e y o elemento 
    for i in range(len(x)):
        if x[i]== y:
            return i
    return None
        
            
busca_linear = busca_linear(x=x,y=y)
print(busca_linear)