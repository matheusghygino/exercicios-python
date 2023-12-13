"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500."""

""" num = 0
    ultimo = 1
    penultimo = 1
    while num <= 500:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        num += 1
        if termo < 500:
            print(termo)
        else:
        break"""

a, b = 0, 1

while b <= 500:
    print(b)
    a, b = b, a + b # a = b  b = a + b