#Desenvolvedor: Julio Gabriel Charlante

'''Exercício 4: 

Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 

	SP – R$67.836,43 
	RJ – R$36.678,66 
	MG – R$29.229,88 
	ES – R$27.165,48 
	Outros – R$19.849,53 

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. '''

#Resolução:

faturamento = {'SP': 67836.43,
               'RJ': 36678.66,
               'MG': 29229.88,
               'ES': 27165.48,
               'OUTROS': 19849.53}

soma = 0
percentual = []
p = 0
estados = []

for i in faturamento:
    soma += faturamento[i]


for i in faturamento:
    p = faturamento[i] / soma
    percentual.append(p)

for k in faturamento.keys():
    estados.append(k)
 
for i in range(len(estados) - 1):
    print("O percentual de representação que o {} teve no faturamento foi de {:.2f}%.".format(estados[i], (percentual[i] * 100)))
    
print("O percentual de representação que os {} estados tiveram foi de {:.2f}%.".format(estados[-1], (percentual[-1] * 100)))