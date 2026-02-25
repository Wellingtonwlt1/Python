dias = int(input('Quantos dias alugados? '))        # Pede ao usuário quantos dias o carro ficou alugado e converte para inteiro
KM = int(input('Quantos KM rodados? '))             # Pede ao usuário quantos quilômetros foram percorridos e converte para inteiro
pago = (dias * 60) + (KM * 0.15)                    # Calcula o valor total: R$60 por dia + R$0,15 por quilômetro rodado
print('O total a pagar R${:.2f}'.format(pago))      # Exibe o valor final a pagar, formatado com 2 casas decimais