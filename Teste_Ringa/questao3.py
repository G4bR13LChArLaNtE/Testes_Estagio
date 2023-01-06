entrada = input("Digite a string a ser comprimida: ")

x = 0

lista = []

for j in entrada:
    for i in range(len(entrada)):
        if j == entrada[i]:
            x = x + 1
        elif (j != entrada[i]) and x > 1:
            