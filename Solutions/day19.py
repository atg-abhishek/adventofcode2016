from pprint import pprint 

inp = 3018458
# inp = 5 # test input 
lst = []

def day19():
    global inp, lst
    
    # initializing each elf with a present 
    for i in range(0,inp):
        lst.append([i,1])
    count = 0
    i = 0
    # this will keep track of how many elves have had their presents taken away 
    while(count!=inp-1):
        # pprint(lst)
        
        if lst[i][1] != 0:
            # idx = next_valid_index(i+1)
            j = (i+1)%inp
            while(lst[j][1]==0):
                j = (j+1)%inp
            # pprint(" i is " + str(i) + " j is " + str(j))
            lst[i][1] += lst[j][1]
            lst[j][1] = 0
            count += 1 
        i = (i+1)%inp
    # pprint(lst)
    for l in lst:
        if l[1]!=0:
            return l[0]+1

# def next_valid_index(curr_idx):
#     global lst, inp
#     while(lst[(curr_idx+1)%inp][1]==0):
#         curr_idx = (curr_idx+1)%inp
#     return curr_idx

pprint(day19())
