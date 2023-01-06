lista = [10, 20, 10, 20, 10, 30, 20, 50, 10]
listaOrg = lista.sort()



def numeroParesMeias(lista):
    num = 0
    cont = 0
    for i in range(0, len(lista)):
        if lista[i] != lista[i - 1]:
            num = lista.count(lista[i])
            cont += (num//2)
    return cont

print(numeroParesMeias(lista))