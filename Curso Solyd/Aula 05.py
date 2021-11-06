## Aula 05 - estruturas de laço - While e for

nomes = ['marcos', 'antonio', 'vilela', 'teixeira']
lista = range(5, 10, 2)

print(nomes)

for nome in nomes:
    print(nome)

for nome in nomes:
    print(nome[0])

for item in lista:
    print (item)

for i in range (4):
    print(nomes[i])

palavra = 'marcos antonio'
    
for i in palavra:
    print(i)

i = 5

while i < 10:
    print('i menor que 10', i)
    i = i +1

print("acabou while", i)

while i < 10:
    print('loop', i)
    i = i + 1

while i > 10:
    print('loop infinito', i)

feira=['maça', 'oleo', 'massa']
print(len(feira))

contador = 0

for item in feira:
    contador += 1

print(contador)

numero = 0

while True:
    print(float(numero))
    if numero == 20:
        break
    numero += 1


numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1


