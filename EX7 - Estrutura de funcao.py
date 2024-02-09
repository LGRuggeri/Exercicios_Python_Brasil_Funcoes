# 7.Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma 
# prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número 
# de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a 
# ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor 
# a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e 
# assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o 
# programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor 
# total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
# mais 0,1% de juros por dia de atraso.

def valorPagamento(valor_prestacao,dias_atraso):
    if dias_atraso > 0:
        valor_juros= (valor_prestacao*0.03) + (dias_atraso*0.001)
        valor_prestacao= valor_prestacao + valor_juros
    else:
        valor_prestacao= valor_prestacao
    return valor_prestacao
        
import os
valor_pagar= True
lista_valores= []
valor_total= 0
quantidade_total= 0

while valor_pagar != 0:
    clear= lambda: os.system('cls')
    clear()
    valor_pagar= float(input('Digite o valor da prestação: '))
    if valor_pagar == 0:
        break
    else:
        dias_em_atraso= int(input('Digite quantos dias em atraso: '))
        lista_valores.append(valorPagamento(valor_pagar,dias_em_atraso))
      
      
print('Quantidade prestação','Valor total')    
valor_total= sum(lista_valores)
quantidade_total= len(lista_valores)
print(f'      {quantidade_total}              R${valor_total:,.2f}')
    

