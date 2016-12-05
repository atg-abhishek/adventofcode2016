from pprint import pprint 
from collections import defaultdict
import operator, json
lst = []
with open("day4.txt") as infile:
    data = infile.read()
    lst = data.splitlines()

# lst = lst[:1]

def day4_part1():
    global lst
    total = 0
    valid_rooms = []
    for l in lst:
        # separating the different parts of the input 
        items = l.split("-")
        last = items[-1]
        enc = items[:-1]
        sector_id = last[:3]
        frequency = last[3:]
        frequency = frequency.replace("[", "")
        frequency = frequency.replace("]","")
        # d will store the initial character frequency
        d = defaultdict(int)
        for stub in enc:
            chars = list(stub)
            for c in chars:
                if d[c] is None:
                    d[c] = 1
                else:
                    d[c] = d[c] + 1
        # sorting the dict so that the highest frequency letters are at the top
        sorted_dict = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        # flipping the list to have value - key pairs 
        flipped_sorted_dict = [(v,k) for (k,v) in sorted_dict]
        # grouping characters by their frequency 
        frequency_to_char = defaultdict(list)
        for entry in flipped_sorted_dict:
            frequency_to_char[entry[0]].append(entry[1])
        # sorting the above grouping by frequency
        sorted_frequency_to_char = sorted(frequency_to_char.items(), key=operator.itemgetter(0), reverse=True)
        # sorting the alphabets lexically within the frequency
        sorted_list_by_freq_and_lexical = []
        for entry in sorted_frequency_to_char:
            temp = sorted(entry[1])
            sorted_list_by_freq_and_lexical.append((entry[0],temp))
        # creating the final list to be used 
        final_list = []
        for entry in sorted_list_by_freq_and_lexical: 
            final_list += entry[1]
        
        if check_valid_room(final_list, frequency):
            total += int(sector_id)
            valid_rooms.append(l)
    # writing result to file to use for second part         
    with open("day4_part1_results.json",'w') as outfile:
        json.dump({"total" : total, "valid_rooms" : valid_rooms}, outfile) 

def check_valid_room(sorted_dict, checksum):
    # checks if the checksum matches the frequency order in the final list
    for i in range(0,5):
        if sorted_dict[i][0] != checksum[i]:
            return False
    return True

def day4_part2():
    data = {}
    with open("day4_part1_results.json") as infile:
        data = json.load(infile)
    raw_valid_rooms = data['valid_rooms']
    for room in raw_valid_rooms:
        items = room.split("-")
        name = items[:-1]
        sector_id = items[-1][:3]
        res = ""
        for part in name:
            res += shift_decrypt(part, int(sector_id)) + " "
        if "pole" in res:
            pprint(sector_id)
            

def shift_decrypt(s, shift):
    start_index = ord('a')  
    res = ""
    for char in s:
        # getting ascii value of char and then bringing it in 0 to 25 range by subtracting the value of 'a' and then adding the shift value 
        # this is modded by 26 to keep from overflowing and then 'a' is added back to convert it back to the character
        new_char = chr(((ord(char)-start_index+shift)%26)+start_index)
        res += new_char
    return res

day4_part2()
# pprint(shift_decrypt('bmvyz',4))
# pprint(day4())