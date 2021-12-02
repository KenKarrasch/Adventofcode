f = io.open("20-10.txt","r")

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
print("part 1 -",jone*jthr)
a[#a+1] = a[#a] + 3
memo = {}

function getdist (i)
   if i == #a then
      return 1
   end
   if memo[i] ~= nil then
      return memo[i]
   end
   local ans = 0
   for j = i+1, #a do
      if a[j] - a[i] <= 3 then
         ans = ans + getdist(j)
      end
   end
   memo[i] = ans
   return ans
end

print("part 2 -",getdist(1))
