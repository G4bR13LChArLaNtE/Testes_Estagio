#Desenvolvedor: Julio gabriel Charlante

''' Exercício 3:
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
	• O menor valor de faturamento ocorrido em um dia do mês;
	• O maior valor de faturamento ocorrido em um dia do mês;
	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média. '''
 
#Resolução:

import json

with open('dados.json', 'r') as json_arq:
    dados = json.load(json_arq)
 
 
cont = 0 
soma = 0
valores = []
dias = []


for i in dados:
    soma += i['valor']
    if i['valor'] > 0:
        cont += 1
        valores.append(i['valor'])


media = soma/cont


for i in dados:
    if i['valor'] > media:
        dias.append(i['valor'])



print("O menor valor de faturamento diário desse mês foi: R${:.4f}".format(min(valores)))
print("O maior valor de faturamento diário desse mês foi: R${:.4f}".format(max(valores)))
print("O total de dias que o faturamento ultrapassou a média foi: {} dia(s).".format(len(dias)))