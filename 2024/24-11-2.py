f = open('24-11.txt').read() # '5 89749 6061 43 867 1965860 0 206250'

# the trick with this one is:

# - the stone order is not important, stones don't affect any other stones

# - instead of keeping an monolithic array of stones, keep a list of stones you currently have and
#    and how many of each type of stones you have.
#   e.g.  array [ 2, 5, 12, 8, 2, 6] would instead be stored as 
#    [ [2, 3], [5,1], [12,1], [8,1], [6,1]]
#   where [2,3] means you have 3 stones with label '2'
#   do this for each blink

numbers = f.split()

def transform_numbers(numbers,bks):
    result = []
    rsd = {}    
    for num_str in numbers:
      rsd[num_str] = 1    
    for b in range(bks):
     nk = list(rsd.keys())
     orsd = rsd.copy()
     for num_str in nk:
        # Rule 1: If the number is 0, convert to 1
        ns1 = -1
        ns2 = -1
        num = orsd[num_str]  # Save a copy of the old dictionary
        rsd[num_str] -= num
        if num_str == '0':
            result.append('1')
            ns1 = '1'
        # Rule 2: If the number has an even number of digits, split in half
        elif len(num_str) % 2 == 0:
            mid = len(num_str) // 2
            ns1 = str(int(num_str[:mid]))
            ns2 = str(int(num_str[mid:]))
        else:
            ns1 = str(int(num_str) * 2024)                
        if ns1 != -1:
          if ns1 in rsd.keys():
            rsd[ns1] += num
          else:
            rsd[ns1] = num
        if ns2 != -1:
          if ns2 in rsd.keys():
            rsd[ns2] += num
          else:
            rsd[ns2] = num
     for pp in nk:
        if rsd[pp] == 0:
            rsd.pop(pp)
    ss = 0
    for ns in rsd.values():
      ss += ns
    print(ss)    
    return 

transform_numbers(numbers,75)
