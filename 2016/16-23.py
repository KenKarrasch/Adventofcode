i = [x.split() for x in open('16-23.txt').read().split('\n')]
a = int(i[19][1])*int(i[20][1])
print('part 1 -',a+5040)
print('part 2 -',a+479001600)
