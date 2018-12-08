s = map(int, open('18-8.txt').read().split())
i = 0

def getnext():
  global i
  global s
  i += 1  
  return s[i-1]

def readtree():
  numberofchilden = getnext()
  numberofmeta = getnext()   
  children = []  
  metadata = []
  for i in range(numberofchilden):
    children.append(readtree())
  for i in range(numberofmeta):
    metadata.append(getnext())
  return(children, metadata)

def summetadata(root):
  children = root[0]
  metadata = root[1]
  total = 0
  for i in children:
    total += summetadata(i)
  for m in metadata:
    total += m
  return total

def sumspecial(branch):
  children = branch[0]
  metadata = branch[1]
  specialtotal = 0
  if len(children) == 0:
   for m in metadata:
    specialtotal += m
  else:
    for m in range(len(metadata)):      
      if metadata[m] < len(children)+1:
        specialtotal += sumspecial(children[metadata[m]-1])        
  return specialtotal

print s
root = readtree()
print summetadata(root)
print sumspecial(root)

