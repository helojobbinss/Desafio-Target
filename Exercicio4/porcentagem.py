def porcentagem(valor):
    porcentagem = (100 * valor)/180759.98
    return porcentagem

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53
total = SP+RJ+MG+ES+Outros
print("A porcentagem de São Paulo em relação ao total é ", porcentagem(SP),"%")
print("A porcentagem do Rio de Janeiro em relação ao total é ",porcentagem(RJ),"%")
print("A porcentagem de Minas Gerais em relação ao total é ",porcentagem(MG),"%")
print("A porcentagem do Espírito Santo em relação ao total é ",porcentagem(ES),"%")
print("A porcentagem dos outros estados em relação ao total é ",porcentagem(Outros),"%")