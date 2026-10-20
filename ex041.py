from datetime import date

# Pega o ano atual do sistema
atual = date.today().year

# Solicita o ano de nascimento do atleta
nascimento = int(input('Ano de Nascimento: '))

# Calcula a idade
idade = atual - nascimento

# Exibe a idade
print('O atleta tem {} anos.'.format(idade))

# Estrutura condicional para classificar o atleta
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
