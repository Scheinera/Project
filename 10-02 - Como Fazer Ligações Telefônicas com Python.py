# Link com as referências de como escrever a mensagem
# https://www.twilio.com/docs/voice/twiml
from twilio.rest import Client

account_sid = "seu account_sid, pegue na sua conta do twilio"
auth_token = "seu token, pegue na sua conta do twilio"
meu_numero = "seu numero pessoal - o numero que você verificou no twilio"
numero_twilio = "seu numero do twilio"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language="pt-BR">
Ei, Lira, ta tudo bem? Parece que você não trabalha mais. Até ligação tá automatizado.
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)


