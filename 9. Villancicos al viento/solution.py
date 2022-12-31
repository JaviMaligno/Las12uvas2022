from collections import defaultdict
def number_of_houses(houses):
    n_houses = 0
    hearing = defaultdict(bool)
    for house, number in enumerate(houses):
        start = 0 if number > house else house-number
        for i in range(start,house):
            n_houses += 1 if not hearing[i] else 0
            hearing[i] = True
    return n_houses

print(number_of_houses([1, 0, 1]), number_of_houses([0, 1, 0, 1, 2]))

