f = open('16-2.txt').read().split('\n')
cd = ''
dr = [[1,2,3,1,2,3,4,5,6], \
     [2,3,3,5,6,6,8,9,9], \
      [4,5,6,7,8,9,7,8,9],
      [1,1,2,4,4,5,7,7,8]]
dd = [['1','2','1','4','5','2','3','4','9','6','7','8','B'], \
      ['1','3','4','4','6','7','8','9','9','B','C','C','D'], \
      ['3','6','7','8','5','A','B','C','9','A','D','C','D'], \
      ['1','2','2','3','5','5','6','7','8','A','A','B','D']]     
b = ['1','2','3','4','5','6','7','8','9','A','B','C','D']
ky = {'U':0,'R':1,'D':2,'L':3}

for i in f:
    lt = 5
    for ch in i:
        lt = dr[ky[ch]][lt-1]
    cd += str(lt)
print('part 1 -',cd)
cd = ''

def getch(lt):    
    for i in range(len(b)):
        if b[i] == lt:
            return i   

for i in f:
    lt = '5'
    for ch in i:
        lt = dd[ky[ch]][getch(lt)]
    cd += str(lt)
print('part 2 -',cd)