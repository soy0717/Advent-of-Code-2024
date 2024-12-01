def similarity_score(file):
    l = file.readlines()
    l1 = [int(i.split()[0]) for i in l]
    l2 = [int(i.split()[1]) for i in l]
    score = sum([i*l2.count(i) for i in l1])
    return score

print(similarity_score(open('input.txt')))