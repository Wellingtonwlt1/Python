#from math import sqrt                        # Importa apenas a função sqrt (raiz quadrada) da biblioteca math
#num = int(input('Digite um numero: '))       # Pede ao usuário um número inteiro
#raiz = math.sqrt(num)                        # Calcula a raiz quadrada usando math.sqrt
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))   # Exibe o resultado com 2 casas decimais

from math import sqrt                         # Importa diretamente a função sqrt da biblioteca math
num = int(input('Digite um numero: '))        # Pede ao usuário um número inteiro
raiz = sqrt(num)                              # Calcula a raiz quadrada do número informado
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))    # Exibe o número e sua raiz quadrada com 2 casas decimais