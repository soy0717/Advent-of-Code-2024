def safeOrUnsafe(file):
    l = file.readlines()
    safe = 0 
    for i in l:
        sub_list = [int(x) for x in i.split()]
        distances = [abs(sub_list[x] - sub_list[x+1]) for x in range(len(sub_list)-1)]
        if not (sub_list == sorted(sub_list) or sub_list == sorted(sub_list, reverse=True)):
            continue
        if not all(x in [1,2,3] for x in distances):
            continue
        safe += 1
    return safe

print(safeOrUnsafe(open('input.txt')))