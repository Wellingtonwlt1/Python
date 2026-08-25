# Solicita ao usuário que digite seu nome completo
# str() garante que seja tratado como string
# strip() remove espaços extras no início e no fim
n = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em partes (lista), separando por espaços
# Exemplo: "Maria Silva Santos" vira ['Maria', 'Silva', 'Santos']
nome = n.split()

# Mensagem inicial
print('Muito prazer em te conhecer!')

# Mostra o primeiro nome
# nome[0] pega o primeiro elemento da lista
print('seu primeiro nome é {}'.format(nome[0]))

# Mostra o último nome
# nome[len(nome)-1] pega o último elemento da lista
# len(nome) retorna o tamanho da lista, subtraindo 1 acessamos o último índice
print('Seu último nome é {}'.format(nome[len(nome)-1]))
