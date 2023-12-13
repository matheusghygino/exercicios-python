"""Faça um programa que leia 5 números e informe o maior número."""
maior = 0
for c in range(5):
    num = int(input("Digite um número inteiro: "))
    if num > maior:
        maior = num
        
        
print(maior)           