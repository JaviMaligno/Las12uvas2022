from collections import defaultdict
def no_emparejados(calcetines):
    vistos = defaultdict(bool)
    max_no_emparejados = 0
    actual_no_emparejados = 0
    for calcetin in calcetines:
        actual_no_emparejados -= 1 if vistos[calcetin] else -1
        vistos[calcetin] = not vistos[calcetin]
        max_no_emparejados = max(max_no_emparejados, actual_no_emparejados)
    return max_no_emparejados

#print(no_emparejados([1, 2, 1, 1, 1, 2]))

