class Carro:

    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

    def __str__(self):
        return self.nome

    def listar_carros():
        for i in Carro.carros:
            print (f"{i.nome} | {i.modelo} | {i.ano}")


    