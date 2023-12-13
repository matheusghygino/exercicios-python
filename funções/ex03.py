'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''


def somar_numeros(n1, n2, n3):
    soma = n1 + n2 + n3
    print(f'A soma dos números é: {soma}')

 
n1 = int(input('Digite um número: ')) 
n2 = int(input('Digite outro número: ')) 
n3 = int(input('Digite mais um número: '))   
somar_numeros(n1, n2, n3)


    