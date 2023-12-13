"""Faça um programa  que peça um número inteiro  dtermine se ele é par ou impar."""

num = int(input("Digite um númro inteiro para que o programa lhe diga se ele é par ou ímpar: "))

if num // 2 == 0:
    print("O número é par")
elif num == 0:
    print(f"O número digitado foi {num} e é um número neutro!")
else:
    print("O número é ímpar!")