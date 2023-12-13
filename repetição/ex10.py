"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""

num = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num > num2:
    maior = num
    menor = num2
else: 
    maior = num2
    menor = num

for i in range((maior -  menor) -1):
    print((i + 1) + menor)