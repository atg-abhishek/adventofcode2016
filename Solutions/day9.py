from pprint import pprint 

inp = ""
with open("../data/day9.txt") as infile:
    inp = infile.read()



def day9():
    global inp
    i = 0
    count = 0
    # pprint(inp)
    while i<len(inp):
        # pprint("Count is " + str(count))
        num_chars = 0
        num_times = 0
        # pprint(inp[i])
        marker_detected = False
        if inp[i] == "(":
            marker_detected = True
            temp = ""
            i = i + 1
            while(inp[i] != ')'):
                temp += inp[i]
                i = i + 1
            temp = temp.split("x")
            num_chars = int(temp[0])
            num_times = int(temp[1])
            i = i + 1 # to come to the next character after the marker 
            # pprint("*"+inp[i])
            i = i + num_chars 
            # pprint("**"+inp[i])
            count += num_chars*num_times
            # pprint(count )
        if not marker_detected:
            i = i + 1
            count += 1
    return count 

# pprint(day9())
# li = ["ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG", "(6x1)(1x3)A", "X(8x2)(3x3)ABCY"]
# # li = li[3:4]
# for l in li:
#     pprint(day9(l))

pprint(day9())