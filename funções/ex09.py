'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.'''

def reverso(num):
    print(int(str(num)[::-1]))

reverso(int(input('Digite um número: ')))