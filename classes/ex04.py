"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class Pessoa:
    
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
    
    @property
    def nome(self):
         return self.__nome
    
    @property
    def idade(self):
         return self.__idade
    
    @property
    def peso(self):
         return self.__peso
    
    @property
    def altura(self):
         return self.__altura
    
    def envelhecer(self, valor):
        contador = 0        
        if self.__idade < 21:
            while self.__idade < 21:
                self.__idade += 1
                self.__altura += 0.5
                contador += 1
            self.__idade  += (valor - contador)  
        else:
            self.__idade += valor
                     
    def engordar(self, valor):
        self.__peso += valor
    
    def emagrecer(self, valor):
        self.__peso -= valor
    
    def crescer(self, valor):
        self.__altura += valor