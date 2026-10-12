from modelos.restaurante import Restaurante


restaurante1 = Restaurante("Praca", "gourmet")
restaurante2 = Restaurante("Japinha", "japonesa")
restaurante3 = Restaurante("Indian express", "indiana")

restaurante1.receber_avaliacao("luiz", 10)
restaurante1.receber_avaliacao("Joao", 3)

restaurante2.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()