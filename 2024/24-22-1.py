f = [int(i) for i in open('24-22.txt').read().split('\n')]

sn = 123
ns = [1,10,100,2024]
ns = f
tly = 0
for n in ns:
    sn = n
    for i in range(2000):    
        sn = ((sn * 64)^sn)%16777216
        sn = ((sn//32)^sn)%16777216
        sn = ((sn*2048)^sn)%16777216    
    tly += sn
print(tly)
