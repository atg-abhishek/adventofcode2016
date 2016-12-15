from pprint import pprint 
from collections import defaultdict
from hashlib import md5
import re,json

d = defaultdict(list)
li = []
res = []
count = 0
def day14(salt, key_stretching):
    global d, li, count 
    index = 0
    # initializing the list with a 1001 hashes 
    while(index<=1000):
        plaintext = salt + str(index)
        hashtext = plaintext
        if key_stretching:
            for i in range(0,2017):
                hashtext = md5(hashtext.encode()).hexdigest().lower()
                # plaintext = hashtext
        else:
            hashtext = md5(plaintext.encode()).hexdigest().lower()
        li.append(hashtext)
        triples = getTriples(hashtext)
        d[hashtext] = triples
        index += 1
    while (count<64):
        testhash = li[index-1001]
        if len(d[testhash]) != 0:
            if check_valid_key(d[testhash][0][1],index-1000):
                count += 1
                pprint(count)

        plaintext = salt+str(index)
        hashtext = plaintext
        if key_stretching:
            for i in range(0,2017):
                hashtext = md5(hashtext.encode()).hexdigest().lower()
                # plaintext = hashtext
        else:
            hashtext = md5(plaintext.encode()).hexdigest().lower()
        li.append(hashtext)
        triples = getTriples(hashtext)
        d[hashtext] = triples
        index += 1
    
    with open('day14_res_2016.json','w') as outfile:
        json.dump({"res" : res},outfile)
    return res[-1][1]

def getTriples(s):
    triples = re.findall(r'((\w)\2{2,})',s)
    return triples

def check_valid_key(letter, idx):
    global d, li, res
    for i in range(idx, idx+1000):
        trips = d[li[i]]
        trips = [x[0] for x in trips]
        if letter*5 in trips:
            res.append((li[idx-1],idx-1,li[i],i,count))
            return True
    return False

# pprint(day14("ahsbgdzn", False)) # for part 1 
pprint(day14("ahsbgdzn", True))
