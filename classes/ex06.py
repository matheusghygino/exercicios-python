"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Televisor:
    
    def __init__(self, canal = 1, volume = 50):
        self.__canal = canal
        self.__volume = volume
        if self.__volume > 100:
            self.__volume = 100
        if self.__volume < 1:
            self.__volume = 1
        if self.__canal < 1:
            self.__canal = 1
        if self.__canal > 100:
            self.__canal = 100
        
        
    @property
    def canal(self):
        return self.__canal
    
    @property
    def volume(self):
        return self.__volume

    def aumentar_volume(self, valor):
        novo_volume = self.__volume + valor
        if novo_volume < 100:
            self.__volume += novo_volume
        else:
            self.__volume = 100
            
    def diminuir_volume(self, valor):
        novo_volume = self.__volume - valor
        if novo_volume > 1:
            self.__volume -= novo_volume
        else:
            self.__volume = 1
    
    def informar_canal(self, valor):
        if valor >= 1 and valor <= 100:
            self.__canal = valor
        else:
            print("Canal inválido")