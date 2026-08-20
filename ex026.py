# Solicita ao usuário que digite uma frase
# str() garante que seja string
# upper() transforma tudo em maiúsculas (facilita a busca pela letra A)
# strip() remove espaços extras no início e no fim
frase = str(input('Digite uma frase: ')).upper().strip()

# Conta quantas vezes a letra 'A' aparece na frase
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

# Mostra a posição da primeira ocorrência da letra 'A'
# find('A') retorna o índice da primeira vez que 'A' aparece
# +1 é usado porque os índices começam em 0, mas queremos mostrar a posição de forma humana (1ª, 2ª, etc.)
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

# Mostra a posição da última ocorrência da letra 'A'
# rfind('A') retorna o índice da última vez que 'A' aparece
# +1 novamente para ajustar a contagem
print('A ultima letra A aparece ma posição {}'.format(frase.rfind('A')+1))
