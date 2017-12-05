lines = open('input.txt').readlines()
valid1 = 0
valid2 = 0
def validate(words):
    for i in range(len(words)):
     for j in range(i + 1, len(words)):
         if words[i] == words[j]:
             return False
    return True
def validate2(words):
    for i in range(len(words)):
     for j in range(i + 1, len(words)):
         wordi = sorted(list(map(lambda x : x, words[i])))
         wordj = sorted(list(map(lambda x : x, words[j])))
         if wordi == wordj:
             return False
    return True
    
for line in lines:
    words = line[:-1].split(' ')
    if validate(words):
        valid1+= 1
    if validate2(words):
        valid2+= 1
print(valid1)
print(valid2)
