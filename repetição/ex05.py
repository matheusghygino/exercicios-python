"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""


print("Vamos calcular o crescimento de duas cidades, para isso informe a população e a taxa anual de crescimento de cada uma quando for pedido!")

cidadeA = int(input("Informe o número de habitantes da cidade A: "))
tacA = float(input("Agora informe a taxa anual de crescimento da cidade A em porcento: "))
cidadeB = int(input("Informe o número de habitantes da cidade B: "))
tacB = float(input("Agora informe a taxa anual de crescimento da cidade B em porcento: "))

ano = 0
menor = 0
maior = 0

if cidadeA < cidadeB:
    menor = cidadeA
    maior = cidadeB
elif cidadeB < cidadeA:
    menor = cidadeB
    maior = cidadeA
    
while menor <= maior:
    
    ano += 1

print(f"Demorou {ano} anos para a cidade {menor} alcançar a população da cidade {maior} e agora elas possuem {cidadeA:.2f} e {cidadeB:.2f} habitantes respectitivamente")