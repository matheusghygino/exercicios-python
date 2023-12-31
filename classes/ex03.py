"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local."""

class Retangulo:
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura
    
    @base.setter
    def base(self, base):
        self.__base = base
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    def calcular_area(self):
        area = self.__base * self.altura
        return print(area)

    def calcular_perimetro(self):
        perimetro = (self.__base * 2) + (self.__altura * 2)
        return print(perimetro)

        
    