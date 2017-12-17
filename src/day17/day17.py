step = 367
x = 1
positions = [0]
pos = 0
## part1 ##
while x <= 2017:
    pos = ((pos + step) % x)+1
    positions.insert(pos, x)
    x += 1
print(positions[positions.index(2017) +1])
## part2 ##
pos = 0
res = 0
x = 1
while x <= 50000000:
    pos = ((pos + step) % x)+1
    if pos == 1 :
        res = x
    x += 1
print(res)
