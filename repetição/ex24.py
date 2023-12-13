'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

n_notas = int(input("Digite o número dde notas que você irá calcular: "))
soma = 0
for i in  range(n_notas):
    nota = int(input(f"Digite o valor da {i+1}ª nota: "))
    soma += nota
    
media = soma / n_notas

print(f"Você digitou {n_notas} e a média aritmética delas é {media}")