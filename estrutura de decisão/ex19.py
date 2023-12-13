"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input("Digite um número inteiro menor do que 1000: "))

unidade = num % 10
dezena = (num // 10 ) % 10
centena = num // 100

print(f"{num} = {centena} centenas, {dezena} dezenas e {unidade} unidades")