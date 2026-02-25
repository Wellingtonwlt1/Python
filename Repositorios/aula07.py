n1 = int(input('Um valor: '))  # Lê um valor digitado pelo usuário, converte para inteiro e armazena em n1
n2 = int(input('Outro valor: '))  # Lê outro valor digitado pelo usuário, converte para inteiro e armazena em n2

s = n1 + n2  # Calcula a soma dos dois valores
m = n1 * n2  # Calcula o produto (multiplicação) dos dois valores
d = n1 / n2  # Calcula a divisão real (resultado com casas decimais)
di = n1 // n2  # Calcula a divisão inteira (descarta as casas decimais)
e = n1 ** n2  # Calcula a potência (n1 elevado a n2)

# Exibe os resultados formatados:
# - A soma, o produto e a divisão real com 3 casas decimais
# - O parâmetro end=' ' evita a quebra de linha, permitindo continuar na mesma linha
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')

# Exibe a divisão inteira e a potência na mesma linha
print('Divisão inteira {} e potência {}'.format(di, e))