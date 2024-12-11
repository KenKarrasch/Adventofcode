f = open('24-11.txt').read() # '5 89749 6061 43 867 1965860 0 206250'

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
  
transformed = transform_numbers(numbers,75)
