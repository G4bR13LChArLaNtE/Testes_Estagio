#Desenvolvedor: Julio Gabriel Charlante

''' Exercício 5: 

Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
	b) Evite usar funções prontas, como, por exemplo, reverse. '''

#Resolução:

def inverte_palavras():
    frase = input("Por favor, digite a frase desejada: ")
    quant = len(frase)
    cont = quant
    while cont > 0:
        print(frase[cont - 1], end="")
        cont -= 1

inverte_palavras()