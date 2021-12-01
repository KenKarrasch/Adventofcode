s = int(open('15-20.txt').read().split('\n')[0])

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

i,am,am2  = 0,int(s/10),int(s/11)
while True:
  if sum(factors(i)) > am:
    print('part 1 -',i)
    break
  i += 1
  if i%10000==0:
    print(i)
while True:
  ls,nls,i = factors(i),[],i+1
  for f in ls:
    if f*50 > i:
      nls.append(f)
  if sum(nls) > am2:
    print('part 2 -',i)
    break
  if i%10000==0:
    print(i)
