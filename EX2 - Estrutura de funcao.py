# 2.Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. 
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def n_inteiro(n):
    num_int= n
    return num_int
 
cont= 0
  
num_inteiro= int(input('Digite um número inteiro: '))

for i in range(num_inteiro):
    cont+=1
    print(n_inteiro(cont),end=' ' )