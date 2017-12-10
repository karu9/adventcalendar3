## part 1 ##
elements = [x for x in range(5)]
index = 0
skip_size = 0
for inp in [3,4,1,5]:
    reversedList = (elements + elements)[index:index + int(inp)][::-1]
    for i in range(len(reversedList)):
        elements[(index + i) % len(elements)] = reversedList[i]
    index = (index + int(inp) + skip_size) % len(elements)
    print(index)
    skip_size += 1
print(elements[0] * elements[1])
