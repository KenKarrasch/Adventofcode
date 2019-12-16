r = [f for f in open('19-16.txt').read()]

# Part 1 only

d = r
fft = [0,1,0,-1]
tly = []
p = 0
for j in range(100):
 print j
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
