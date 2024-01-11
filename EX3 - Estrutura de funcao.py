# 3.Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def soma(n1,n2,n3):
    soma_argumentos= n1+n2+n3
    return soma_argumentos

num_list= []
for i in range(3):
    num= int(input(f'Digite o {i+1} número inteiro: '))
    num_list.append(num)

print(soma(num_list[0],num_list[1],num_list[2]))
