from pprint import pprint 
import hashlib

def day5_part1(inp):
    count = 1
    num = 0
    res = ""
    # looping till we find 8 characters for the password 
    while(count<=8):
        s = inp+str(num)
        hexstring = hashlib.md5(s.encode()).hexdigest()
        # checking if this is an "interesting" hash
        if '00000' == hexstring[:5]:
            pprint(hexstring)
            count += 1
            res += hexstring[5]
        num += 1
    return res

def day5_part2(inp):
    count = 1
    num = 0
    # empty list for the password
    res = list("aaaaaaaa")
    # will be used to keep track of the positions that have been filled
    filled_positions = ""
    while (count<=8):
        s = inp+str(num)
        hexstring = hashlib.md5(s.encode()).hexdigest()
        if '00000' == hexstring[:5]:
            # makes sure that the index is valid
            if hexstring[5] in '01234567':
                # makes sure that the index has not already been filled 
                if hexstring[5] not in filled_positions:
                    pprint(hexstring)
                    count += 1
                    res[int(hexstring[5])] = hexstring[6]
                    filled_positions += hexstring[5]
        num += 1
    return "".join(res)


pprint(day5_part2("abbhdwsy"))