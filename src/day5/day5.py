## part 1 ##
lines = list(map (lambda x : int(x[:-1]), open('input.txt').readlines()))
index = 0
steps = 0
while index < len(lines):
    leap = lines[index]
    lines[index] += 1
    index += leap
    steps += 1
print(steps)
## part 2 ##
lines = list(map (lambda x : int(x[:-1]), open('input.txt').readlines()))
index = 0
steps = 0
while index < len(lines):
    leap = lines[index]
    if leap < 3 :
        lines[index] += 1
    else:
        lines[index] -= 1
    index += leap
    steps += 1
print(steps)
