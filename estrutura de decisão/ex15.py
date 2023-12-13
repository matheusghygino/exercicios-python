"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;"""
   
triangulo = False    
    
l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
l2 = float(input("Digite o valor do segundo lado do triângulo: "))
l3 = float(input("Digite o valor do terceiro lado do triângulo: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    triangulo = True
    if triangulo == True:
        print("Os lados informados podem formar um triângulo! ")
        if l1 == l2 and  l1 == l3:
            print("O triângulo é um triângulo Equilátero!")    
        elif l1  == l1 or l1 == l3 and l2 == l3 or l2 == l1:
            print("O triângulo é um triângulo Isósceles!")
        else:
            print("O triângulo é um triângulo escaleno!")
else:
    print("Os valores digitados não podem formar um triângulo devido suas proporções!")