from pprint import pprint 

lst = []
with open("../data/day8.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"] # test input 

grid = []
height = 6
width = 50
for i in range(0,height):
    temp = []
    for j in range(0,width):
        temp.append(False)
    grid.append(temp)

def day8():
    count = 0
    global grid, height, width
    for l in lst:
        # pprint(l)
        instructions = l.split(" ")
        if instructions[0] == 'rect':
            nums = instructions[1].split('x')
            rect(nums[1],nums[0])
        if instructions[0] == 'rotate':
            if instructions[1] == 'row':
                rotate_row(instructions[2].split("=")[1],instructions[-1])
            else:
                rotate_col(instructions[2].split("=")[1],instructions[-1])
        # pprint(grid)
    
    for i in range(0,height):
        for j in range(0,width):
            if grid[i][j]:
                count += 1
    return count   

def rotate_row(row_num, amount):
    row_num = int(row_num)
    amount = int(amount)
    global grid
    row = grid[row_num]
    res = [False for i in range(0, len(row))]
    for i in range(0,len(row)):
        res[(i+amount)%len(row)] = row[i]
    grid[row_num] = res

def rotate_col(col_num, amount):
    col_num = int(col_num)
    amount = int(amount)
    global grid, height, width
    temp = [False for i in range(0,height)]
    for i in range(0,height):
        temp[i] = grid[i][col_num]
    res = [False for i in range(0,height)]
    for i in range(0,height):
        res[(i+amount)%height] = temp[i]
    for i in range(0,height):
        grid[i][col_num] = res[i]

def rect(a,b):
    global grid 
    a = int(a)
    b = int(b)
    for row in range(0, a):
        for col in range(0, b):
            grid[row][col] = True

pprint(day8())