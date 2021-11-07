# AULA 07 SOLYD - métodos e funcoes

def soma (numero1, numero2): # def - para definir uma funcao, e nao para chama-la
    resp = numero1 + numero2
    return resp              # return para chmar a resposta da funcao

retorno = soma(75, 1289)
retorno2 = soma( 2, 2 )
retorno3 = soma ( 75.5, 34.6)
print(retorno, retorno2, retorno3)


def imprimeoi():
    print("oi")

def contador(x):
    if len(x)==7:
        return True

    else:
        return False

print (contador("oi pessoal"))

def temseteletras(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if temseteletras({1,2,3,4,5,7,8}):
    print("realmente tem sete ")




