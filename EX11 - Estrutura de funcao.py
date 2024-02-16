# 11.Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, 
# valide a data e retorne NULL caso a data seja inválida.


import datetime
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

def mes_por_extenso (dma):
    dma= data_mes_ano.split('/')
    data= dma[0]
    mes= dma[1]
    ano= dma[2]
    for i,meses_ano in enumerate(meses):
            cont= i+1
            if cont == mes:
                k= data,' de ',meses_ano,ano
    return k


data_mes_ano= input('Digite a data, mês e ano (DD/MM/AAAA): ')
print(mes_por_extenso(data_mes_ano))