from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca.title()
        self._modelo = modelo
        self._ativo = False

    def __str__(self):
        return f"{self._marca} | {self._modelo} | {self.ativo}"

    @property
    def ativo(self):
        return "ligado" if self._ativo else "desligado"

    @abstractmethod
    def ligar(self):
        pass