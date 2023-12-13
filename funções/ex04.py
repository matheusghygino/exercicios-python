'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''


def argumento(arg):
    if arg > 0:
        print('P')
    else:
        print('N')

num = int(input('Digite um número inteiro: '))

argumento(num)