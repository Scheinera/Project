from binance.client import Client
# from secrets import api_secret, api_key
api_secret = "6r6OtaF1AbvNsKfxrElFvYjzHjDTWzcZGouWrQWDHqH0aPPkE8OqCjjD2DDital9"
api_key = "YvH7L3VgJJRw42XPyHZhlxkiK30kgvMbvOYN9hdKasKiUYSw0ZVhKfV1qi0ckIsX"


client = Client(api_key, api_secret)

# pegar informações da nossa conta
info = client.get_account()
for item in info:
    print(item)

# ver os saldos dos ativos que temos na conta
lista_ativos = info["balances"]
# print(lista_ativos)
# ativos que temos algum saldo
for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem dentro da binance
from binance.enums import *
order = client.create_order(
    symbol='XRPUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.01,
    )
print(order)

# visualizar as ordens executadas
print(client.get_all_orders(symbol='XRPUSDT'))
print(client.get_my_trades(symbol='XRPUSDT'))

# te mostrar as referências de cada par de moedas
print(client.get_symbol_info('XRPUSDT'))

# pegar as cotações em tempo real
transacoes = client.get_recent_trades(symbol="XRPUSDT", limit=1)
print(transacoes)