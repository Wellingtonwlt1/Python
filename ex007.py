n1 = float(input('Primeira nota do aluno: '))  # Lê a primeira nota digitada pelo usuário, converte para número decimal (float) e guarda em n1
n2 = float(input('Segunda nota do aluno:'))    # Lê a segunda nota digitada pelo usuário, converte para float e guarda em n2

média = (n1 + n2) / 2                          # Calcula a média aritmética das duas notas e guarda em 'média'

print('A media entre {:.1f} e {:.1f} vale {:.1f}'.format(n1, n2, média))
# Exibe uma mensagem formatada mostrando:
# - A primeira nota com 1 casa decimal ({:.1f})
# - A segunda nota com 1 casa decimal ({:.1f})
# - A média calculada também com 1 casa decimal ({:.1f})