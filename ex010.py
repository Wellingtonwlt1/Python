real = float(input('Quanto de dinheiro você tem na carteira? R$'))
# Pede ao usuário o valor em reais e converte para número decimal
dolar = real / 5.14 # Converte o valor em reais para dólares usando a taxa de câmbio fixa de 5,14
print('Com R${:.2f} Você pode comprar US${:.2f}'.format(real, dolar))
# Exibe o valor em reais e o equivalente em dólares com 2 casas decimais