# 6.Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão 
# e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de 
# entrada todas as vezes que desejar.

def transformahora(tipo_hora,h):
    if tipo_hora == 1:
        if h==00:
            h= h+12
        elif h>=1 and h<13:
            h= h
        else:
            h= h-12
    if tipo_hora == 2:
        if h == 12:
            h= h
        elif h>=13 and h<00:
            h= h-12
        else:
            h= h+12
    return h   

def transformaminuto(tipo_hora,m):
    m
    return m

continuar= 0
import os   

while continuar != 1:
    clear= lambda: os.system('cls')
    clear()
    formato_hora= int(input('Digite o formato de hora que deseja 12 horas ou 24 horas: 1-(12) ou 2-(24)'))
    if formato_hora ==1:
        periodo_hora= input('Digite se o horário é AM ou PM, A(AM) ou P(PM)').upper() 
    horas= int(input('Digite as horas: '))
    minutos= int(input('Digite os minutos: '))

    if formato_hora == 1:
        if horas >=00 and horas<=12:
            periodo_hora= periodo_hora.replace('A','AM')
            print(transformahora(formato_hora,horas),':',transformaminuto(formato_hora,minutos),periodo_hora)
        else:
            periodo_hora= periodo_hora.replace('P','PM')
            print(transformahora(formato_hora,horas),':',transformaminuto(formato_hora,minutos),periodo_hora)

    if formato_hora == 2:
        print(transformahora(formato_hora,horas),':',transformaminuto(formato_hora,minutos))
    continuar= int(input('Deseja continuar?: Pressione 0-Continuar ou 1-Parar'))
    