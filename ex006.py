n = int(input('Digite um valor: '))  # Lê um número digitado pelo usuário, converte para inteiro e armazena em 'n'
d = n * 2                            # Calcula o dobro do número e guarda em 'd'
t = n * 3                            # Calcula o triplo do número e guarda em 't'
r = n ** (1/2)                       # Calcula a raiz quadrada do número usando potência fracionária (n elevado a 1/2)

print('O dobro de {} vale {}'.format(n, d))  # Exibe o número digitado e seu dobro
print('O triplo de {} vale {}'.format(n, t)) # Exibe o número digitado e seu triplo
print('A raiz quadrada de {} vale {:.2f}'.format(n, r))  # Exibe o número digitado e sua raiz quadrada com 2 casas decimais