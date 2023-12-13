'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
todos = []
par = []
impar = []

for i in  range(20):
    num = int(input("Digite um número: "))
    todos.append(num)
    if num <= 0:
        continue
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Esse é o vetor com todos os números: {', '.join(map(str, todos))}, este o com os números pares: {', '.join(map(str, par))} e este com os ímpares: {', '.join(map(str, impar))}")
