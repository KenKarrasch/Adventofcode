f = open('20-18.txt').read().split('\n')
# calculator
def calc(s):
    n, num, op= 0,True,'+'
    ch = s.split(' ')
    for h in ch:
      if num:
        if op == '+': n += int(h)
        if op == '-': n -= int(h)
        if op == '*': n *= int(h)
        num = False
      else:
        num = True
        op = h
    return n
    
def calca(s,p):
    if p == 1:
        return(calc(s))
    h = s.split()
    while '+' in h:
       dn = False
       for j in range(len(h)):
         if not dn:
          if h[j] == '+':
              mt = h[j-1]+' + '+h[j+1]
              n,dn = calc(mt),True
              h = h[0:j-1] + [str(n)] + h[j+2:]
              dn = True
    sto = h[0]
    for i in range(1,len(h)):
         sto = sto + ' ' + h[i]
    return calc(sto)

def sbr(sin,p):
    s = sin
    while '(' in s:
        st,i,fr = -1,0,False
        for i in range(len(s)):
          if not fr:
            if '(' in s[i]: st = i
            if ')' in s[i]:
             if st != -1:
                n = calca(s[st+1:i],p)
                s = s[0:st] + str(n) + s[i+1:len(s)]
                fr = True
    return(calca(s,p))
    
t1,t2 = 0,0
for l in f:
   t1 += sbr(l,1)
   t2 += sbr(l,2)
print 'part 1 -',t1
print 'part 2 -',t2
