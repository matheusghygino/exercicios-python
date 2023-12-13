"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
par = 0
impar = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Foram digitados {par} números pares e {impar} números ímpares: ")