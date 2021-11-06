## AULA 03 SOLYD

var_verdadeiro = True #variavel tipo boleano, verdadeiro ou falso
var_falso = False

print(type(var_falso))
print(type(var_verdadeiro))

print(var_verdadeiro)
print(var_falso)

if var_verdadeiro == True:
    print("var verdade é verdadeiro")
    print(var_verdadeiro, "é", var_verdadeiro)

print("#############################################")

if var_verdadeiro == True:
    print("var verdade é verdadeiro")

print('#########################################')

print("opções:\n1= marcos\n2= antonio\n3= vilela")

opcao = input("escolha uma opcao: ")

if opcao == '1':
    print('marcos')
elif opcao == '2':
    print('antonio')
elif opcao == '3':
    print('vilela')
else:
    print('opção invalida')



