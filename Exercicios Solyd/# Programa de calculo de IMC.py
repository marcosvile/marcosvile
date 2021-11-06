

# Programa de calculo de IMC

# O cálculo de IMC serve para obter o indice de massa corporal, utlizando do calculo
# IMC=peso/(alturaXaltura)

peso=float(input('Qual o seu peso em kg: ')) #entrada do peso, variavel do tipo float
altura=float(input('Qual a sua altura em metros: ')) #entrada da altura, variavel do tipo float

IMC=(float(peso)/(float(altura)*(float(altura)))) #para o calculo funcionar, necessario indicar o tipo da variavel como float 
                                                  #para o calculo funcionar, para o calculo funcionar, as informações float devem
                                                  #utilizar 'ponto' nao 'virgula'

#16 a 16,9 kg/m² - Muito abaixo do peso
#17 a 18,4 kg/m² - Abaixo do peso 
#18,5 a 24,9 kg/m² - Peso normal 
#25 a 29,9 kg/m² - Acima do peso 
#30 a 34,9 kg/m² - Obesidade grau I 
#35 a 40 kg/m² - Obesidade grau II 
#maior que 40 kg/m² - Obesidade grau III#


print("seu IMC, Índice de Massa Corporal é:", IMC)

if IMC < 16.9:
    print("você está muito abaixo do peso")

elif IMC < 18.4:
    print("Você está abaixo do peso")

elif IMC < 24.9:
    print("Você está no peso normal")

elif IMC < 29.9:
    print("Você está acima do peso")

elif IMC < 34.9:
    print("Você está com obesidade grau I")

elif IMC < 40:
    print("Você está com obesidade grau II")

elif IMC > 40.1:
    print("Você está com oberisade grau III")

