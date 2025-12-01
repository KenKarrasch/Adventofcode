f = open('day1in.txt').read().split('\n')
d = 50
ct = 0
for i in f:
    if i[0] == 'R':
        for j in range(int(i[1:])):
            d += 1
            if d%100 == 0:
                ct += 1
    if i[0] == 'L':
        for j in range(int(i[1:])):
            d -= 1
            if d%100 == 0:
                ct += 1
print(ct)
