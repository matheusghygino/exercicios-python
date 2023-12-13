"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""

class Conta:
    
    def __init__ (self, numero, nome, saldo = 0):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo
        
    @property
    def numero(self):
        return self._numero

    @property
    def nome(self):
        return self._nome
    
    @property
    def saldo(self):
        return self._saldo
    
    def alterarNome(self, nome):
        self._nome = nome
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")

class ContaDeInvestimento(Conta):
    
    def __init__(self, numero, nome, saldo = 0, juros = 0):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo
        self._juros = juros
    
    def adicionar_juros(self):
        self._saldo += self._saldo * (self._juros / 100)

contaInvestimento = ContaDeInvestimento(123, "Matheus", 1000, 10)
contaInvestimento.adicionar_juros()
contaInvestimento.adicionar_juros()
contaInvestimento.adicionar_juros()
contaInvestimento.adicionar_juros()
contaInvestimento.adicionar_juros()
print(contaInvestimento._saldo)