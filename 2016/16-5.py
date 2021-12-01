import hashlib
id = open('16-5.txt').read()
fd,n = False,0
st,chs = '',0
pwd,pwd2 = '',['','','','','','','','']
while not fd:
    if hashlib.md5(id+str(n)).hexdigest()[0:5] == '00000':
        st = hashlib.md5(id+str(n)).hexdigest()
        chs += 1
        if chs < 9:
            pwd += st[5]
        print 'pwd',pwd,st[5]
        if st[5] in ['0','1','2','3','4','5','6','7']:
          if pwd2[int(st[5])] == '':
            pwd2[int(st[5])] = st[6]
            print pwd2
            if '' not in pwd2:
                fd = True
    n += 1
p2 = ''
print 'part 1 -',pwd
print 'part 2 -',p2.join(pwd2)
