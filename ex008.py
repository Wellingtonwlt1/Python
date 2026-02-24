#medida = float(input('Uma distância em metros: '))  # (Comentado) Lê uma distância em metros e guarda em 'medida'
#cm = medida * 100                                   # (Comentado) Converte metros em centímetros
#mm = medida * 1000                                  # (Comentado) Converte metros em milímetros
#km = medida / 1000                                  # (Comentado) Converte metros em quilômetros
#hm = medida / 100                                   # (Comentado) Converte metros em hectômetros
#dam = medida / 10                                   # (Comentado) Converte metros em decâmetros
#dm = medida * 10                                    # (Comentado) Converte metros em decímetros
#print('A medida de {}m, corresponde a \n{:.0f}cm, \n{:.0f}mm, \n{}km, \n{}hm, \n{}dam, \n{:.0f}dm,' .format(medida, cm, mm, km, hm, dam, dm))
# (Comentado) Exibe os resultados formatados em várias linhas

medida = float(input('Uma distância em metros: '))   # Lê uma distância em metros e guarda em 'medida'

cm = medida * 100                                    # Converte metros em centímetros
mm = medida * 1000                                   # Converte metros em milímetros
km = medida / 1000                                   # Converte metros em quilômetros
hm = medida / 100                                    # Converte metros em hectômetros
dam = medida / 10                                    # Converte metros em decâmetros
dn = medida * 10                                     # Converte metros em decímetros (aqui chamado 'dn')

print(f'A medida de {medida}m corresponde a')        # Exibe a frase inicial
print(f'{km}km')                                     # Exibe o valor em quilômetros
print(f'{hm}hm')                                     # Exibe o valor em hectômetros
print(f'{dam}dam')                                   # Exibe o valor em decâmetros
print(f'{dn:.0f}dn')                                 # Exibe o valor em decímetros, sem casas decimais
print(f'{cm:.0f}cm')                                 # Exibe o valor em centímetros, sem casas decimais
print(f'{mm:.0f}mm')                                 # Exibe o valor em milímetros, sem casas decimais

#print(f'A medida de {medida}m corresponde a\n{km}km\n{hm}hm\n{dam}dam\n{dn:.0f}dn\n{cm:.0f}cm\n{mm:.0f}mm')
# (Comentado) Versão alternativa compacta usando apenas um print com quebras de linha (\n)