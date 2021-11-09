# Aula 09 - POO
# Main - onde meu programa principal irá rodar

from typing import ForwardRef
from veiculo import Veiculo
from carro import Carro, Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print(caminhao_rosa)
print(type(caminhao_rosa))

print("cor: ", caminhao_rosa.cor)
print("Marca: ", caminhao_rosa.marca)
print("Tanque: ", caminhao_rosa.tanque)


carro_azul = Veiculo("azul", 5, "BMW", 17)

print("#######################")
print("CARRO AZUL: ")
print("Cor: ", carro_azul.cor )
print("Rodas: ", carro_azul.rodas)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)

carro_azul.abastecer(35)
print("Tanque: ", carro_azul.tanque)

print("#################")

carro = Carro("azul", "VW", 30)


print("Carro: ")
print("CARRO : ")
print("Cor: ", carro.cor)
print("Rodas: ", carro.rodas)
print("Marca: ", carro.marca)
print("Tanque: ", carro.tanque)

carro.abastecer(35)
print("Tanque: ", carro.tanque)

carro.abastecer(35)
print("Tanque: ", carro.tanque)
