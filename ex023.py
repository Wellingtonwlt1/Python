# Solicita ao usuário que digite um número inteiro
num = int(input('Informe um nímero: '))

# Calcula o dígito da unidade
# Divide por 1 (não altera nada) e pega o resto da divisão por 10
u = num // 1 % 10

# Calcula o dígito da dezena
# Divide o número por 10 (remove a unidade) e pega o resto da divisão por 10
d = num // 10 % 10

# Calcula o dígito da centena
# Divide o número por 100 (remove unidade e dezena) e pega o resto da divisão por 10
c = num // 100 % 10

# Calcula o dígito do milhar
# Divide o número por 1000 (remove unidade, dezena e centena) e pega o resto da divisão por 10
m = num // 1000 % 10

# Exibe mensagem inicial mostrando o número digitado
print('Analisando o número {}'.format(num))

# Mostra o valor da unidade
print('Unidade: {}'.format(u))

# Mostra o valor da dezena
print('Dezena: {}'.format(d))

# Mostra o valor da centena
print('Centena: {}'.format(c))

# Mostra o valor do milhar
print('Milhar: {}'.format(m))
