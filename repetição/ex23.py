"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

num = int(input("Digite um número inteiro maior do que 1: "))
div = 0

for i in range(num):
    if num % (i+1) == 0:
        print('')
        