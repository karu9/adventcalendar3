inp = open('input.txt').readlines()[0]
length = len(inp)
halfLen = length/2
sumPart1 = 0
sumPart2 = 0
for i in range(0,  len(inp)) :
    if inp[i-1] == inp[i]:
        sumPart1 += int(inp[i])
    if inp[i] == inp[int((i + halfLen) % length)]:
        sumPart2 += int(inp[i])
print(sumPart1)
print(sumPart2)
