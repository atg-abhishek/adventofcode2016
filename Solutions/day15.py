from pprint import pprint

lst = []

with open("../Data/day15.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["Disc #1 has 5 positions; at time=0, it is at position 4.", "Disc #2 has 2 positions; at time=0, it is at position 1."] #test input 

def day15():
    global lst
    disks = []
    for l in lst:
        temp = l.split(" ")
        # disk number, initial position, total number of positions
        disks.append((int(temp[1][1]), int(temp[-1][0]), int(temp[3]) ))
    time = 0
    success = False
    while (not success):
        res = determine_positions(time, disks)
        non_zero = False
        for r in res:
            if r[1] != 0:
                non_zero = True
                break
        if non_zero:
            time += 1
            continue
        else:
            break
    return time
            

def determine_positions(time, disks):
    res = []
    time = time + 1
    for d in disks:
        disk_num = d[0]
        init_pos = d[1]
        total_pos = d[2]
        final_pos = (init_pos + time)%total_pos
        res.append((disk_num, final_pos))
        time = time + 1
    return res

pprint(day15())