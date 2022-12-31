from itertools import combinations
from collections import defaultdict
def max_perimetro(lados):
    # de nuevo el número de lados viene dado como input aunque no sea necesario, esta vez no lo usaré
    n_lados = len(lados)
    if n_lados < 3:
        return "NO HAY NINGUNO"
    max_perimeter = 0
    visited_triple = defaultdict(bool)
    # to make it efficient I would have to rewrite combinations so that it doesn't produce repeated combinations when there are repeated elements https://docs.python.org/3/library/itertools.html#itertools.combinations
    # I going to just check if I have been to that triple before
    for triple in combinations(lados, 3): 
        if visited_triple[triple]:
            continue
        else:
            current_perimeter = perimetro(triple) 
            max_perimeter = current_perimeter if max_perimeter < current_perimeter else max_perimeter
    return max_perimeter if max_perimeter > 0 else "NO HAY NINGUNO"

    

def perimetro(tres_lados):
    lado0 = tres_lados[0]
    lado1 = tres_lados[1]
    lado2 = tres_lados[2]
    return sum(tres_lados) if abs(lado1 - lado0) < lado2 < lado0 + lado1 else 0


print(max_perimetro([1, 2, 2, 1, 2]))
print(max_perimetro([1, 1, 10]))

