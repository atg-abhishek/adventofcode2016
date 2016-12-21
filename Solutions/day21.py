from pprint import pprint
from itertools import permutations

lst = []
# password = list("abcde") # test input 

# password = list("bdeac") #test input 

# password = list("abcdefgh") # for first part 
password = list("fbgdceah") # for second part 
rev = False # True indicates that we need to scramble

with open("../Data/day21.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["swap position 4 with position 0", "swap letter d with letter b", "reverse positions 0 through 4", "rotate left 1 step", "move position 1 to position 4", "move position 3 to position 0", "rotate based on position of letter b", "rotate based on position of letter d"] # test input 

def day21():
    global lst, password
    for l in lst:
        temp = l.split(" ")
        if "move" in temp:
            index_x = int(temp[2])
            index_y = int(temp[5])
            # if rev:
            #     p = index_x
            #     index_x = index_y
            #     index_y = p
            move(index_x, index_y)
            continue
        if "rotate" in temp:
            if "based" in temp:
                letter = temp[-1]
                rotate_index(letter)
                continue
            else:
                direction = temp[1]
                steps = int(temp[-2])
                # if rev:
                #     if direction == "right":
                #         direction = "left"
                #     else:
                #         direction = "right"
                rotate(direction, steps) 
                continue
        if "reverse" in temp:
            index_x = int(temp[-3])
            index_y = int(temp[-1])
            reverse(index_x, index_y)
            continue
        if "swap" in temp:
            if "position" in temp:
                index_x = int(temp[-4])
                index_y = int(temp[-1])
                # if rev:
                #     p = index_x 
                #     index_x = index_y
                #     index_y = p
                swap(index_x, index_y)
            else:
                letter_x = temp[-4]
                letter_y = temp[-1]
                # if rev:
                #     p = letter_x
                #     letter_x = letter_y
                #     letter_y = p
                swap_letters(letter_x, letter_y)


def swap(index_x, index_y):
    global password
    temp = password[index_x]
    password[index_x] = password[index_y]
    password[index_y] = temp

def swap_letters(letter_x, letter_y):
    index_x = index_y = 0
    global password
    for i in range(0, len(password)):
        if password[i] == letter_x:
            index_x = i
        if password[i] == letter_y:
            index_y = i
    swap(index_x, index_y)

def rotate(direction, steps):
    global password
    if direction == "left":
        steps = (-1)*steps
    temp = list("0"*len(password))
    for i in range(0, len(password)):
        temp[(i+steps)%len(password)] = password[i]
    password = temp

def rotate_index(letter_x):
    steps = 0
    global password
    for i in range(0, len(password)):
        if password[i] == letter_x:
            steps = i
            break
    if steps>=4: # if it is more than 4 than do it once more than 4 
        steps += 1
    steps += 1 # for the additional one time
    # if rev:
    #     rotate("left", steps)
    # else:
    rotate("right", steps)

def reverse(index_x, index_y):
    global password
    sublist = password[index_x:index_y+1]
    temp = []
    for i in range(0, len(sublist)):
        temp.append(sublist[len(sublist)-1-i])
    res = list("0"*len(password))
    res[0:index_x] = password[0:index_x]
    res[index_x:index_y+1] = temp
    res[index_y+1:] = password[index_y+1:]
    password = res

def move(index_x, index_y):
    letter = password[index_x]
    del password[index_x]
    password.insert(index_y,letter) 


def part2():
    global password
    temp = password
    for s in permutations(temp):
        s = ''.join(s)
        password = list(s)
        day21()
        if password == temp:
            pprint(s)

        

part2()

