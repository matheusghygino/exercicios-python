"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""

class Quadrado:
    
    def __init__(self, tamanho_do_lado):
        self.__tamanho_do_lado = tamanho_do_lado
        pass
   
    @property
    def tamanho_do_lado(self):
        return self.__tamanho_do_lado
    
    @tamanho_do_lado.setter
    def tamanho_do_lado(self, tamanho_do_lado):
        self.__tamanho_do_lado = tamanho_do_lado
    
    def calcular_area(self):
        area = self.tamanho_do_lado * self.tamanho_do_lado
        return area
        
    


