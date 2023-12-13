"""Faça um programa que leia 5 números e informe a soma e a média dos números"""
soma = 0
for i in range(5):
    num = float(input(f"Digite o {i + 1} número: "))
    soma = soma +  num

media = soma / (i + 1)

print(f"A média dos números digitados é {media}")