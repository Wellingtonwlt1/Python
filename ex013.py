salário = float(input('Qual é o salário do Funcionário? R$'))   # Pede ao usuário o salário atual e converte para número decimal
novo = salário + (salário * 15 / 100)  # Calcula o novo salário aplicando um aumento de 15%
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
# Exibe o salário antigo e o novo salário com aumento, ambos formatados com 2 casas decimais