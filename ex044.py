# Exibe o nome da loja centralizado em 40 caracteres,
# preenchendo os espaços vazios com o sinal "="
print('{:=^40}'.format(' LOJAS WLT '))

# Solicita o valor total das compras
preço = float(input('Preço das compras: R$ '))

# Exibe o menu de formas de pagamento
print('''FORMAS DE PAGAMENTO
[ 1 ] à Vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3x ou mais no cartão''')

# Solicita ao usuário a opção de pagamento
opção = int(input('Qual é a opção? '))

# Pagamento à vista em dinheiro ou cheque
# Recebe 10% de desconto
if opção == 1:
    total = preço - (preço * 10 / 100)

# Pagamento à vista no cartão
# Recebe 5% de desconto
elif opção == 2:
    total = preço - (preço * 5 / 100)

# Pagamento em 2 vezes no cartão
# Não há desconto nem juros
elif opção == 3:
    total = preço
    parcela = total / 2

    # Mostra o valor de cada parcela
    print('Sua compra será parcelada em 2X de R${:.2f} SEM JUROS'.format(parcela))

# Pagamento em 3 vezes ou mais no cartão
# Acréscimo de 20% sobre o valor da compra
elif opção == 4:
    total = preço + (preço * 20 / 100)

    # Pergunta em quantas parcelas será dividido
    totparc = int(input('Quantas parcelas? '))

    # Calcula o valor de cada parcela
    parcela = total / totparc

    # Exibe informações do parcelamento
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totparc, parcela))

# Caso o usuário digite uma opção inválida
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

# Exibe o valor original da compra e o valor final após descontos ou juros
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))