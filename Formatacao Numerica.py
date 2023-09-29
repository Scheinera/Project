# Separador de decimal

faturamento =  1500
custo =  500
lucro = faturamento - custo
print(f'O lucro foi de R${lucro:,.2f}')


margem = lucro / faturamento
print(f'A margem foi de {margem:.2%}')

# Formato Brasileiro

texto_lucro = f'R${lucro:_.2f}'
texto_lucro = texto_lucro.replace(".",","). replace("_",".")
print(f'O lucro foi de {texto_lucro}')

