# Solicita ao usuário um número inteiro
num = int(input('Digite o número inteiro: '))

# Exibe o menu de opções de conversão
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

# Recebe a escolha do usuário
opção = int(input('Sua opção '))

# Estrutura condicional para verificar a escolha
if opção == 1:
    # bin() converte para binário, [2:] remove o prefixo '0b'
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    # oct() converte para octal, [2:] remove o prefixo '0o'
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    # hex() converte para hexadecimal, [2:] remove o prefixo '0x'
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    # Caso o usuário digite uma opção inválida
    print('Opção inválida. Tente novamente')
