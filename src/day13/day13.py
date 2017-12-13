firewalls = list(map(lambda x: [int(x[:x.index(':')]), int(x[x.index(':')+2: -1])], open('input.txt').readlines()))
print(sum(list(map(lambda x : x[0] * x[1], list(filter(lambda x : x[0] % (2 * (x[1]-1)) == 0, firewalls))))))
i = 1
while len(list(filter(lambda x : (x[0] + i) % (2 * (x[1]-1)) == 0, firewalls))) != 0 :
    i += 1
print(i)
