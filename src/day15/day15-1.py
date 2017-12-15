a = 116
b = 299
fa = 16807
fb = 48271
mod = 2147483647
i = 0
matching = 0
while i < 40000000:
    a = (a * fa) % mod
    b = (b * fb) % mod
    if(('0'*16+str(bin(a)[2:]))[-16:] == ('0'*16+str(bin(b)[2:]))[-16:]):
        matching += 1
    i += 1
print(matching)
