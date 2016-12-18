from pprint import pprint 

# inp = ".^^.^.^^^^" # test input 1 
inp = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."

def day18():
    global inp
    num_rows = 400000 - 1 # part 2
    # num_rows = 40 - 1 # part 1
    prev_tiles = list(inp)
    grid = []
    grid.append(prev_tiles)
    count = 0
    count += inp.count(".")
    for i in range(0, num_rows):
        temp = []
        for i in range(0, len(prev_tiles)):
            
            left = center = right = ""
            if i==0:
                left = "."
                right = prev_tiles[i+1]
            if i==len(prev_tiles)-1:
                left = prev_tiles[i-1]
                right = "."
            if i>=1 and i<=len(prev_tiles)-2:
                left = prev_tiles[i-1]
                right = prev_tiles[i+1]
            center = prev_tiles[i]
            if not safe_tile(left, center, right):
                count += 1
                temp.append(".")
                continue
            temp.append("^")
        prev_tiles = temp
        grid.append(temp)
    
    # for x in grid:
    #     row = ""
    #     for y in x:
    #         row += y
    #     pprint(row)

    return count
            

def safe_tile(left, center, right):
    if left == "^" and center == "^" and right == ".":
        return True
    if center == "^" and right == "^" and left == ".":
        return True
    if left == "^" and center == "." and right == ".":
        return True
    if left == "." and center == "." and right == "^":
        return True
    return False

pprint(day18())