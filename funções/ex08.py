'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''

def contar_digitos(num):
    print(f'O número possui {len(str(num))} dígitos')

contar_digitos(int(input("Digite um número: ")))