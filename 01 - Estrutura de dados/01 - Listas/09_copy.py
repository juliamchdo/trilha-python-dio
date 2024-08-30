lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy() # a mesma lista com os valores criados inicalmente, porém em uma instância diferente

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista)) #instâncias diferentes