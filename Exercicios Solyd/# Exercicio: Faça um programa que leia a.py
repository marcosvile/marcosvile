# Exercicio: Faça um programa que leia a quantidade de pessoas que serão convidadas
# para uma festa, após isso, o programa irá perguntar o nome de todas as pessoas
# e colocar numa lista de convidados e após isso irá imprimir todos os nomes da lista

print ("---------------------------------- ")
print ("sistema de controle de convidados: ")
print ("---------------------------------- ")

convidados = input("Insira o numero de convidados: ")
lista = []


i=1

while i <= int(convidados):
    convidado = input ("Insira o nome do convidado " + str(i) +": " )

    lista.append(convidado)

    i += 1

print("\nforam convidados", convidados, "pessoas. \n ")


for convidado in lista:
    print(convidado,)
