# 4.Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento 
# for zero ou negativo.

def valor_caract(n):
    if n > 0:
        n= 'P'
    else:
        n= 'N'
    return n

num= int(input('Digite um valor inteiro positivo, negativo ou zero: '))

print(valor_caract(num))