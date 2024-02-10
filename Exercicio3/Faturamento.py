import json
with open('Exercicio3\dados.json', encoding='utf-8') as meu_json:
    dados=json.load(meu_json)

maximo = 0
minimo = 10000
soma = 0
dia = 1
faturamento_max = []
for i, v in enumerate (dados):
    if(int(dados[i]['valor']) != 0.0):
        soma = soma + int(dados[i]['valor'])
        dia = dia+1
    if(minimo >= int(dados[i]['valor'])):
       if(int(dados[i]['valor']) != 0.0):
            minimo = dados[i]['valor']
    if(maximo<= int(dados[i]['valor'])):
        maximo = dados[i]['valor']
media = soma/dia
for i,v in enumerate (dados):
    if(int(dados[i]['valor']) >= media):
        faturamento_max.append(int(dados[i]['dia']))

print("O valor mínimo de faturamento é :",minimo)
print("O faturamento máximo é: ",maximo)
print("O faturamento foi maior que o faturamento mensal nos dias: ",faturamento_max)
    
