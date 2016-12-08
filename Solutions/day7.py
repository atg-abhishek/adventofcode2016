from pprint import pprint 
import re

lst = []
with open("../data/day7.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = ["abba[mnop]qrst","aaaa[qwer]tyui","ioxxoj[asdfgh]zxcvbn","abcd[bdib]lkoij[asdas]xyyx"] #test input 
# lst = ["aba[bab]xyz","xyx[xyx]xyx","aaa[kek]eke","zazbz[bzb]cdb"] #test input for part 2 

def day7_part1():
    global lst
    count = 0
    for l in lst:
        # the following flag is used to break out of the main for loop on detecting all conditions met
        hypernet_fail = False
        # following isolates the sequences between [ and ]
        hypernets = re.findall(r"\[[a-z]*\]", l)
        # now want to eliminate those sequences from the string 
        remaining = re.sub(r"\[[a-z]*\]", "-",l)
        # bringing all the other parts into a single string 
        remaining = remaining.split("-")
        for h in hypernets:
            # remove the opening and closing square brackets
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

def day7_part2():
    global lst
    count = 0
    for l in lst:
        
        hypernets = re.findall(r"\[[a-z]*\]", l)
        remaining = re.sub(r"\[[a-z]*\]", "-",l)
        remaining = remaining.split("-")
        d = set()
        # following finds all the places that meet the aba condition and places in them in a set so later we can check to find the corresponding bab sequence 
        for r in remaining:
            check_aba(r,d)
        # pprint(d)
        found_in_hypernet = False
        for seq in d:
            for h in hypernets:
                if seq in h:
                    # pprint(l)
                    found_in_hypernet = True
                    count += 1
                    break
            if found_in_hypernet:
                break
    return count
            


def check_abba(s):
    for i in range(0,len(s)-3):
        # following if block to remove the cases with same consecutive letters 
        if s[i] == s[i+1]:
            continue
        if s[i]+s[i+1] == s[i+3]+s[i+2]:
            return True
    return False

def check_aba(s,d):
    for i in range(0,len(s)-2):
        if s[i]==s[i+1]:
            continue
        if s[i] == s[i+2]:
            # adding directly into d the sequence needed to check for presence in the supernetsadd
            d.add(s[i+1]+s[i]+s[i+1])

        

pprint(day7_part2())