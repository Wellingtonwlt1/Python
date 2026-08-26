# Solicita ao usuário que digite um número inteiro
número = int(input('Me diga um número qualquer: '))

# Calcula o resto da divisão do número por 2
# Se o resto for 0, o número é par; se for 1, é ímpar
resultado = número % 2

# Linha comentada que mostraria o valor do resto diretamente
# print('O resultado foi {}'.format(resultado))

# Estrutura condicional para verificar se o número é par ou ímpar
if resultado == 0:
    # Caso o resto seja 0, o número é par
    print('O resultado é PAR!'.format(resultado))
else:
    # Caso contrário, o número é ímpar
    print('O Resultado é ÍMPAR!'.format(resultado))
