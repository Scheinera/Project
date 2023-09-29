produtos = ["ABC123", "abd012", "ABS111", "AbB222"]

texto = " abd012"

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

texto = tratar_texto(texto)
print(texto)

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)








