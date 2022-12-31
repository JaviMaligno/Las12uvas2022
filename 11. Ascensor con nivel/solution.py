def min_rank(lifts, final_level = 10):
    min_lift = min([lift for lift in lifts if lift[0] < final_level <= lift[1]], key = lambda x: x[2])
    min_level = min_lift[2]
    if final_level == 1:
        return min_level
    else:
        return max(min_level, min_rank(lifts, final_level= final_level-1))

def lifts(text):
    lift_list = list(map(lambda x: tuple(map(int,x.split(' '))), text.splitlines()))
    final_level = max(lift[1] for lift in lift_list)
    return lift_list, final_level
test = """0 3 3\n3 10 11\n0 4 2\n2 8 6\n8 10 8"""

print(min_rank(lifts(test)[0]))
