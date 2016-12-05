from pprint import pprint 

inp = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

deb = False

# indicating the part gives the result for that particular day
# indicating the debug will print out the path that it traverses
def day1(part, debug=False):
    global deb
    if debug:
        deb = True
    # used to indicate position on the grid 
    horizontal = 0
    vertical = 0
    face = "north"
    # d will keep track of points traveled to so far 
    d = {(0,0)}
    directions = inp.split(", ")
    for step in directions:
        debug_print("Step is " + step)
        turn = step[0]
        dist = int(step[1:])
        # face indicates which way you're facing 
        face = move_result_calculator(turn, face)
        if face is "north":
            # the outer if works for the simple case of part 1
            if part is "part2":
                # the for loop is used to actually mark all points between start and stop points as visited to check which is the first point where there is an overlap 
                for i in range(vertical+1, vertical+dist+1): # starting from +1 to avoid checking the same spot as the one last standing on
                    debug_print("[North] Going to " + str(horizontal) + "," + str(i))
                    # at every point check whether it has been visited already 
                    if (horizontal, i) in d:
                        return (horizontal, i)
                    else:
                        d.add((horizontal, i))
            vertical += dist
        if face is "south":
            if part is "part2":
                for i in range(vertical-1,vertical-dist-1,-1):
                    debug_print("[South] Going to " + str(horizontal) + "," + str(i))
                    if (horizontal, i) in d:
                        return (horizontal, i)
                    else:
                        d.add((horizontal, i))
            vertical -= dist
        if face is "west":
            if part is "part2":
                for i in range(horizontal-1, horizontal-dist-1,-1):
                    debug_print("[West] Going to " + str(i) + "," + str(vertical))
                    if (i, vertical) in d:
                        return (i, vertical)
                    else:
                        d.add((i, vertical))
            horizontal -= dist
        if face is "east":
            if part is "part2":
                for i in range(horizontal+1, horizontal+dist+1):
                    debug_print("[East] Going to " + str(i) + "," + str(vertical))
                    if (i, vertical) in d:
                        return (i, vertical)
                    else:
                        d.add((i, vertical))
            horizontal += dist
        
        debug_print("Now at "+str(horizontal)+","+str(vertical))
        debug_print("**********************************")
    if part is not "part2":
        return horizontal+vertical # for part 1

def move_result_calculator(turn, face):
    # calculates which way you are facing given current orientation and turn value 
    res = ""
    if turn is "L":
        if face is "north":
            res = "west"
        if face is "west":
            res = "south"
        if face is "south":
            res = "east"
        if face is "east":
            res = "north"
    if turn is "R":
        if face is "north":
            res = "east"
        if face is "east":
            res = "south"
        if face is "south":
            res = "west"
        if face is "west":
            res = "north"
    return res

def debug_print(s):
    global deb
    if deb:
        pprint(s)

pprint(day1("part2", True))