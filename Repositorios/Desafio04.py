# DESAFIO 004
# Programa que lê algo pelo teclado e mostra seu tipo primitivo
# e todas as informações possíveis sobre ele.

entrada = input("Digite algo: ")

print("\n--- Análise da entrada ---")
print(f"Tipo primitivo: {type(entrada)}")
print(f"É numérico? {entrada.isnumeric()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"É alfanumérico? {entrada.isalnum()}")
print(f"Está em maiúsculas? {entrada.isupper()}")
print(f"Está em minúsculas? {entrada.islower()}")
print(f"Está capitalizado? {entrada.istitle()}")
print(f"Só tem espaços? {entrada.isspace()}")