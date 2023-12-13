"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque."""

class Carro:
    
    def __init__(self, consumo, combustivel = 0):
        self.__consumo = consumo
        self.__combustivel = combustivel
    
    property
    def consumo(self):
        return self.__consumo
    
    property
    def combustivel(self):
        return self.__combustivel
    
    def adicionarGasolina(self, quantidade):
        while quantidade <= 0:
            quantidade = int(input("Por favor adicione 1 ou mais litros!\n"))
        self.__combustivel += quantidade
        
    def andar(self, distancia):
        while distancia <= 0:
            distancia = int(input("Digite uma distância em km maior do que 0"))
        if (distancia / self.__consumo) <= self.__combustivel:
            print("O carro andou {} quilômetros".format(distancia))
        else:
            print("Combustível insuficiente para andar essa distância! Abasteça antes de andar!")
             
    def obterGasolina(self):
        return print(self.__combustivel)