def ganador(joker, boleto):
    # no sé por qué al revés también cuenta como ganador pero es el ejemplo
    return "GANA" if joker == boleto or joker == boleto[::-1] else "PIERDE"

    