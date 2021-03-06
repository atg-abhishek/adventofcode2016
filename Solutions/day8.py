from pprint import pprint 

lst = []
with open("../data/day8.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"] # test input 

# main grid used to carry out all the operations
grid = []
height = 6
width = 50
for i in range(0,height):
    temp = []
    for j in range(0,width):
        # empty indicates there it is off
        temp.append(" ")
    grid.append(temp)

def day8():
    count = 0
    global grid, height, width
    for l in lst:
        # pprint(l)
        # following disassemble all the instructions 
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
            if grid[i][j] == "*":
                count += 1
    # following creates a graphical display at the end 
    for i in range(0,height):
        row = grid[i]
        pprint("".join(row))
    return count   

def rotate_row(row_num, amount):
    row_num = int(row_num)
    amount = int(amount)
    global grid
    row = grid[row_num]
    res = [" " for i in range(0, len(row))]
    for i in range(0,len(row)):
        # following helps with the rotation 
        res[(i+amount)%len(row)] = row[i]
    grid[row_num] = res

def rotate_col(col_num, amount):
    col_num = int(col_num)
    amount = int(amount)
    global grid, height, width
    temp = [" " for i in range(0,height)]
    # following assimilates all the elements from the column into a single list so it is easy to process
    for i in range(0,height):
        temp[i] = grid[i][col_num]
    res = [" " for i in range(0,height)]
    # filling the shifted list 
    for i in range(0,height):
        res[(i+amount)%height] = temp[i]
    # reassigning the elements in the grid after the shift 
    for i in range(0,height):
        grid[i][col_num] = res[i]

def rect(a,b):
    global grid 
    a = int(a)
    b = int(b)
    for row in range(0, a):
        for col in range(0, b):
            # star indicates that the pixel is lit up 
            grid[row][col] = "*"

pprint(day8())