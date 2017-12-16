instructions = open('input.txt').readlines()[0].split(',')
dancers = [chr(x) for x in range(ord('a'), ord('p')+1)]
for instr in instructions:
    if instr[0] == 's':
        permut = int(instr[1:]) % len(dancers)
        dancers = dancers[-permut:] + dancers[0:-permut]
    else :
        i = 0
        j = 0
        if instr[0] == 'x' :
            i = int(instr[1:instr.index('/')])
            j = int(instr[instr.index('/')+1:])
        else:
            i = dancers.index(instr[1])
            j = dancers.index(instr[3])
        dancers[i], dancers[j] = dancers[j], dancers[i]
print("".join(dancers))
