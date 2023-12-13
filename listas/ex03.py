'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Notas: {', '.join(map(str, notas))}")
print(f"Notas: {notas}")
print(f"Média: {media}")
