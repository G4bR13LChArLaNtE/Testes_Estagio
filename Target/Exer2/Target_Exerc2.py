# Desenvolvedor: Julio Gabriel Charlante

''' Exercício 2:
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: 
	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.'''

#Resolução:

continua = True
while continua:
    try:
        n = int(input("Digite o número desejado: "))
        if (n < 0):
            raise TypeError
    except ValueError:
        print("O valor informado não é do tipo inteiro")
    except TypeError:
        print("O número deve ser positivo")
    except Exception:
        print("Ocorreu um erro.")
    else:
        continua = False

fib = []

pri = 0
seg = 0

while(seg < n):
    seg= seg + pri
    pri = seg - pri
    fib.append(seg)
    if(seg == 0):
        seg = seg + 1
if seg == n:
    print("{} pertence a sequência de Fibonacci.".format(n))
else:
    print("{} não pertence a sequência de Fibonacci!".format(n))
