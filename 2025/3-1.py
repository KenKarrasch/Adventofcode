f = [[int(y) for y in x] for x in open('day2in.txt').read().split('\n')]

tly = 0
for i in f:
    bn = 0
    for j in range(len(i)):
        for h in range(j,len(i)):
            if j != h:
                cb = i[j]*10 + i[h]
                if cb > bn:
                    bn = cb
    tly += bn
print(tly)



# 3   6337   3691  ****
