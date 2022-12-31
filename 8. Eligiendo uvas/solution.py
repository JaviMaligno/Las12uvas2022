def best_grape(grapes):
    grapes = grapes[:-2] #ignoring 0's
    taste = grapes[::2]
    skin = grapes[1::2]
    description = list(zip(taste, skin))
    best_taste = max(description, key = lambda x: x[0])
    best_skin = max(description, key = lambda x: -x[1])
    return best_taste if best_taste == best_skin else "NO HAY MEJOR"

print(best_grape([7, 1, 6, 2, 5, 2, 0, 0]), best_grape([7, 3, 8, 4, 0, 0]))