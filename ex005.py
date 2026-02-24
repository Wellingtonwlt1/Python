n = int(input('Digite um Numero: '))
# Solicita ao usuário que digite um número.
# O valor digitado é convertido para inteiro e armazenado na variável n.

a = n - 1
# Calcula o antecessor do número (um valor a menos que n) e guarda em 'a'.

s = n + 1
# Calcula o sucessor do número (um valor a mais que n) e guarda em 's'.

print('Analisando o valor {}, seu antecessor é {} o sucessor é {}'.format(n, a, s))
# Exibe uma mensagem formatada mostrando:
# - O número digitado (n)
# - Seu antecessor (a)
# - Seu sucessor (s)