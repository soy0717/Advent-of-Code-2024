def distance(file):
    data = file.readlines()
    l1 = sorted([int(i.split()[0]) for i in data])
    l2 = sorted([int(i.split()[1]) for i in data])
    dist = sum([abs(l1[i] - l2[i]) for i in range(len(data))])
    return dist

print(distance(open('input.txt')))