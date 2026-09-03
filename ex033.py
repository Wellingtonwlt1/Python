# Solicita ao usuário três valores inteiros
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Assume inicialmente que o menor valor é 'a'
menor = a

# Verifica se 'b' é menor que os outros dois
if b < a and b < c:
    menor = b

# Verifica se 'c' é menor que os outros dois
if c < a and c < b:
    menor = c

# Agora verifica quem é o maior
# Assume inicialmente que o maior valor é 'a'
maior = a

# Verifica se 'b' é maior que os outros dois
if b > a and b > c:
    maior = b

# Verifica se 'c' é maior que os outros dois
if c > a and c > b:
    maior = c

# Exibe o menor valor encontrado
print('O menor valor digitado foi {}'.format(menor))

# Exibe o maior valor encontrado
print('O maior valor digitado foi {}'.format(maior))
