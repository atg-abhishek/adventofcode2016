from pprint import pprint 

lst = []
inp = 4294967295

with open("../Data/day20.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["5-8","0-2","4-7"] # test input 

def day20():
    global lst, inp
    res = []
    for i in range(0,inp+1):
        res.append(True) # all IPs are allowed in the beginning
    pprint("Done initializing")
    for l in lst:
        temp = l.split("-")
        start = int(temp[0])
        end = int(temp[1])
        for i in range(start, end+1):
            res[i] = False
    pprint("Done accepting the blacklists")
    count = 0
    for i in range(0, len(res)):
        if res[i]:
            count += 1

    return count 

pprint(day20())