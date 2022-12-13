import copy
f = open('22-13.txt').read().split('\n\n')
# Part 1
# The input is clearly identical to Pythons list data structure.  Wrote code to convert from string to the list data. I am 
# pretty sure there is an inbuilt Python function to convert, I did it the hard way.
#
# I incorrectly assumed inputs where in the range 0 to 9 (as kind of hinted in the sample data), it is actually 0 to 10, used a kludge to
# handle 10 in the input, i.e. convert 10 to 'a', then convert 'a' back to 10 in th list data, I couldn't be bothered to write a proper parser.
#
# Took a bit of if-then-elses to distinguish between trees, branches and leaves, but got there in the end. Used to 'type' function to distinguish
# between branches (lists) and leafs (integers)

# Part 2
# At first glance a sorting algorithm seemed required, The structure of the data input was clearly hinting at using a Merge sort.
# It's been three decades since I have implemented a merge sort, and looked impossible to code that in a night.
# In my estimation a bubble sort looked like it would take forever to execute (but probably not, in hindsight). 

# Then it dawned on me that no sorting was required at all.  I just need to simply find out how many inputs are higher than [[2]],
# and how many are higher than [[6]].  The indices and answer can be worked out from there.  So complexity went from n^2, to nlogn, to just n.

n = '1234567890a'
def getmeb(st):
   fb = bb = 0
   for i in range(len(st)):
     if st[i] == '[':
        fb += 1
     if st[i] == ']':
        if bb == fb:
          return i
        bb += 1
     
def getl(st):
    ls = []
    r = 0
    while r < len(st):
      if st[r] == '[':
        eb = getmeb(st[r+1::])
        l = getl(st[r+1:r+eb+1])
        ls.append(l)
        r += eb+1
      if st[r] in n:
        if st[r] == 'a':
            nn = 10
        else: 
            nn = int(st[r])
        ls.append(nn)
      r += 1
    return ls

def cms(ob1,ob2):
    lt = type([1,2])    
    if (type(ob1) != lt) and (type(ob2) != lt):
        if ob1 < ob2:
            return -1
        elif ob1 == ob2:    
            return 0
        else: return 1
    elif (type(ob1) == lt) and (type(ob2) == lt):
        p = 0
        while p < len(ob1) and p < len(ob2):
            d = cms(ob1[p],ob2[p])
            if d == -1:
               return -1
            if d == 1:
               return 1
            p += 1
        if p == len(ob1) and p < len(ob2):
            return -1
        elif p == len(ob2) and p < len(ob1):
            return 1
        else:
            return 0
    elif (type(ob1) != lt) and (type(ob2) == lt):
        return cms([ob1],ob2)    
    else:
        return cms(ob1,[ob2]) 

def cmp(s1,s2):
    s1 = s1.replace('10','a')
    s2 = s2.replace('10','a')
    s1t = getl(s1)[0]
    s2t = getl(s2)[0]    
    return cms(s1t,s2t)
tl = 0
for ps in range(len(f)):
  p = f[ps].split()   
  if cmp(p[0],p[1]) < 0:    
    tl += ps+1

print('part 1 -',tl)
nf = []
for ps in range(len(f)):  
  p = f[ps].split()  
  nf.append(copy.deepcopy(p[0]))
  nf.append(copy.deepcopy(p[1]))
ct2,ct6 = 1,2
for i in nf:
    if cmp(i,'[[2]]') < 0:
        ct2 += 1
for i in nf:
    if cmp(i,'[[6]]') < 0:
        ct6 += 1
print('part 2 -',ct2*ct6)
