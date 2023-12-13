"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

num = int(input("Digite um número inteiro para saber se ele é primo ou não: "))
div = 0
for i in range(num):
    if num % (i+1)  == 0:
        div += 1
    i += 1
if div == 2:
    print(f'O número digitado foi o {num} e ele é primo')
elif num == 0:
    print(f"O número digitado foi o {num} e ele n é par nem ímpar")
else:
    print(f"O número digitado foi o {num} e ele é par")