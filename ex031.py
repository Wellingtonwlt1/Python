# Solicita ao usuário a distância da viagem em quilômetros
distância = float(input('Qual é a distância da viagem: '))

# Exibe mensagem informando a distância digitada
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))

# Exemplo de estrutura condicional tradicional (comentada)
'''
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
'''

# Usa uma forma simplificada (operador ternário) para calcular o preço
# Se a distância for menor ou igual a 200 km, o preço é 0.50 por km
# Caso contrário, o preço é 0.45 por km
preço = distância * 0.50 if distância <= 200 else distância * 0.45

# Exibe o preço da passagem formatado com duas casas decimais
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
