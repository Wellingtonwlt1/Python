# Solicita ao usuário a velocidade atual do carro
velocidade = float(input('Qual é a velocidade atual do carro? '))

# Estrutura condicional para verificar se a velocidade ultrapassa 80 km/h
if velocidade > 80:
    # Caso seja maior que 80, exibe mensagem de multa
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')

    # Calcula o valor da multa
    # Para cada km/h acima de 80, o valor é R$7,00
    multa = (velocidade - 80) * 7

    # Exibe o valor da multa formatado com duas casas decimais
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

# Mensagem final, exibida sempre, independente da condição
print('Tenha um bom dia! Dirija com Segurança!')
