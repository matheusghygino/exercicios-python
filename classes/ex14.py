'''Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.'''

class Tamagushi:
    
    def __init__(self, nome, fome = 100, saude = 100, humor = 100, idade = 1):
        self._nome = nome
        
        self._fome = fome
        if self._fome > 100:
            self._fome = 100
        elif self._fome < 1:
            self._fome = 1
            
        self._saude = saude
        if self._saude > 100:
            self._saude = 100
        elif self._saude < 1:
            self.saude = 1
            
        self._idade = idade
        if self._idade < 1:
            self._idade = 1
        
    @property
    def nome(self):
        return self._nome

    @property
    def fome(self):
        return self._fome
    
    @property
    def saude(self):
        return self._saude
    
    @property
    def idade(self):
        return self._idade

    def alimentar(self, qtde_comida):
        self._fome += qtde_comida
        if self._fome > 100:
            self._fome = 100
    
    def brincar(self, tempoBrincando):
        self._humor += tempoBrincando / 3
        if self._humor > 100:
            self._humor = 100
    
    def humor(self):
        self._humor = (self._fome + self._saude) / 2
        