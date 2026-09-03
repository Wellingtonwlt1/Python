# Imprime uma linha decorativa para separar visualmente
print('-='*40)

# Mensagem inicial do programa
print('ANALISADOR DE TRIÂNGULOS')

# Outra linha decorativa
print('-='*40)

# Solicita ao usuário três valores (segmentos de reta)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se os três segmentos podem formar um triângulo
# Regra: cada lado deve ser menor que a soma dos outros dois
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
