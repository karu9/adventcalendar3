instructs = [x[:-1].split(' ') for x in open('input.txt').readlines()]
## [index, lastplayedsound, lastrecoveredsound] ##
values = [0, 0, 0]
registers = {}
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def initreg(reg):
    if reg not in registers:
        registers[reg] = 0
def getintval(val):
    intval = 0
    if not is_int(val):
        intval = registers[val]
    else:
        intval = int(val)
    return intval
def set (reg, val):
    registers[reg] = getintval(val)
    values[0] += 1
def mul (reg, val):
    registers[reg] *= getintval(val)
    values[0] += 1
def jgz(reg, val):
    if registers[reg] > 0:
        values[0] += getintval(val)
    else :    
        values[0] += 1
def add(reg, val):
    registers[reg] += getintval(val)
    values[0] += 1
def mod(reg, val):
    registers[reg] %= getintval(val)
    values[0] += 1
def snd(reg):
    values[1] = registers[reg]
    values[0] += 1
def rcv(reg):
    if(registers[reg] > 0):
        values[2] = values[1]
        print(values)
    values[0] += 1
while values[0] < len(instructs) :
    instruct = instructs[values[0]]
    initreg(instruct[1])
    exec(instruct[0] + '("' + instruct[1] + '","' + instruct[2] + '")' if len(instruct) == 3 else instruct[0] + '("' + instruct[1] + '")')
print(values)
