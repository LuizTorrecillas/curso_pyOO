from carro import Carro
from moto import Moto

moto1 = Moto("Cyborgue", "Cavazaki", "Casual")
moto2 = Moto("Android", "Harley", "Casual")
moto3 = Moto("Animal", "Honda", "Esportiva")

carro1 = Carro("Fiat", "Fastback", 4)
carro2 = Carro("Honda", "Fit", 4)
carro3 = Carro("Lamborguini", "Veneno", 2)

print(f"Carro 1: {carro1._marca} {carro1._modelo}, Cor: {carro1._portas}")
print(f"Carro 2: {carro2._marca} {carro2._modelo}, Cor: {carro2._portas}")
print(f"Carro 3: {carro3._marca} {carro3._modelo}, Cor: {carro3._portas}")
