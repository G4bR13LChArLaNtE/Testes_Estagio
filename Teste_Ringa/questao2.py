status = True

while(status):
    fila_frente = input("Digite as alturas (em Cm) dos alunos da fila da frente, deixando um espaço entre cada número: ")
    fila_atras = input("Digite as alturas (em Cm) dos alunos da fila de trás, deixando um espaço entre cada número: ")

    if len(fila_atras) == len(fila_frente) or len(fila_atras) >= 2 and len(fila_frente) >= 2:
        frente = fila_frente.split(" ")

        tras = fila_atras.split(" ")


        lista1 = []

        lista2 = []

        cont = 0

        for i in range(len(frente)):
            lista1.append(int(frente[i]))

        for i in range(len(tras)):
            lista2.append(int(tras[i]))

        for i in range(len(lista1) ):
            if lista1[i] < lista2[i]:
                cont = cont + 1

        if cont == len(lista1):
            result = True
            print(result)
        else:
            result = False
            print(result)
            
        status = False

    else:
        print("As filas tem que ter o mesmo número de alunos e são formadas de pelo menos por 2 alunos!")
        print("Digite outra vez!")
        