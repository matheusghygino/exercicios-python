"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

cidadeA = 80000
cidadeB = 200000
ano = 0

while cidadeA <= cidadeB:
    cidadeA = cidadeA + cidadeA * 0.003
    cidadeB = cidadeB + cidadeB * 0.0015
    ano += 1

print(f"Demorou {ano} anos para a cidade A alcançar a população da cidade B e agora elas possuem {cidadeA:.2f} e {cidadeB:.2f} habitantes respectitivamente")