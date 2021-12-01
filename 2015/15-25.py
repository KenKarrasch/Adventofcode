import re
f = [int(x) for x in re.findall('[0-9]+',open('15-25.txt').read())]
dw = f[0]+f[1]-2
ct = ((1+dw)*dw/2)+f[1]-1
p = 20151125
for i in range(ct): 
   p = (p*252533)%33554393
print 'part 1 -',p
