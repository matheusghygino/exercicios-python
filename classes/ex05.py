"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios"""

class Conta:
    
    def __init__ (self, numero, nome, saldo = 0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        
    @property
    def numero(self):
        return self.__numero

    @property
    def nome(self):
        return self.__nome
    
    @property
    def saldo(self):
        return self.__saldo
    
    def alterarNome(self, nome):
        self.__nome = nome
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")