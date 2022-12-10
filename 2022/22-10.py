f = open('22-10.txt').read().split('\n')
#  fun solve the code. Reminds me of the crt drawing circuit from the pong game from the sixties
# https://www.falstad.com/pong/index.html
x = 1
gr = [['.'] * 40 for x in range(6)]

cs = [20,60,100,140,180,220]
inst = 0
cycl = [1]
cy = 0

def pr():    
  for i in gr:
    st = ''
    for j in i: st += j
    print(st)


while cy < 240:
    c = f[inst].split()
    if(len(c) > 1):                             
        cycl.append(x)        
        cycl.append(x)    
        x += int(c[1])                    
        cy += 1      
    else: 
        cycl.append(x)            
    inst += 1        
    if inst >= len(f):
        inst = 0
    cy += 1
s = 0
for i in range(len(cycl)):
    if i in cs:
        s += i * cycl[i]

print('part 1 -', s)
for i in range(len(cycl)-1):
    l,p = divmod(i,40)
    if  (cycl[i+1] == p-1) or (cycl[i+1] == p) or (cycl[i+1] == p+1):            
        gr[l][p] = '#'
print('part 2 -')
pr()
