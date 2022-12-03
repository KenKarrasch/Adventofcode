f = open('22-3.txt').read().split('\n')
# fun puzzle after work
qwerty = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
t = 0
for i in f:
  m = len(i)/2
  for ch in qwerty:
    if ch in i[0:m]:
      if ch in i[m::]:
        if ch < 'a':
          t += 26+1+ord(ch) - ord('A')
        else:
          t += 1+ord(ch) - ord('a')
print 'part 1 -', t
t = 0
for i in range(len(f)/3):
  for ch in qwerty:
    if ch in f[3*i]:
      if ch in f[3*i+1]:
        if ch in f[3*i+2]:
          if ch < 'a':
            t += 26+1+ord(ch) - ord('A')
          else:
            t += 1+ord(ch) - ord('a')
print 'part 2 -',t
