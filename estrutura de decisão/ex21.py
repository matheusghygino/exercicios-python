"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

print("Bem vindo ao caixa eletrônico!")
saque = int(input("Quantos reais você quer sacar? "))
if saque < 10 or saque > 600:
    print("Valor de saque inválido! Digite um valor entre 10 e 600 reais!")

n100 = saque // 100
n50 = 0
n10 = 0
n5 = 0
n1 = 5

dezena = (saque // 10) % 10
if dezena >= 5:
    n50 = 1
    n10 = dezena - 5
elif dezena < 5:
    n10 = dezena

unidade = saque % 10
if unidade >= 5:
    n5 = 1
    n1 = unidade - 5
elif unidade < 5:
     n1 = unidade  
print(f"Você receberá {n100} notas de 100, {n50} notas de 50, {n10} notas de 10, {n5} notas de 5 e {n1} notas de 1")