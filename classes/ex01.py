"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""

class Bola:
    
    def __init__ (self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material
    
     
    def trocaCor(self, cor_nova):
        self.__cor = cor_nova
    
    @property
    def mostraCor(self):
        return print(self.__cor)
    

bola = Bola("amarela", 50, "couro")

bola.mostraCor
bola.trocaCor("verde")
bola.mostraCor