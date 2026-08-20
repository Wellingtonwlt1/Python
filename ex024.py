# Solicita ao usuário que digite o nome da cidade onde nasceu
# str() garante que seja tratado como string
# strip() remove espaços extras no início e no fim
cid = str(input('Em que cidade você nasceu? ')).strip()

# Verifica se os 5 primeiros caracteres da cidade são "SANTO"
# cid[:5] pega os primeiros 5 caracteres da string
# upper() transforma em maiúsculas para evitar diferença entre maiúsculas/minúsculas
# == 'SANTO' compara se o resultado é exatamente "SANTO"
print(cid[:5].upper() == 'SANTO')
