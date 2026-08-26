# Importa a função randint para gerar números aleatórios
from random import randint

# Importa a função sleep para pausar a execução por alguns segundos
from time import sleep

# O computador "pensa" em um número aleatório entre 0 e 5
computador = randint(0, 5)

# Linha comentada que mostraria o número escolhido (seria um "spoiler")
# print('Pensei no número {}'.format(computador))

# Imprime uma linha decorativa
print('-=-' * 20)

# Mensagem inicial explicando o jogo
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

# Outra linha decorativa
print('-=-' * 20)

# O jogador tenta adivinhar digitando um número
jogador = int(input('Em que número eu pensei? '))

# Mensagem de processamento
print('PROCESSANDO...')

# Pausa de 3 segundos para dar suspense
sleep(3)

# Estrutura condicional para verificar se o jogador acertou
if jogador == computador:
    # Caso o número seja igual, o jogador vence
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    # Caso contrário, o computador mostra o número correto
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
