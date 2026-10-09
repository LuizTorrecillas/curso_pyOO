class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return self._nome
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "Valido" if self._ativo else "Nao valido"

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praca", "Hamburguer")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("Pizzazz", "Italiano")

Restaurante.listar_restaurantes()