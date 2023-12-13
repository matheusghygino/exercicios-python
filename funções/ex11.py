"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""

from datetime import datetime

def data_por_extenso(data):
    try:
        data = datetime.strptime(data, '%d/%m/%Y')
        return data.strftime('%-d de %B de %Y')
    except ValueError:
        return None

data = '25/10/2023'
data_formatada = data_por_extenso(data)
if data_formatada is not None:
    print(data_formatada)
else:
    print('Data inválida')
