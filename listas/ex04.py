'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

caracteres = []

for i in range(10):
    caractere = input(f'Digite o {i+1}ª caractere: ')
    caracteres.append(caractere)
 
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

quantidade_consoantes = 0
consoantes_lidas = []

for caractere in caracteres:
    if caractere.lower() in consoantes:
        quantidade_consoantes += 1
        consoantes_lidas .append(caractere)

print(f"Quantidade de consoantes lidas: {quantidade_consoantes}")
print(f"Consoantes lidas: {', '.join(consoantes_lidas)}")