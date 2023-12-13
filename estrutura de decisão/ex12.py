"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
    Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00    """
    
valor = float(input("Quanto você recebe por hora trabalhada? "))
horas = float(input("Quantas horas você trabalhou esse mês? "))
salarioBruto = valor * horas
ir = 0.0
taxaSindical = salarioBruto * 0.03
fgts = salarioBruto * 0.11


if salarioBruto > 900 and salarioBruto <= 1500:
    ir = salarioBruto * 0.05
elif salarioBruto <= 2500:
    ir = salarioBruto * 0.1
elif salarioBruto > 2500:
    ir = salarioBruto * 0.2
 
descontos = ir + taxaSindical   
salarioLiquido = salarioBruto - ir - taxaSindical

print(f"Foi descontado R${ir} de imposto de renda do seu salário") 
print(f"Foi escontaddo R${taxaSindical} da taxa sindical do seu salário")
print(f"Foi depositao R${fgts} no seu FGTS")
print(f"O total de descontos foi de R$ {descontos}")
print(f"O seu salário líquido é de R${salarioLiquido}")

    
