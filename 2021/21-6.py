rd = [int(i) for i in open('21-6.txt').read().split(',')]

# Part 1 straightforward, part 2, I used a 'divide and conquer' approach, solved for 128 depth for each case 0 to 8, store in dictionary.
# Then solve each element in the input list, then tallied up. It could run much quicker than what I have here.

f = rd[:]
for j in range(80):
  for i,fs in enumerate(f):
    f[i] -= 1
    if f[i] == -1:
        f[i] = 6
        f.append(9)
print 'part 1 -',len(f)
ds,d256 = {},{}
for t in [0,1,2,3,4,5,6,7,8]:
 f = [t]
 for j in range(128):
  for i,fs in enumerate(f):
    f[i] -= 1
    if f[i] == -1:
        f[i] = 6
        f.append(9)
 ds[t] = len(f)
tly = 0
for t in rd:
 f = [t]
 for j in range(128):
  for i,fs in enumerate(f):
    f[i] -= 1
    if f[i] == -1:
        f[i] = 6
        f.append(9)
 am = 0
 if t not in d256:
   for k in f: am += ds[k]
   d256[t] = am
 tly += d256[t]
 print(t,len(f))
print 'part 2 -',tly
