f = io.open("20-10.txt","r")
-- written in lua. (with some python)
-- I heeded the warnings in the puzzle and
-- didn't make the mistake of writing a recursive algorithm for
-- this one.
-- noticed that the answer was likely to be a multiplication
-- of combinations. The solution looks for runs
-- of 1s advances. Each run of ones
--advances multplies the possible
-- combinations
-- ie a run of the three ones advances eg 3,4,5 multiplies by 2
-- 3 -> 5, or 3->4->5.
-- a run of four eg 6, 7, 8, 9 has 4 combinations
-- a run of five has 7 combination etc

-- run = {2,4,7,13,24,44,81,149,274}

-- wrote a python algorithm to calculate larger runs, using binary numbers and discounting runs three

--f = 1
--r = 0
--st = ''
--for i in range(10):
--ty = 0
--for i in range(f):
--st = str(bin(i))
--print(st)
--th = 0
--ok = True
--for j in range(len(st)-2):
--if st[j+2] == '1':
--th += 1
--else: th = 0
--if th == 3: ok = False
--if ok:
--print st, 'is ok'
--ty += 1
--f *= 2
--r += 1
--print ty


a, i = {0}, 2
for line in f:lines() do
   a[i] = tonumber(line)
   i = i + 1
end
f:close()
table.sort(a)
jthr, jone = 1, 1
for i = 2,#a - 1 do
   if a[i+1] - a[i] == 1 then
      jone = jone + 1
   end
   if a[i+1] - a[i] == 3 then
      jthr = jthr + 1
   end
end
print("part 1 -",jone *jthr)
a[#a+1] = a[#a] + 3
pt, p, mu = 1, 1, 1
run = {2,4,7,13,24,44,81,149,274}
for i = 1,#a - 1 do
   if a[i+1] - a[i] == 1 then
      jone = jone + 1
      p = p + 1
   end
   if a[i+1] - a[i] == 3 then
      jthr = jthr + 1
      if p > 2 then
         mu = mu * run[p-2]
      end
      p, pt = 1, pt + 1
   end
end
print("part 2 -",mu)
