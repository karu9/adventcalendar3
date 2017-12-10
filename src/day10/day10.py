## part 1 ##
elements = [x for x in range(256)]
index = 0
skip_size = 0
for inp in open('input.txt').readlines()[0].split(','):
    reversedList = (elements + elements)[index:index + int(inp)][::-1]
    for i in range(len(reversedList)):
        elements[(index + i) % len(elements)] = reversedList[i]
    index = (index + int(inp) + skip_size) % len(elements)
    skip_size += 1
print(elements[0] * elements[1])
