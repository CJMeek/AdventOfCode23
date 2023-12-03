import re

data = open('AdventOfCode23/Day1/input.txt', 'r').read().split('\n')

vals = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9e"
}

total = 0

num_reg = re.compile(r"\d")

for line in data:
    for k,v in vals.items():
        line = line.replace(k,v)
        
    digits = num_reg.findall(line)
    first_dig = digits[0]
    last_dig = digits[-1]
    
    total += int(f"{first_dig}{last_dig}")
        
    

print(total)
