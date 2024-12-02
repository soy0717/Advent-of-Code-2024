def safeOrUnsafe(file):
    l = file.readlines()
    safe = 0 
    for i in l:
        sub_list = [int(x) for x in i.split()]
        # Function to check if a given sequence is safe
        def is_safe(seq):
            is_sorted = all(seq[x] < seq[x+1] for x in range(len(seq)-1)) or all(seq[x] > seq[x+1] for x in range(len(seq)-1))
            distances = all(y in [1,2,3] for y in [abs(seq[x] - seq[x+1]) for x in range(len(seq)-1)])
            return is_sorted and distances

        # This checks is the sequence is safe with the new condition
        if is_safe(sub_list): 
            safe += 1
        else:
            for j in range(len(sub_list)):
                if is_safe(sub_list[:j] + sub_list[j+1:]): 
                    safe += 1
                    break
    return safe

print(safeOrUnsafe(open('input.txt')))
