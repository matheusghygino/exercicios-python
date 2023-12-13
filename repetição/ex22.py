"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."""

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
    for i in range(num):
        if num % (i+1) == 0:
            dividido = (1+1)
            print(dividido)
    print(f"O número digitado foi o {num} e ele é par")
    