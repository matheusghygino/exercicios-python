class BombaCombustivel:
    
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel
        
    def alterarCombustivel(self, combustivel):
        while combustivel != "GASOLINA" and combustivel != "GASOLINA ADITIVADA" and combustivel != "ALCOOL" and combustivel != "ETANOL: ":
            combustivel = input("Combustível inválido! Digite algum dos combustíveis a seguir: [Gasolina], [Gasolina Aditivada], [Alcool] ou [Etanol]\n").upper()
        self.__tipoCombustivel = combustivel
        return print("Agora o combustível na bomba é: {}".format(combustivel))


bombaCombustivel = BombaCombustivel("Gasolina", 5.0, 500.0 )

bombaCombustivel.alterarCombustivel("banana")
