def media_prometida(n_examenes, notas, nota_prometida):
    # el número de notas es parte del input pero es tontería porque se puede sacar en O(1) por la longitud
    nota_minima = nota_prometida * (n_examenes + 1) - sum(notas)
        # Alomejor no era esto lo que pretendían, pero si consigues la nota o más aunque saques un 0 prefiero devolver un 0 en lugar de imposible
        # Es decir, lo estoy interpretando como nota mínima en lugar de nota exacta
        # La versión exacta sería 
        # return nota_minima if 0 <= nota_minima <= 10 else "IMPOSIBLE"
    return max(nota_minima,0) if nota_minima <= 10 else "IMPOSIBLE"



