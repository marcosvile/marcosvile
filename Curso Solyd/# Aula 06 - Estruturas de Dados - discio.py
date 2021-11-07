# Aula 06 - Estruturas de Dados - discionarios, tuplas, conjuntos

lista=['joao', 'maria'] #lista - possivel manitpular objetos dentro, adicionar, remover, inserir
tupla=("gui", "jose") #tupla - nao é possivel manipular os objetos dentro, mas é possivel alterar o valor
dicionario={'nome': 'guilherme', 'idade': 27 } #discionario - tem uma chave e um valor, separados por dois pontos
conjunto={'mar', 'antonio'} # tem chaves dentro, e nao tem valores, nao pode ter itens repetidos

print(tupla, )
print(type(tupla))

print(tupla[1])

tupla=("fabricio", "kaka")
print(tupla)

if 'joao' in lista:
    print("joao esta na coleção")

print(dicionario)

print(dicionario['nome'])

print(len(dicionario))
print(len(conjunto))

if 'guilherme' in dicionario.values():
    print("guilherme esta aqui")

for valores in dicionario.values():
    print(valores)

for valores in dicionario.keys():
    print(valores)

dicionario['idade']=40

print(dicionario)

dicionario['endereço'] = 'av jonh snow'

print(dicionario)

print(conjunto)

conjunto.add("maria")
conjunto.add("almir")

print(conjunto)


if "almir" in lista:
    print(" foi encontrado no conjunto")
else: print("no estás")



