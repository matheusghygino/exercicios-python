"""Altere o programa anterior para mostrar no final a soma dos números."""

num = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num > num2:
    maior = num
    menor = num2
else: 
    maior = num2
    menor = num
total = 0
for i in range((maior -  menor) -1):
    soma = (i +  1) + menor
    total += soma
    print(total)    