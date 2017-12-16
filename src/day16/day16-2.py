instructions = open('input.txt').readlines()[0].split(',')
dancers = [chr(x) for x in range(ord('a'), ord('p')+1)]
it = 0
startends = {}
while it < 1000000000:
    start = "".join(dancers)
    if start in startends :
        dancers = startends[start]
    else :
        for instr in instructions:
            if instr[0] == 's':
                permut = int(instr[1:])
                dancers = dancers[-permut:] + dancers[0:-permut]
            else :
                i = 0
                j = 0
                if instr[0] == 'x' :
                    spt = instr[1:].split('/')
                    i = int(spt[0])
                    j = int(spt[1])
                else:
                    i = dancers.index(instr[1])
                    j = dancers.index(instr[3])
                dancers[i], dancers[j] = dancers[j], dancers[i]
        startends[start] = dancers.copy()
    it += 1
print("".join(dancers))
