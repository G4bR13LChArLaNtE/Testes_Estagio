def quantidade(tam):
    print("#"*tam)

opc1 = ""
opc = True

while(opc):
    tam = int(input("Digite a quantidade desejada: "))

    quantidade(tam)
    opc1 = input("Gostaria de continuar? S/N \n")
    if opc1 == "S" or opc1 == "s":
        opc = True
    else:
        opc = False