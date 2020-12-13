
s = open('20-13.txt').read().split('\n')
bs = s[1].split(',')

# Thought this would be impossible.
# Gave up trying to work out Chinese Remainder Theorem, and Fermat Little Theorem

# After 3 hrs of working the puzzle I got a phonecall from an old workmate
# who had some ground breaking ideas.  Basically begin by working out a pair
# of buses.  Then gradually add busses to get an answer. 

# First consider a simple case two buses say 5,7.  Then work out the
# when they line up.  Conditions are right after 20 mins, and
# then again at 55, 90, 125, 160, 195, 230, 265, 300 mins.
# So basically they line up at t = 20 + 35x, where x is any number.

# The [5,7] pair of buses is equivalent to one bus at
# the 20min mark every 35 mins.

# In other words 5,7 is equivalent 
# to x,x,x,x,x, x,x,x,x,x, x,x,x,x,x, x,x,x,x,35

# Then add another number say 13, the problem becomes 5,7,13
# or x,x,13,x,x, x,x,x,x,x, x,x,x,x,x, x,x,x,x,35

# Then do the [13, 35] pair of busses. bus '13' arriving at t+3 mins
# and bus '35' arriving at t+20mins

# This is equivalent to 1 bus at the 440min mark every 455mins after that.

bsn = []
for i in range(len(bs)):
    if bs[i] != 'x':
        bsn.append(int(bs[i]))
t = int(s[0])
l = []
for i in range(len(bsn)):
    l.append(bsn[i]-t%bsn[i])
for i in range(len(l)):
    if l[i] == min(l):
        print('part 1 -',bsn[i]*min(l))

bsn = []
for i in range(len(bs)):
    if bs[i] != 'x':
        bsn.append(int(bs[i]))
    else: bsn.append(-1)
    
def getecl(b1,b2,st,diff):
    t = st
    while True:
        t += b1       
        if (t+diff)%b2 == 0: 
            return t

adv = bsn[0]
st = 0
for i in range(len(bsn)-1):
    if bsn[i+1] != -1:
        st = getecl(adv,bsn[i+1],st,i+1)
        adv *= bsn[i+1]
print('part 2 -',st)
