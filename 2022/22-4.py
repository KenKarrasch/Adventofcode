f = open('22-4.txt').read().split('\n')
# forgot to cast the incoming string to an integer, costed me several minutes.
# turns out python happily compares multiletter strings as if they were numbers. 
# The test case worked fine as they were single digits.
# one of the pitfalls of using a loose language I guess
t1 = t2  = 0
for i in f:
    p = [int(k) for k in i.replace('-',',').split(',')]
    c1 = c2 = False    
    if p[0] <= p[2]:
        if p[1] >= p[3]:
            c1 = True
    if p[2] <= p[0]:
        if p[3] >= p[1]:
            c1 = True
    if p[0] <= p[3]:
        if p[1] >= p[2]:
            c2 = True
    if p[2] <= p[1]:
        if p[3] >= p[0]:
            c2 = True
    if c1: t1 += 1
    if c2: t2 += 1
print('part 1 -',t1)
print('part 2 -',t2)
