# 1.Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. 
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def n_inteiro(n):
    num_int= n
    return num_int
  
num_inteiro= int(input('Digite um número inteiro: '))

for i in range(num_inteiro):
    num_repete= n_inteiro(num_inteiro)
    print(num_repete,end=' ')
