"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

n = int(input("Quantos números você quer comparar? "))
maior = 0
menor = 0
soma = 0
for i in range(n):
    num = int(input(f"Digite o {i + 1}º número: "))
    while num < 0 or num > 1000:
        num = int(input("Digite um número entre 0  1000: "))
    soma = soma + num
    if num >= maior:
        maior = num
    elif menor <= num:
        menor = num
print(f"A soma dos números digitados é {soma}, o maior valor foi {maior} e o menor foi {menor}")