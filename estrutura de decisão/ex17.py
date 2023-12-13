"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto"""

ano = int(input("Informe um ano e iremos te responder se o mesmo é bissexto: "))

bissexto = False

if bissexto % 4 == 0:
    bissexto = True
    print("O ano é bissexto")
elif bissexto == False:
    print("O ano não é bissexto")