from pprint import pprint 
import re

lst = []
with open("../data/day7.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["abba[mnop]qrst","aaaa[qwer]tyui","ioxxoj[asdfgh]zxcvbn","abcd[bdib]lkoij[asdas]xyyx"] #test input 

def day7():
    global lst
    count = 0
    for l in lst:
        pprint(l)
        hypernet_fail = False
        hypernets = re.findall(r"\[[a-z]*\]", l)
        remaining = re.sub(r"\[[a-z]*\]", "-",l)
        remaining = remaining.split("-")
        for h in hypernets:
            if check_abba(h[1:-1]):
                hypernet_fail = True
                break
        if hypernet_fail:
            continue
        for r in remaining:
            if check_abba(r):
                count += 1
                break
        
    return count

def check_abba(s):
    for i in range(0,len(s)-3):
        if s[i] == s[i+1]:
            continue
        if s[i]+s[i+1] == s[i+3]+s[i+2]:
            return True
    return False


pprint(day7())