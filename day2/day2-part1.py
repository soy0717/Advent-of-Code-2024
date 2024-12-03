def safeOrUnsafe(file):
    l = file.readlines()
    safe = 0 
    for i in l:
        sub_list = [int(x) for x in i.split()]
        # This check if the sequence is strictly increasing or decreasing
        if not (sub_list == sorted(sub_list) or sub_list == sorted(sub_list, reverse=True)):
            continue
        # This check if two adjacent levels differ by at least 1 and at most 3
        distances = [abs(sub_list[x] - sub_list[x+1]) for x in range(len(sub_list)-1)]
        if not all(x in [1,2,3] for x in distances):
            continue
            
        safe += 1
    return safe

with open('day2\\input.txt') as f:
    print(safeOrUnsafe(f))
