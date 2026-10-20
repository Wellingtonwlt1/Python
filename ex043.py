# Solicita peso e altura do usuário
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

# Calcula o IMC: peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

# Exibe o IMC formatado com uma casa decimal
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

# Estrutura condicional para classificar o IMC
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO normal!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
