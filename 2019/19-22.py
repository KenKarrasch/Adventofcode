import sys
import collections
import math


# The key to this problem is it is similar to how a magician 'shuffles' a deck of
# cards (by cutting, reversing and incrementing), but the magician still knows
# exactly where card is. Magicians use the same principles used in this question.
# There is no loss in information and shuffles can be traced backwards and forwards.
#
# When I realised that we needed the card in position 2020, I realised it
# mean't that I would need to work backwards.  I was initially convinced this
# could not be done as I thought the increment function was a one way trap door.
# because it wraps around.  It dawned on me later that it is better to view it
# as an infinite array, so is e.g.   array a[0,1,2,3,4,5,6,7,8,9] inc 3'ed, becomes
# an[0,X,X,1,X,X,2,X,X,3,X,X,4,X,X,5,X,X,6,X,X,7,X,X,8,X,X,9] where is X is
# 'don't care' so the new position of card 6 is at position 6*3 = 18 mod 10 = 8
#
# Note that since the deck length and all of the increment lengths are prime numbers
# there is no loss in information, the question also hinted this.  I used Wolfram Alpha
# to confirm the it is prime.  (Other websites didn't cut it, and I couldn't figure
# out a quick algorithm to work with such large numbers)
#
# The first step is to convert the rules into one single polynomial function. 
#
# The Polynomial has two components, the multiply factor, a, from the increment
# and the linear offset factor, b, from the reverse and cutting.
# The position of the card is translated to p(new) = a*p+b
#
# A polynomial can be made for the reverse direction also. Cutting and Stacking is
# fairly straightforward. Increment was a challenge.
#
# I was baffled as to how to actually invert the increment function, especially
# for large numbers, it turns out Python has an inbuilt power function that allows
# the modulus to be specified.  The inv power/modulus uses Fermat's little theorem
# which quickly reduces.
#
# Now we need to apply the polynomial 100 trillion times.
# (I should reference 'Jonathan Paulson' for this approach)
#
# So after 3 shuffles the position of a card becomes:
# p' = ap+b
# p'' = ap'+b = a(ap+b)+b = a(a.a.p+a.b+b)
# p''' = a(a(ap+b)+b)+b = a(a.a.p+a.b+b)+b = a.a.a.p+a.a.b+a.ab+a.b+b
# and so on 100 trillion times
#
# p(n times) = (a^n).p+(a^n-1).b+(a^n-2).b+.........b
#
# Which is a summation
#
# Wolfram alpha has a tool for converting summations into a single formula
#
# type: "\ sum b*a^i   for i=0 to i=n" into Wolfram Alpha
#
# The summation tallies to:
#
# (b.a^(n+1)/a-1) - (b/(a-1))
#
# calculates as (s2020*modpow(ai,sh,l) + (modpow(ai,sh,l)-1)*bi*modinv(ai-1,l))%l)


r = open('19-22.txt').read().split('\n')

d = []
for a in r:
  if 'inc' in a:
    d.append([0,int(a.split('ment')[1])])
  if 'cut' in a:
    d.append([1,int(a.split('cut')[1])])
  if 'stack' in a:    
    d.append([2,-1])
    
def modinv(a, m):
    return modpow(a,m-2,m)
def modpow(b,e,m):
    if e==0:
        return 1
    elif e%2==0:
        return modpow((b*b)%m, e/2, m)
    else:
        return (b*modpow(b,e-1,m))%m

def geteqpolynomial(d,l):
  a,b = 1,0
  #p' = a*p+b
  for z in d:    
    if z[0] == 0:#if 'deal with increment' in a:        
        inc = z[1]        
        a,b = a*inc,b*inc
    if z[0] == 2:#if 'deal into new stack' in a:        
        a,b = -a, -b-1
    if z[0] == 1:#if 'cut' in a:
        c = z[1]       
        a,b = a,b-c
    a = a%l
    b = b%l  
  return a,b

def geteqpolynomialreverse(d,l):
  a,b = 1,0
  #p' = a*p+b
  for z in d[::-1]:    
    if z[0] == 0:#if 'deal with increment' in a:        
        inc = z[1]
        ninc = modinv(inc,l)
        a,b = a*ninc,b*ninc
    if z[0] == 2:#if 'deal into new stack' in a:        
        a,b = -a, -b-1
    if z[0] == 1:#if 'cut' in a:
        c = z[1]       
        a,b = a,b+c
    a = a%l
    b = b%l  
  return a,b

s2020,l = 2020,10007
a,b = geteqpolynomial(d,l)
print('part 1 -',(a*2019+b)%10007)

sh,l = 101741582076661,119315717514047
ai,bi = geteqpolynomialreverse(d,l)
print('part 2 -',(s2020*modpow(ai,sh,l) + (modpow(ai,sh,l)-1)*bi*modinv(ai-1,l))%l)
