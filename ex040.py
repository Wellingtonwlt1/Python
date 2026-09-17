# Solicita as duas notas do aluno
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

# Calcula a média
média = (nota1 + nota2) / 2

# Exibe as notas e a média formatadas
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))

# Estrutura condicional para verificar a situação do aluno
if 7 > média >= 5:
    # Média entre 5 e 6.9 → Recuperação
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    # Média abaixo de 5 → Reprovado
    print('O aluno está REPROVADO.')
else:
    # Média igual ou acima de 7 → Aprovado
    print('O aluno está APROVADO.')
