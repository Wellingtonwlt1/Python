from datetime import date

# Pega o ano atual do sistema
atual = date.today().year

# Solicita o ano de nascimento do usuário
nasc = int(input('Ano de nascimento: '))

# Calcula a idade
idade = atual - nasc

# Exibe informações básicas
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

# Estrutura condicional para verificar situação do alistamento
if idade == 18:
    # Caso tenha exatamente 18 anos
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    # Caso ainda não tenha 18 anos
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    # Caso já tenha passado dos 18 anos
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
