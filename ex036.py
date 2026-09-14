# Solicita os dados ao usuário
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

# Calcula o valor da prestação mensal
prestação = casa / (anos * 12)

# Calcula o valor máximo permitido da prestação (30% do salário)
mínimo = salário * 30 / 100

# Exibe informações sobre o financiamento
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

# Verifica se o financiamento pode ser concedido
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
