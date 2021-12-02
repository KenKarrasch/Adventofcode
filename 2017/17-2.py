f = [[int(i) for i in fid.split()] for fid in open('17-2.txt').read().split('\n')]
t1,t2 = 0,0
for fb in f:    
    t1 += max(fb)-min(fb)
    for j in fb:
        for i in fb:
            if ((i%j == 0) and (i != j)):               
                t2 += i/j                    
print('part 1 -',t1,'part 2 -',t2)
