def quantidade(tam):
    print("#"*tam)

opc1 = "s"


while(opc1 == "s" or opc1 == "S"):
    tam = int(input("Digite a quantidade desejada: "))

    quantidade(tam)
    opc1 = input("Gostaria de continuar? S/N \n")