f = open('day1in.txt').read().split('\n')
d = 50
ct = 0
for i in f:
    if i[0] == 'R':
        d += int(i[1:])
    if i[0] == 'L':
        d -= int(i[1:])
    if d%100 == 0:
        ct += 1
print(ct)
