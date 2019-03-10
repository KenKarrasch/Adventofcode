def thr(s):
  for i in range(len(s)-2):
    if ord(s[i]) == ord(s[i+1])-1:
      if ord(s[i]) == ord(s[i+2])-2:
       return True
  return False

def twpr(s):
  lp = -2
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      if lp != i-1:
        if lp != -2:
          return True
        lp = i
  return False
  
def iol(s):
   if 'i' in s: return True
   if 'o' in s: return True
   if 'l' in s: return True
   return False

def adv(s):
   w = len(s)
   out = []
   carry = True
   for c in range(w):
     o = ord(s[w-c-1])
     if carry:
       l = o+1
     else:
       l = o
     if l > ord('z'):
         carry = True
         out.append('a')
     else:
         carry = False
         out.append(chr(l))
   return out[::-1]

f = open('15-11.txt').read()
ns = [i for i in f]
for j in [1,2]:
 while True:
  ns = adv(ns)
  s = ns[:]
  if thr(s) and twpr(s) and not iol(s):
   print 'part',j,'-',s
   break
