import re
def multiply(file):
    data = file.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    enabled = True
    matches = re.finditer(pattern, data)
    sum = 0
    
    for i in matches:
        x = i.group(0)
        if x == "don't()":
            enabled = False
        elif x == 'do()':
            enabled = True
        else:
            if enabled == True:
                n1, n2 = int(i.group(1)), int(i.group(2))
                sum += n1 * n2
    return sum

with open('day3\\input.txt') as f:
    print(multiply(f))