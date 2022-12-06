f = open('22-6.txt').read()
# nice easy one
p = [(1,4),(2,14)]
for l,pt in p:
  for i in range(len(f)-pt):
    gd = True
    st = f[i:i+pt]
    for j in range(pt):
      if st.count(f[i+j]) > 1:
         gd = False
    if gd:
        print 'part',l,'-',i+pt
        break
