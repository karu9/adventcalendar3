## part 1 ##
inp = open('input.txt').readlines()[0]
filtered_inp = ''
## remove escapes ##
i = 0
while i < len(inp):
    if inp[i] == '!':
        i += 2
    else :
        filtered_inp += inp[i]
        i += 1
## remove garbage ##
filtered_inp2 = ''
in_garbage = False
i = 0
garbage_count = 0
while i < len(filtered_inp):
    char = filtered_inp[i]
    if not in_garbage :
        if char == '<':
            in_garbage = True
        if char in '{}':
            filtered_inp2 += char
    elif in_garbage :
        if char == '>' :
            in_garbage = False
        else :
            garbage_count += 1 
    i += 1
## count groups ##
count = 0
value = 0
for char in filtered_inp2:
    if char == '}':
        count += value
        value -= 1
    else:
        value += 1
print(count)
print(garbage_count)
