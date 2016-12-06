from pprint import pprint 
from collections import defaultdict
import operator
lst = []
with open("day6.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

def day6(part):
    global lst
    res = ""
    # d stores the char positions and then has a list of all chars encountered there
    d = defaultdict(list)
    for l in lst:
        chars = list(l)
        for i in range(len(chars)):
            d[i].append(chars[i])
    for x in d.items():
        char = find_most_frequent_char(x[1], part)
        res += char
    return res

# helps to find the most frequent char in the list or for part 2 the least frequent char 
def find_most_frequent_char(li, part):
    # d stores the frequency of each char 
    d = defaultdict(int)
    for l in li:
        if d[l] is None:
            d[l] = 1
        else:
            d[l] += 1
    # following gets the chars by their frequency 
    sorted_dict = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    if part == "part1":
        return sorted_dict[0][0]
    else:
        return sorted_dict[-1][0]

pprint(day6("part1"))