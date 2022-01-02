from datetime import datetime
import lib
import os


ano = str(datetime.today().year)

if not os.path.exists(ano):
    os.makedirs(ano)

mesN = str(datetime.today().month)
mes = (datetime.today().month)
mes = lib.meses(mes)
arquivo = str(mesN + '-' + mes)

if not lib.arquivoExiste(arquivo):
    os.chdir(ano)
    #lib.CriaArquivo(arquivo)

despesas = []
ganhos = []
data = [datetime.today().strftime('%d/%m/%Y - %H:%M')]
while True:
    entrada = float(input('Entre com o valor: '))
    if entrada == 0:
        break
    elif entrada < 0:
        despesas.append(entrada)
    else:
        ganhos.append(entrada)

if not despesas:
    despesas.append(0)
if not ganhos:
    ganhos.append(0)
if len(despesas) > len(ganhos):
    while len(despesas) > len(ganhos):
        ganhos.append(0)
if len(ganhos) > len(despesas):
    while len(ganhos) > len(despesas):
        despesas.append(0)

lib.entrada(arquivo, ganhos, despesas)
