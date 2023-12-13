'''Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)'''

class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        self._salario = valor
    
    def aumentarSalario(self, valor):
        valorPorcentual = self._salario * (valor / 100)
        self._salario += valorPorcentual
    
matheus = Funcionario('Matheus', 1000)
matheus.aumentarSalario(10)
print(matheus.salario)