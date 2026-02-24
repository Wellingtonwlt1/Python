# DESAFIO 004
# Programa que lê algo pelo teclado e mostra seu tipo primitivo
# e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabeto?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minusculas?', a.islower())
print('Está capitalizada?', a.istitle())