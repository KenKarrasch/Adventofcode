from z3 import *

# The weapon of choice among the pro's on the leaderboard appears to be the Z3 zolver to work out the 
# simultaneous equations, so I thought I should have a go at using it.  The other option of course is 
# to do them by hand.
#
# Looks like 4 hails stones are required to get an answer, I guess the other 296 were for dramatic effect
#   
# Z3 instructions are online - https://ericpony.github.io/z3py-tutorial/guide-examples.htm
#
# Feed the equation into the solver (or any variation of it):
#
#  rock position - hail position == time * (hail velocity - rock velocity)
#

f = open('23-24.txt').read().split('\n')

hail = []
for i in f:
    pi,vi = i.split(' @ ')
    p = [int(y) for y in pi.split(',')]
    v = [int(y) for y in vi.split(',')]
    hail.append([p,v])

r = [Int('rx'), Int('ry'), Int('rz')]
rv = [Int('rvx'), Int('rvy'), Int('rvz')]
s = Solver()
tm = [] # time variables to add to the Z3 solver
for i in range(len(hail)): tm.append(Int("timeofimpact" + str(i)))

for ob in range(len(hail))[0:4]:   # put all the simultaneous equations onto the solver
  for d in [0,1,2]:  # x, y, and z dimensions
   #   rock position - hail position == time * (hail velocity - rock velocity)
   s.add(r[d] - hail[ob][0][d] ==  tm[ob] * (hail[ob][1][d] - rv[d]))

res = s.check()
model = s.model()
print('rock starting point:',model.eval(r[0]),model.eval(r[1]),model.eval(r[2]))
print('rock velocity:',model.eval(rv[0]),model.eval(rv[1]),model.eval(rv[2]))
print('part 2',model.eval(r[0]+r[1]+r[2]))
