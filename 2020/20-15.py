# Store the results in a dictionary
# About 30sec processing on Python
z = [5,2,8,16,18,0,1]
d = 30000000
p,l,i = {},z[-1],len(z) - 1
for x in range(len(z[0:-1])):
    p[z[x]] = x
while i < d + 2:
    if l in p.keys():      
       n = i-p[l]
       p[l] = i
       l = n
    else:
       p[l] = i
       l = 0
    i += 1
    if i == 2020-1: print('part 1 -',l)        
    if i == d-1: print('part 2 -',l)
    if i%1000000 == 0: print("progress",i, 'out of 30,000,000')
