def jumpingOnClouds(c):
    jumps = 0
    i = 0 
    while i != len(c) - 1:                  #Careful here, because if it is i < len(c) il will iterate one more time
        if i < len(c) - 2:                  #Check if e did not get out of range
            i += 2 if c[i + 2] != 1 else 1
        else:
            i += 1
        jumps += 1
    return jumps