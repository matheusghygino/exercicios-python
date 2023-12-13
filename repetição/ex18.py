"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

n = int(input("Quantos números você quer comparar? "))
soma = 0
num = int(input("Digite o 1º número: "))
menor = num
maior = 0
for i in range(n -1):
    num = int(input(f"Digite o {i + 2}º número: "))
    soma = soma + num
    if num >= maior:
        maior = num
    elif num <= menor:
        menor = num
print(f"A soma dos números digitados é {soma}, o maior valor foi {maior} e o menor foi {menor}")