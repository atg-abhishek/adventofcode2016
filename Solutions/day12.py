from pprint import pprint 

lst = []
with open("../data/day12.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"] #test input

d = {'a':0, 'b':0,'c':0,'d':0}

def day12(part):
    global d, lst
    if part == "part2":
        d['c'] = 1
    i = 0
    while(i<len(lst)):
        instructions = lst[i].split(" ")
        task = instructions[0]
        if task == 'cpy':
            copy(instructions[1],instructions[2])
        if task == 'inc':
            inc(instructions[1])
        if task == 'dec':
            dec(instructions[1])
        if task == 'jnz':
            x = instructions[1]
            execute = False
            if x in 'abcd':
                if d[x] != 0:
                    execute = True
            else:
                if int(x) != 0:
                    execute = True
            if execute:
                y = int(instructions[2])
                if y>1 or y<=-1:
                    i = i + y
                    continue
                
        i = i+1
    return d['a']

def copy(val, reg):
    global d
    if val in 'abcd':
        d[reg] = d[val]
    else:
        d[reg] = int(val)

def inc(reg):
    global d
    
    d[reg] = d[reg] + 1

def dec(reg):
    global d
    d[reg] = d[reg] - 1



pprint(day12("part2"))