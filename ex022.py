# Solicita ao usuário que digite seu nome completo
# str() garante que seja tratado como string
# strip() remove espaços extras no início e no fim
nome = str(input('Digite seu nome completo: ')).strip()

# Mensagem inicial
print('Analisando seu nome...')

# Mostra o nome em letras maiúsculas
print('Seu nome em maiísculas é {}'.format(nome.upper()))

# Mostra o nome em letras minúsculas
print("seu nome em minúsculas é {}".format(nome.lower()))

# Conta o número total de letras (descontando os espaços)
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# Este trecho está comentado, mas se ativo mostraria
# o tamanho do primeiro nome usando a posição do primeiro espaço

# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# Divide o nome em partes (lista), separando por espaços
separa = nome.split()

# Mostra o primeiro nome e quantas letras ele tem
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
