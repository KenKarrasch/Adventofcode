f = [[int(x) for x in y.split(',')] for y in open('in.txt').read().split('\n')]
#  9     107   3769  **

szs = []

for r1 in f:
    for r2 in f:
        sz = abs(1+r1[0]-r2[0]) * abs(1+r1[1]-r2[1])
        szs.append(sz)
print(max(szs))
