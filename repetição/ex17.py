"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

n = int(input("Digite um número inteiro: "))
if  n < 0:
    print("O fatorial do número não existe!")
elif n == 0:
    print("O fatorial de 0 é igual a 1!")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial = fatorial * i
    print(fatorial)