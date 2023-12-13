'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
from math import prod

vetor = []
soma = 0
inteiros = 0
produto = 0

for i in range(5):
    num = int(input(f"Digite o {i+1} número: "))
    soma += num
    vetor.append(num)
    produto *= num

print(f"A soma nos números é {soma}, o produto {prod(vetor)} {produto} e os números digitados foram {', '.join(map(str, vetor))}")

