# Exercicio 01 - SOLYD

# Faça um formulário que pergunte o nome, CPF, endereço, idade, altura e telefone 
# e imprima isso em um relatório organizado

nome = input('Insira o seu nome: ') #entrada do nome do usuário
CPF = input('Insira o seu CPF, apenas números: ') #entrada dos dados de CPF
endereco = input('Insira o seu endereço: ') #entrada de endereço
CEP = input('Insira o seu CEP, apenas números: ') #insira o seu CEP
idade = input('Insira a sua idade: ') #entrada de idade
altura = input('Insira a sua altura: ') #entrada de altura
telefone = input('Insira o seu telefone: ') #entrada de telefone

print('Colaborador: ', nome,'\nidade: ',idade,'\ntelefone: ',telefone,'\nCPF: ', CPF,'\nLogradouro: ', endereco,'\nCEP: ', CEP,'\naltura: ', altura)
