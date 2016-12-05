from pprint import pprint 
from collections import defaultdict
import operator
lst = []
with open("day4.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = lst[:1]

def day4():
    global lst
    total = 0
    for l in lst:
        items = l.split("-")
        last = items[-1]
        enc = items[:-1]
        sector_id = last[:3]
        frequency = last[3:]
        frequency = frequency.replace("[", "")
        frequency = frequency.replace("]","")
        d = defaultdict(int)
        for stub in enc:
            chars = list(stub)
            for c in chars:
                if d[c] is None:
                    d[c] = 1
                else:
                    d[c] = d[c] + 1
        sorted_dict = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        flipped_sorted_dict = [(v,k) for (k,v) in sorted_dict]
    
        frequency_to_char = defaultdict(list)
        for entry in flipped_sorted_dict:
            frequency_to_char[entry[0]].append(entry[1])
        sorted_frequency_to_char = sorted(frequency_to_char.items(), key=operator.itemgetter(0), reverse=True)
        
        sorted_list_by_freq_and_lexical = []
        for entry in sorted_frequency_to_char:
            temp = sorted(entry[1])
            sorted_list_by_freq_and_lexical.append((entry[0],temp))
        
        final_list = []
        for entry in sorted_list_by_freq_and_lexical: 
            final_list += entry[1]
        
        if check_valid_room(final_list, frequency):
            total += int(sector_id)
    return total

def check_valid_room(sorted_dict, checksum):
    for i in range(0,5):
        if sorted_dict[i][0] != checksum[i]:
            return False
    return True

pprint(day4())