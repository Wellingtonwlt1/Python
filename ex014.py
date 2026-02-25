c = float(input('Informe a tempetatura em °C: '))   # Pede ao usuário a temperatura em graus Celsius e converte para número decimal
f = ((9*c)/5)+32   # Converte a temperatura de Celsius para Fahrenheit usando a fórmula (°C × 9/5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))  # Exibe a temperatura original em °C e o resultado convertido em °F