## part 1 ##
import math
instructions = open('input.txt').readlines()[0].split(',')
x = 0
y = 0
maximum = 0
for instruction in instructions :
    if instruction == 'n':
        y += 1
    elif instruction == 's':
        y -= 1
    elif instruction == 'nw':
        x -= 1
        y += 0.5
    elif instruction == 'ne':
        x += 1
        y += 0.5
    elif instruction == 'se':
        x += 1
        y -= 0.5
    elif instruction == 'sw':
        x -= 1
        y -= 0.5
    maximum = max(maximum, (max(abs(x), abs(y))))
print(max(abs(x), abs(y)))
print(maximum)
    
