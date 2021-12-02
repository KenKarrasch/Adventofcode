
w = open('19-16.txt').read()

# part 1 was fairly straightforward
# 
# part 2 - I noticed the offset was 
# at the end of the sequence.
# then it took a while to recognise
# that towards the end of the sequence
# the multiply factor is always one 1,
# and the leading zeros are in a 
# triangular shape. (the zeros finish 
# at the line number)

# So the solution is get the last 
# data chunk starting at the 7 digit 
# number, (570,000 in my case)
# then tallying it, then subtract 
# each element one at a time and 
# adding to the output. the ouput is 
# then the input to the next iteration
# 
# It's a quick calculation from there.
# 
# Doing the part 2 calculation using 
# part 1 method would take about 94 
# years.

# The solution assumes the 7 digit 
# number is towards the end of the 
# sequence. 

# Technically not a general solution 
# but should work for all cases in aoc
#
# FFT reminds me of the actual FFT 
# (fast fourier transform) algorithm
# for converting from time domain to 
# frequency domain

r = [y for y in w]
d = r
fft = [0,1,0,-1]
tly = []
p = 0
for j in range(100):
 if j % 10 == 0: print j,'%'
 for a in range(len(r)):
  nfft = []
  for n in range(int(len(d)/((a+1)*len(fft)))+1):
    for h in range(len(fft)):
     for g in range(a+1):
      nfft.append(fft[h])
  nfft.pop(0)
  amt = 0
  p = 0
  for b in range(len(r)):
    amt += int(d[b])*nfft[p]
    p += 1
    p = p%len(nfft)
  tly.append(abs(amt)%10)
 d = tly[:]
 tly = []
print 'part 1 -',d[:8]


f = [int(r) for r in w]
d = f

sig = -(int(w[:7]) - len(d)*10000)
stch = sig % len(d)
nc = sig // len(d)
d = d[-stch:]
for a in range(nc):
  for g in f:
    d.append(g)
for j in range(100):
 if j % 10 == 0: print j,'%'
 t = sum(d)
 nd = [t%10]
 for a in range(len(d)):
    t -= d[a]
    nd.append(t%10)
 d = nd[:]
print 'part 2 -',d[:8]
