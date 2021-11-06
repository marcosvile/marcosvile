# Exercicio aula 3
# faça um programa que solicite a idade e decida se ela esta apta a entrar no exercito
# requisitos: maior de 18 anos, peso maior ou igual 60kg, altura maior ou igual 1.70m

idade = int(input ("Insira a sua idade: "))

peso = float(input("Insira o seu peso: "))

altura = float(input("Insira a sua altura: "))

if idade <= 18 and peso <= 60 and altura <= 1.70:

    print ("Você não está apto para alistamento militar")

else: 

    print ("você esta apto para alistamento militar")

