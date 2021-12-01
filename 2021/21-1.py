r = [int(i) for i in open('21-1.txt').read().split()]
ct = p = 0

for i in r:
    if i > p: ct += 1
    p = i
print 'part 1 -',ct-1
ct = p = 0
for i in range(len(r)-2):
    i = sum(r[i:i+3])
    if i > p: ct += 1
    p = i
print 'part 2 -',ct
