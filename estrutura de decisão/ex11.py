"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento."""
    
salario = float(input("Iremos dar um aumnto para nossos trabalhadores de acordo com quanto vocês recebm! Para isso digite seu salário aqui: "))

aumento = 0.0

if salario <= 280:
    aumento = salario * 0.2
    salario = salario + aumento
elif salario < 700:
    aumento = salario * 0.15
    salario = salario + aumento
elif salario < 1500:
    aumento = salario * 0.1
    salario = salario + aumento


print(f"Seu novo salário é de {salario} e o seu aumento foi de R${aumento}")