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
        # removing the blank entries in the list 
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
    # flattening the grid of values in to a vector 
    flattened = [item for sublist in grid for item in sublist]
    # going up to -6 because iteration works by walking along every row of input and then getting the 3 values below them to form the sides for the triangle. Meaning 9 values are processed at a time.
    for i in range(0,len(flattened)-6,9):
        # the following loop is used to walk along one row and collect the elements below it 
        for j in range(0,3):
            sides = []
            sides.append(flattened[i+j])
            sides.append(flattened[i+j+3])
            sides.append(flattened[i+j+6])
            if valid_triangle(sides):
                count += 1
    return count 

def valid_triangle(li):
    # checking the side sum rule for triangles
    if li[0] + li[1] <= li[2]:
        return False
    if li[1] + li[2] <= li[0]:
        return False
    if li[0] + li[2] <= li[1]:
        return False
    return True

pprint(day3_part2())
# pprint(day3())