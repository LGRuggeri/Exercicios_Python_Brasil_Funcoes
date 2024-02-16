# 8.Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informando.
# Reverso do número. 

def reverso_numero(numero):
    contador_numero= len(str(numero))
    reverso= str(numero)[::-1]
    return contador_numero,reverso

numero_inteiro= int(input('Digite um número inteiro: '))
print(reverso_numero(numero_inteiro))
