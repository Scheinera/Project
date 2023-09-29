from hashlib import sha256
import time


def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
        nonce += 1


if __name__ == "__main__":
    num_bloco = 15
    transacoes = """
    Lira->Alon->10
    Alon->Joao->5
    Joao->Amanda->11"""
    qtde_zeros = 20
    hash_anterior = "00000000000000000004929b1d734940ca8b866d4ae307d54ab65468cc9ee289"
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
    print(resultado)
    print(time.time() - inicio)