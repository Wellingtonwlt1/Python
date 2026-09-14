# Solicita ao usuário dois números inteiros
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

# Estrutura condicional para comparar os valores
if n1 > n2:
    print('O primeiro valor é maior ')
elif n1 < n2:
    print('O segundo valor é maior ')
else:
    print('Os dois valores são IGUAIS')
