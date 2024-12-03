import re
def multiply(file):
    data = file.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return sum(int(i) * int(j) for i,j in matches)

with open('day3\\input.txt') as f:
    print(multiply(f))