entrada = input("Digite a lista de numero inteiros, deixando um espaço entre cada número: ")

lista = entrada.split(" ")

listaInt = []

for i in range(len(lista)):
    listaInt.append(int(lista[i]))

soma = int(input("Digite a soma alvo: "))

listaSoma = []

for i in listaInt:
    for j in range(len(listaInt)):
        if i != listaInt[j] and (listaInt[j] + i) == soma:
            listaSoma.append(i)

listaSoma.sort()

print(listaSoma)