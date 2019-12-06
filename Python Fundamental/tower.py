def tower(floor,blocksize): # blocksize = lebar dan tinggi

    space = floor
    tng = blocksize
    out = ''
    for i in range (floor):
        for i in range (space):
            out += ' '
        for i in range (tng):
            out += '*'
        out += '\n'
        tng += 1
        space += 1
    print(out)

tower(6,10)



