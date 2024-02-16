# 9.Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    reverso= str(numero)[::-1]
    return reverso

numero_inteiro= int(input('Digite um número inteiro: '))
print(reverso_numero(numero_inteiro))
