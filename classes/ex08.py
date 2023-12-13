"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?"""

class Macaco:
    
    def __init__(self, nome, bucho = ""):
        self.__nome = nome
        self.__bucho = bucho
    
    @property
    def bucho(self):
        return self.__bucho
    
    def comer(self, alimento):
        self.__bucho += alimento + ""
    
    def digerir(self):
        self.__bucho = ""