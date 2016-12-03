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
        
def valid_triangle(li):

    if li[0] + li[1] <= li[2]:
        return False
    if li[1] + li[2] <= li[0]:
        return False
    if li[0] + li[2] <= li[1]:
        return False
    return True

pprint(day3())