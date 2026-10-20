# Solicita ao usuário três valores (segmentos de reta)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se os três segmentos podem formar um triângulo
# Regra: cada lado deve ser menor que a soma dos outros dois
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ', end='')

    # Verifica o tipo de triângulo
    if r1 == r2 == r3:
        # Todos os lados iguais
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        # Todos os lados diferentes
        print('ESCALENO')
    else:
        # Dois lados iguais
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
