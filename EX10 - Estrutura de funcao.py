# 10.Jogo de Craps. 
# Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e 
# ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random
import os

continuar = 0
lista_dados= []

while continuar != 1:
    print('Olá jogador vamos jogar Craps.')
    iniciar= input('Precione ENTER para começar.')
    dado1= random.randint(2,6)
    dado2= random.randint(2,6)
    soma_dados= dado1 + dado2
    if soma_dados in lista_dados:
            print('Você PERDEU!!!')
            break
    lista_dados.append(soma_dados)
    if soma_dados == 7 or soma_dados == 11:
        print(f'Você tirou {soma_dados} um natural e ganhou PARABÉNS!!!')
        lista_dados.clear()
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        print(f'Você tirou {soma_dados} um craps e PERDEU!!!')
        lista_dados.clear()
    else:
        print(f'Você tirou um ponto {soma_dados}, e deve tirar um natural para ganhar, se tirar {soma_dados} ou craps perde.')
    print(lista_dados)
    continuar= int(input('Gostaria de jogar Craps? 0-Sim ou 1-Não: '))
    
 
    