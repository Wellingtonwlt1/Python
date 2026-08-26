# Importa a classe date do módulo datetime para trabalhar com datas
from datetime import date

# Solicita ao usuário um ano para analisar
ano = int(input('Que ano quer analisar? '))

# Se o usuário digitar 0, o programa usa o ano atual do sistema
if ano == 0:
    ano = date.today().year

# Estrutura condicional para verificar se o ano é bissexto
# Regras:
# - É bissexto se for divisível por 4
# - Mas não pode ser divisível por 100
# - Exceto se também for divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} Não é BISSEXTO!'.format(ano))
