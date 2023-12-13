"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""
print("Nos informe uma data como for pedido a seguir!")
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if dia < 1 or dia > 30:
    print("Valor inválio para dia! Por favor informe um valor entre 1 e 30!")
elif mes < 1 or mes > 12:
    print("Valor inválido para o mês! Por favor informe um valor entre 1 e 12!")
elif ano < 1:
    print("Valor inválido para ano! Por favor informe um valor maior do que zero!")
else:
    print(f"{dia}/{mes}/{ano}")