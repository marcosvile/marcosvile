# Exercicio 07
# escreva uma funcao que recebe um objeto de coleção
# e retorne o valo do maior numero dentro dessa coleção
# faca outra funcao que retorne o menor numero

from typing import Collection


def maior(colecao):
    maioritem = colecao[0]
    for item in colecao:
        if item > maioritem:
            maioritem = item
    return maioritem

print (maior([1, 2, 3, 4, 5, 6, 399]))

def menor(colecao):
    menoritem = colecao[0]
    for item in colecao:
        if item < menoritem:
            menoritem = item
    return menoritem

print (menor([34, 12, 2, 12, 8, 1, -969]))

