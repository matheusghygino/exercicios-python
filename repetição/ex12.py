"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50"""
    
num = int(input("Digite um número inteiro entre 1 e 10 para que seja gerada a tabuada do mesmo: "))
while num <= 0 or num > 10:
    num = int(input("Valor inválido! Digite um número inteiro entre 1 e 10 para que seja gerada a tabuada do mesmo: "))

for i in range(10):
    tabuada = num * (i + 1)
    print(f"{num} x {i + 1} = {tabuada}")    