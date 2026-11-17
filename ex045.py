# Importa a função randint para gerar números aleatórios
from random import randint

# Importa a função sleep para criar pausas no programa
from time import sleep

# Tupla com as opções do jogo
itens = ('Pedra', 'Papel', 'Tesoura')

# O computador escolhe aleatoriamente um número entre 0 e 2
computador = randint(0, 2)

# Exibe as opções para o jogador
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# Recebe a jogada do jogador
jogador = int(input('Qual é a sua jogada? '))

# Efeito visual do "JO-KEN-PO"
print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO!!!')

# Linha decorativa
print('-=' * 12)

# Verifica se a jogada do jogador é válida
if jogador not in [0, 1, 2]:
    print('JOGADA INVÁLIDA!')
else:
    # Mostra a escolha do computador
    print('Computador jogou {}'.format(itens[computador]))

    # Mostra a escolha do jogador
    print('Jogador jogou {}'.format(itens[jogador]))

    # Linha decorativa
    print('-=' * 12)

    # Computador escolheu Pedra
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')

    # Computador escolheu Papel
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')

    # Computador escolheu Tesoura
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')