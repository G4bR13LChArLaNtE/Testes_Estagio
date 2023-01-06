pal1 = input("Digite a primeira palavra: ")
pal2 = input("Digite a segunda palavra: ")

def comparar(a, b):
    cont = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            if a[i] in b:
                cont += 1
    if cont == len(a):
        return "As duas palavras são anagramas"
    else:
        return "As duas palavras não são anagramas"

print(comparar(pal1, pal2))