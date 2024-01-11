# 5.Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
# expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,altera):
    taxaImposto= (imposto/100)*custo
    altera= custo+taxaImposto
    return altera

custo= int(input('Digite o valor de custo do produto: '))
imposto= int(input('Digite o valor do percentual da alíquota do imposto: '))

print('R$',somaImposto(custo,imposto))