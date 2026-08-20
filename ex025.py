# Solicita ao usuário que digite seu nome completo
# str() garante que seja tratado como string
# strip() remove espaços extras no início e no fim
nome = str(input('Qual é seu nome completo: ')).strip()

# Verifica se o nome contém a palavra "Silva"
# nome.lower() transforma todo o texto em minúsculas
# 'Silva' in nome.lower() retorna True se "silva" estiver presente, False caso contrário
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))
