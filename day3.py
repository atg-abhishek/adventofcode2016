from pprint import pprint

lst = []
with open("day3.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

def day3():
    global lst
    count = 0
    for l in lst:
        sides = l.split(" ")
        sides = [s for s in sides if s is not ""]
        sides = [int(s) for s in sides]
        
        if valid_triangle(sides):
            count += 1
    return count

def day3_part2():
    global lst
    grid = []
    for l in lst:
        sides = l.split(" ")
        sides = [s for s in sides if s is not ""]
        sides = [int(s) for s in sides]
        grid.append(sides)
    count = 0
    flattened = [item for sublist in grid for item in sublist]
    for i in range(0,len(flattened)-6,9):
        for j in range(0,3):
            sides = []
            sides.append(flattened[i+j])
            sides.append(flattened[i+j+3])
            sides.append(flattened[i+j+6])
            if valid_triangle(sides):
                count += 1
    return count 

def valid_triangle(li):

    if li[0] + li[1] <= li[2]:
        return False
    if li[1] + li[2] <= li[0]:
        return False
    if li[0] + li[2] <= li[1]:
        return False
    return True

pprint(day3_part2())
# pprint(day3())