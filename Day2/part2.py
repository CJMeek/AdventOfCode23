import re

debug = False

data = ""

sum = 0

red, blue, green = 12, 14, 13

id_reg = re.compile(r"\d+")

bag_reg = re.compile(r"(\d+) (\w)")

if(debug):
    data = open('Day2/test.txt', 'r').read().split('\n')
else:
    data = open('Day2/input.txt', 'r').read().split('\n')

for line in data:

    id_split = line.split(':')

    bags = id_split[1].split(";")

    maxCubes = {'r':0, 'b':0, 'g':0}

    win = True

    for bag in bags:

        cubes = {'r':0, 'b':0, 'g':0}

        for num, colour in bag_reg.findall(bag):
            cubes[colour] += int(num)
    
        for colour in maxCubes:
            maxCubes[colour] = max(maxCubes[colour], cubes[colour])
    sum += maxCubes['r'] * maxCubes['b'] * maxCubes['g']

print(sum)


            
            
        

            
        



    

    


    

    

