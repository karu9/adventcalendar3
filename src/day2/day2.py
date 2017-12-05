lines = open('input.txt').readlines()
sumPart1 = 0
sumPart2 = 0
for i in range(0, len(lines)) :
    listValues = list(map(lambda x : int(x), lines[i][:-1].split("\t")));
    sumPart1 += max(listValues) - min(listValues);
    for i in listValues:
        listDivide = list(filter(lambda x : x != i and max(i, x) % min(i, x) == 0, listValues))
        if(len(listDivide) == 1):
            sumPart2 += int(max(listDivide[0], i) / min(listDivide[0], i));
            break
print(sumPart1)
print(sumPart2)
