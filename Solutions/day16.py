from pprint import pprint 

inp = "10111011111001111"
disk_cap = 272


def day16():
    global inp, disk_cap
    disk_curr = 0
    data = inp
    while(disk_curr<=disk_cap):
        a = data
        b = a[::-1]
        new_b = ""
        for i in range(0, len(b)):
            if b[i] == '1':
                new_b += '0'
            else:
                new_b += '1'
        data = a + '0' + new_b
        disk_curr = len(data)
    chksum = checksum(data[:disk_cap])
    return chksum

def checksum(s):
    res = "" 
    while(len(res)%2==0):
        res = ""
        for i in range(0, len(s)-1,2):
            if s[i] == s[i+1]:
                res += '1'
            else:
                res += '0'
        s = res
    return res  
    
pprint(day16())
