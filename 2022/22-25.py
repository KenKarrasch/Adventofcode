f = open('22-25.txt').read().split('\n')

# Part 1 - 1071st, Part 2 - 902nd, 25min solve, It's been a while since I got in top 1000, there's alot more competition now I guess.
#  
# 400 stars now complete (all years done)
#
# trial and error solution, continually refining to narrow down to the answer
#

def snafu(i):
    n = []
    for ch in i:
        n.append(ch)
    v = 1
    num = 0    
    for ns in n[::-1]:
        dn = False
        if ns == '=':
            num -= 2*v
            dn = True
        if ns == '-':
            num -= v
            dn = True
        if not dn:
            num += int(ns)*v
        v *= 5
    return num

# tally up numbers
t = 0
for i in f:
    t += snafu(i)

# work out what number to start from, start from 1, keep adding '='s until is above target, then go back one

st = ['1']
dn = False
while t > snafu(st):            
    pst = st[:]
    st.append('=')

# See if 2 is better start point, if is still lower than target, thenstart from '2======='
st = pst[:]
st[0] = '2'
if t < snafu(st):
    st[0] = '1'
lt = ['=','-','0','1','2']

ref = 1
dn = False
while not dn:      
    nx = False
    for d in range(len(lt)):   # work through each of the letters until it goes over the target, then step back one
      if not nx:     
        st[ref] = lt[d]
        if snafu(st) > t:           
           st[ref] = lt[d-1]
           ref += 1
           nx = True
    if not nx:               
           st[ref] = '2'
           ref += 1
           nx = True
    if snafu(st) == t:
        dn = True        
ans = ''
for lt in st:
    ans += lt
print('part 1 -',ans)
