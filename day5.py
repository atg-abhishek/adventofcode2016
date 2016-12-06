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
    res = list("aaaaaaaa")
    filled_positions = ""
    while (count<=8):
        s = inp+str(num)
        hexstring = hashlib.md5(s.encode()).hexdigest()
        if '00000' == hexstring[:5]:
            if hexstring[5] in '01234567':
                # if int(hexstring[5])<=7 and int(hexstring[5])>=0:
                if hexstring[5] not in filled_positions:
                    pprint(hexstring)
                    count += 1
                    res[int(hexstring[5])] = hexstring[6]
                    filled_positions += hexstring[5]
        num += 1
    return "".join(res)


# pprint(day5_part2("abbhdwsy"))