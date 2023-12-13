"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto = int(input("Quanto de imposto em porcentual tem sobre o produto? ")), custo = int(input('Qual o custo do item sem imposto: '))):
    valorImposto = custo * (taxaImposto/100)
    novoPreco = custo + valorImposto
    print(f"O valor do produto com imposto é: {novoPreco}")

somaImposto()