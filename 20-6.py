s = open('20-6.txt').read().split('\n\n')

# nice 10m puzzle, couldn't start on time due to sporting commitments
# I forgot to reset my c counter, it cost me a minute or two.
# I have probably done it the hardest posible way, I'm betting the puzzle
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
