from pprint import pprint 
import hashlib

def day5(inp):
    count = 1
    num = 0
    res = ""
    while(count<=8):
        s = inp+str(num)
        hexstring = hashlib.md5(s.encode()).hexdigest()
        if '00000' == hexstring[:5]:
            pprint(hexstring)
            count += 1
            res += hexstring[5]
        num += 1
    return res
    

pprint(day5("abbhdwsy"))