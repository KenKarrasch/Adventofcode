import copy
f = open('22-21.txt').read().split('\n')

# Part 1 - Straightforward, Works like an electrical circuit

# Part 2 - 

# Start from HUMN = 1, have a look at the delta between root equality components
# if the it is above 0, keep going up by factor of 10, when it is below zeroadd 100 trillion. keep adding 100 trillion until it goes below 0
# go back one iteration, then narrow the scan, add 10 trillion.
# keep going until is zooms in on the exact number.

m = []
mn = []
w = []
mr = {}
mn = {}

for ob in range(len(f)):
    i = f[ob].split()    
    w.append(i[1:])    
    mr[i[0].replace(':','')] = ob   
    mn[i[0].replace(':','')] = False
    m.append(i[0].replace(':',''))
   
dep = []

for i in range(len(w)):
    if len(w[i]) == 1:
        mn[m[i]] = int(w[i][0])

mns = {}
for key, value in mn.items():
  mns[key] = value

def calc(wi):         
      if wi[1] == '+':
        return mn[wi[0]] + mn[wi[2]]
      if wi[1] == '-':
        return mn[wi[0]] - mn[wi[2]]
      if wi[1] == '*':
        return mn[wi[0]] * mn[wi[2]]
      if wi[1] == '/':
        return mn[wi[0]] // mn[wi[2]]

def root(wi):    
    delta[0] = mn[wi[2]] - mn[wi[0]]
    if mn[wi[0]] == mn[wi[2]]:        
        return True
    else:         
        return False

sv = []
for i in range(len(w)):
    sv.append(mn[m[i]])    

done = False
while not done:
    for i in range(len(w)):      
       if len(w[i]) == 3:
        if (mn[w[i][0]] != False) and (mn[w[i][2]] != False):
           mn[m[i]] = calc(w[i]) 
   
    done = True
    for i in range(len(w)):
        if mn[m[i]] == 0:
            done = False

print('part 1 -',mn['root'])



delta = [0]
st = 1
#adder = 100 000 000 000
adder = 100000000000
comp = False

while not comp:  
  pr = st
  st += adder
  fa = st
  mn['humn'] = fa
  done = False
  #print()
  while not done:
    for i in range(len(w)):      
       if len(w[i]) == 3:
        if (mn[w[i][0]] != False) and (mn[w[i][2]] != False):
          if m[i] != 'root':            
            mn[m[i]] = calc(w[i])                      
          else:
            if root(w[i]):
                #print('pass',mn['humn'])                
                print('part 2 -',st)
                comp = True
                
            else:
                #print(mn['humn'], 'fail')   
                #print(delta[0])
                if delta[0] > 0:
                    st = pr
                    adder = adder//10

            done = True            
  for i in range(len(w)):
    mn[m[i]] = sv[i]


# 3558714869438 too high
# 3558714869436 correct
# 3558714869439 too high
