"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""

class Tamagushi:
    
    def __init__(self, nome, fome = 100, saude = 100, idade = 1):
        self.__nome = nome
        
        self.__fome = fome
        if self.__fome > 100:
            self.__fome = 100
        elif self.__fome < 1:
            self.__fome = 1
            
        self.__saude = saude
        if self.__saude > 100:
            self.__saude = 100
        elif self.__saude < 1:
            self.__saude = 1
            
        self.__idade = idade
        if self.__idade < 1:
            self.__idade = 1
        
    @property
    def nome(self):
        return self.__nome

    @property
    def fome(self):
        return self.__fome
    
    @property
    def saude(self):
        return self.__saude
    
    @property
    def idade(self):
        return self.__idade

    def humor(self):
        media = (self.__fome + self.__saude) / 2
        return media