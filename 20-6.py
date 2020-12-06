s = open('20-6.txt').read().split('\n\n')

# nice 20m puzzle (10m each part)
# I forgot to reset the counter between parts, it cost me a minute or two.
# I have probably done it the hardest and slowest possible way, n squared, I'm betting the puzzle
# could be done in one line of Python code. 

def gord(char):
    return ord(char) - ord('a') 

bl = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bn = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

c = 0
for g in s:
    st, a = g.split(), bl[:]
    for f in st:
        for ch in f:
            if(a[gord(ch)] == 0):
                a[gord(ch)] = 1
    c += sum(a)        

print('part 1 -',c)

c = 0
for g in s:
    st, a = g.split(), bn[:]
    for f in st:
       l = bl[:] 
       for ch in f:
            if(a[gord(ch)] == 1):
                l[gord(ch)] = 1
       for g in range(len(l)):
           if l[g] != 1:
               a[g] = 0
    c += sum(a)        

print('part 2 -',c)
