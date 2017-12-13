elements = [x for x in range(256)]
lenghts = list(map(lambda x : ord(x), open('input.txt').readlines()[0])) + [17, 31, 73, 47, 23]
index = 0
skip_size = 0
for h in range(64):
    for inp in lenghts:
        reversedList = (elements + elements)[index:index + int(inp)][::-1]
        for i in range(len(reversedList)):
            elements[(index + i) % len(elements)] = reversedList[i]
        index = (index + int(inp) + skip_size) % len(elements)
        skip_size += 1
denseHash = []
for i in range(16) :
    xor = elements[16*i]
    for element in elements[16*i + 1 : 16*i + 16]:
        xor ^= element
    denseHash.append(('0' +hex(xor)[2:])[-2:])
print(''.join(denseHash))


