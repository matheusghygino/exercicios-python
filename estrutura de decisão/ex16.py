"""Faça um programa que calcule as raízes de uma equação do  segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazr as consistências, informanoao usuário nas seguints situações:
    a - se o usuário informar o valor de A igual a zero, a quação não é do segundo grau e o programa não deve pedir os dmais valores, sendo encerrado
    b - se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa
    c - Se o delta calculado for igual a zero a equação possui apenas uma raiz  real; informe-a ao usuário
    d - Se o delta for positivo, a equação possui duas raizes eais; informe-as  ao usuário"""
    
print("Bem vindo! Vamos calcular uma equação de segundo grau, para isso informe os valores solicitados abaixo!")    
a = float(input("Informe o valor de a: "))

if a == 0:
     print("A equação não é de seguno grau e não pode ser concluída! ")
else:
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))
    
    delta = (b ** 2) - (4*a*c)

    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        print(delta)
        x = (-b + delta ** (1/2)) / ( 2 * a)
        print(f"A quação possui uma raiz: {x:.2f}")
    elif delta > 0:
        x = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2) / (2 * a))
        print(f"A equação possui duas raizes: {x:.2f} e {x2:.2f}")