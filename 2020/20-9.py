s = open('20-9.txt').read().split()

n,lb,r,fd = [int(i) for i in s],25,0,False
p = lb
while (p < len(s)) and not fd:
    i, fd = 0, True    
    for i in range(lb):
      for j in range(lb):
            if n[p-i-1] + n[p-j-1] == n[p]:
                fd = False    
    p += 1
    if fd:
        print('part 1 -',n[p-1])
for i in range(p-1):
    skip = False
    for j in range(p-1-i):
      if not skip:
       if(sum(n[i:i+j]) == n[p-1]):
           print('part 2 -',min(n[i:i+j]) + max(n[i:i+j]))
       if(sum(n[i:i+j]) > n[p-1]):
           skip = True    
