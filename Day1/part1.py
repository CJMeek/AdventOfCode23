import re

data = open('AdventOfCode23/Day1/input.txt', 'r').read().split('\n')

total = 0

num_reg = re.compile(r"\d")

def getCallibrationVal(line):
    digits = num_reg.findall(line)
    first_dig = digits[0]
    last_dig = digits[-1]
    
    global total
    total += int(f"{first_dig}{last_dig}")


for line in data:
    getCallibrationVal(line)

print(total)

