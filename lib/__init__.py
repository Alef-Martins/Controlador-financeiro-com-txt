from datetime import datetime

DataAtual= datetime.now()

def meses(mes):
    if mes == 1:
        mes = str('Janeiro')
    elif mes == 2:
        mes = str('Fevereiro')
    elif mes == 3:
        mes = str('Março')
    elif mes == 4:
        mes = str('Abril')
    elif mes == 5:
        mes = str('Maio')
    elif mes == 6:
        mes = str('Junho')
    elif mes == 7:
        mes = str('Julho')
    elif mes == 8:
        mes = str('Agosto')
    elif mes == 9:
        mes = str('Setembro')
    elif mes == 10:
        mes = str('Outubro')
    elif mes == 11:
        mes = str('Novembro')
    elif mes == 12:
        mes = str('Dezembro')
    return mes

def arquivoExiste(nome):
    try:
        a = open(nome, "rt+")#(rt)Lê um arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def total(arquivo):
    ler = open(arquivo, 'rt')
    total_liquido = 0
    c = 0
    linhas = []
    for linha in ler:
        linhas.append(linha)
        c += 1
    if c > 0:
        total_liquido = linhas[-1]
        total_liquido = float(total_liquido.replace(total_liquido[:7], ''))
    ler.close
    if not linhas:
        return 0
    else:
        return total_liquido

def entrada (arquivo, ganhos, despesas):
    total_ganhos = 0
    total_despesas = 0
    try:
        a = open(arquivo, 'a+')
    except:
        print('\033[31mERRO na leitura do arquivo\033[m')
    else:
        try:
            for c in range(0,len(ganhos)):
                total_ganhos += ganhos[c]
                total_despesas += despesas[c]
            a.write('_'*30 + '\n')
            a.write('----' + datetime.today().strftime('%d/%m/%Y - %H:%M') + '----\n')
            a.write(f'Ganhos     | Despesas\n')
            for c in range(0, len(ganhos)):
                a.write(f'{ganhos[c]:<10.2f} | {despesas[c]:.2f}\n')
            a.write('-'*20 + '\n')
            a.write(f'{total_ganhos:<10.2f} | {total_despesas:.2f}\n')
            a.write('_'*20 + '\n')
            a.write(f'Valor líquido: {total_ganhos + total_despesas:.2f}\n')  
            a.write(f'Saldo: {total(arquivo) + total_ganhos + total_despesas:.2f}\n')
            if total_ganhos + total_despesas >= 0:
                print(f'Valor líquido: \033[32m{total_ganhos + total_despesas:.2f}\033[m')
            else:
                print(f'Valor líquido: \033[31m{total_ganhos + total_despesas:.2f}\033[m')
            if total(arquivo) + total_ganhos + total_despesas >= 0:
                print(f'Saldo: \033[32m{total(arquivo) + total_ganhos + total_despesas:.2f}\033[m')
            elif total(arquivo) + total_ganhos + total_despesas < 0:
                print(f'Saldo: \033[31m{total(arquivo) + total_ganhos + total_despesas:.2f}\033[m')

        except:
            print('\033[31mERRO na escrita de dados\033[m')
        else:
            a.close   
