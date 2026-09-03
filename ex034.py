# Solicita ao usuário o salário atual do funcionário
salário = float(input('Qual é o salário do funcionário? R$'))

# Estrutura condicional para calcular o aumento
# Se o salário for menor ou igual a R$1250, o aumento é de 15%
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    # Caso contrário, o aumento é de 10%
    novo = salário + (salário * 10 / 100)

# Exibe o salário antigo e o novo salário após o aumento
# {:.2f} formata o valor com duas casas decimais
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
