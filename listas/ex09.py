'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a {i+1}º idade: "))
    idades.append(idade)
    altura = float(input(f"Digite a {i+1}º altura: "))
    alturas.append(altura)

for i in range(4, -1, -1):
    print(f"{idades[i]} {alturas[i]}")