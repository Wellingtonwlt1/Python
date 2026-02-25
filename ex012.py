preço = float(input('Qual é o preço do produto? R$'))   # Pede ao usuário o preço do produto e converte para número decimal
novo = preço - (preço * 5 / 100)  # Calcula o novo preço aplicando um desconto de 5%
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
# Exibe o preço original e o preço com desconto, ambos formatados com 2 casas decimais