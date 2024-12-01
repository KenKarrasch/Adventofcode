g = open('24-1.txt').read().split('\n')

# started late, 4 minute solve, but nowhere near fast enough to get onto the leaderboard

print(g)

l1 = []
l2 = []

for i in g:
    g = i.split()
    l1.append(int(g[0]))
    l2.append(int(g[1]))

print(l1,l2)

l1.sort()
l2.sort()

print(l1,l2)
d = 0

for i in range(len(l1)):
    d += abs(l1[i])

print('part 1 -', d)

d = 0

for i in range(len(l1)):
    ct = 0
    for j in range(len(l2)):
        if(l1[i] == l2[j]):
            ct += 1
    d += l1[i] * ct

print('part 2 -', d)
