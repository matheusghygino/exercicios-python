"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."""

def fatorial(valor_fatorial):
    n = valor_fatorial
    while n >= 16:  
        n = int(input("Valor inválido! Digite um número inteiro menor do que 16: "))
    while  n < 0:
        n = int(input(("O fatorial do número não existe! Digite um número positivo: ")))
        while n > 16:
            n = int(input("Valor inválido! Digite um número inteiro menor do que 16: "))    
    if n == 0:
        print("O fatorial de 0 é igual a 1!")
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial = fatorial * i  
            print(fatorial) 
    return(fatorial)

numero = int(input("Digite um número inteiro e menor que 16 para que seja calculado sua fatorial: "))
fatorial(numero)
outro = input("Você quer calcular outro número? (S) para sim (N) para não: ").upper().strip()
while outro == "S":
    numero = int(input("Digite um número inteiro e menor que 16 para que seja calculado sua fatorial: "))
    fatorial(numero)
    outro = input("Você quer calcular outro número? (S) para sim (N) para não: ").upper().strip()
print("Programa finalizado!")