def turron(case):
    time = case[0]
    line1 = case[1]
    line2 = case[2]
    if line1 and line2:
        piece1 = line1[-1]
        piece2 = line2[-1]
        if piece1 <= piece2:
            line1 = line1[:-1] 
            remaining_time = time-piece1    
        else: 
            line2 = line2[:-1]     
            remaining_time = time-piece2    
    elif line1:
        piece1 = line1[-1]
        line1 = line1[:-1] 
        remaining_time = time-piece1
    else:
        piece2 = line2[-1]        
        line2 = line2[:-1]     
        remaining_time = time-piece2
    case = [remaining_time,line1,line2]
    return 1+turron(case) if remaining_time >= 0 else 0



def test_cases(test):
    lines = list(map(lambda x: tuple(map(int,x.split(' '))), test.splitlines()))
    cases = [[lines[i][-1],*lines[i+1:i+3]] for i in range(0,len(lines),3)]
    return cases


test = """3 2 2
2 2 1
2 1
3 5 5
1 3 3
2 1 1 1 1"""


for case in test_cases(test):
    print(turron(case))