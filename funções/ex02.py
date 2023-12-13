'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

def imprime_sequencia(n):
    for i in range(n+1):
        
        for j in range(1, i+1):
           print(j, end=' ')
        print('')  

imprime_sequencia(3)


