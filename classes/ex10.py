"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""

class BombaCombustivel:
    
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel
        
    
    property
    def tipoCombustivel(self):
        return self.__tipoCombustivel
    
    property
    def valorLitro(self):
        return self.__valorLitro
    
    property
    def quantidadeCombustivel(self):
        return self.__quantidadeCombustivel
        
    def abastecerPorValor(self, valor):
        while valor <= 0:
            valor = int(input("Não é possível abastecer com 0 ou um valor negativo, por favor informe um valor válido! \n"))
        litros = valor / self.__valorLitro
        if litros < self.__quantidadeCombustivel:
            self.__quantidadeCombustivel -= litros
        return print("Foram adicionados {} litros de combustível no seu veículo".format(litros, self.__quantidadeCombustivel))
    
    def abastecerPorLitro(self, litros):
        while litros <= 0:
            litros = int(input("Não é possível abastecer com 0 ou um valor negativo, por favor informe um valor válido! \n"))             
        if self.__quantidadeCombustivel > litros:
            valor_a_pagar = litros * self.__valorLitro
            self.__quantidadeCombustivel -= litros
            return print("O valor a pagar é R${}".format(valor_a_pagar))
        else:
            return print("A bomba não tem combustível suficiente para abastecer essa quantidade. Temos somente {}".format(self.__quantidadeCombustivel))
    
    def alterarValor(self, valor):
        while valor <= 0:
            valor = int(input("O valor do combustível precisa ser maior do que 0! Digite um valor válido: "))
        self.__valorLitro = valor
        return print("O novo valor do combustível é: R${} por litro".format(valor))
        
    def alterarCombustivel(self, combustivel):
        while combustivel != "GASOLINA" and combustivel != "GASOLINA ADITIVADA" and combustivel != "ALCOOL" and combustivel != "ETANOL: ":
            combustivel = input("Combustível inválido! Digite algum dos combustíveis a seguir: [Gasolina], [Gasolina Aditivada], [Alcool] ou [Etanol]\n").upper()
        self.__tipoCombustivel = combustivel
        return print("Agora o combustível na bomba é: {}".format(combustivel))
    
    def alterarQuantidadeCombustivel(self, quantidade):
        print("Informe quantos litros de combustível irá colocar ou retirar da bomba: ")
        self.__quantidadeCombustivel += quantidade
        if quantidade < 0:
            quantidade = 0
        return print("A bomba agora tem {} litros de combustível!".format(quantidade))
    