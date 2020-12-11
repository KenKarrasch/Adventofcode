f = io.open("20-11.txt","r")

-- straightforward puzzle
-- learned some new things (and pitfalls) about Lua,
-- local variables,
-- multidimensional arrays, string manipulation, functions 
-- executes in 7 secs, which isn't
-- particularly fast.


-- would be intereseted in how
-- this compares to other languages, maybe
-- the data types used are slow

-- made the mistake of not copying the input file 
-- properly, this costed me several minutes

ar = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}}
a, i = {},1

for l in f:lines() do
   a[i], j = {},1
   for c = 1, #l do
      a[i][j] = string.sub(l,c,c)
      j = j + 1
   end
   i = i + 1
end
f:close()
dim = #a

function dc(b)
   local a = {}
   for i = 1,#b do
      a[i] = {}
      for j = 1,#b[i] do
         a[i][j] = b[i][j]
      end
   end
   return (a)
end

function safe(a)
   if a > 0 and a<=dim then
      return true
   end
   return false
end

function findp(p,i,j,d1,d2,md)
   local m = 1
   while safe(i+d1*m) and safe(j+d2*m) and m < md + 1 do
      if p[i+d1*m][j+d2*m] == "#" then
         return true
      end
      if p[i+d1*m][j+d2*m] == "L" then
         return false
      end
      m = m + 1
   end
   return false
end

function proc(p,cr,md)
   local n = dc(p)
   for i = 1,#p do
      for j = 1,#p[i] do
         ct = 0
         for d = 1,#ar do
            if findp(p,i,j,ar[d][1],ar[d][2],md) then
               ct = ct + 1
            end
         end
         if(
         p[i][j] == "L") then
            if ct == 0 then
               n[i][j] = "#"
            end
         end
         if(
         p[i][j] == "#") then
            if ct > cr then
               n[i][j] = "L"
            end
         end
      end
   end
   return(n)
end

function same(c,d)
   for i = 1,#c do
      for j = 1,#c[i] do
         if c[i][j] ~= d[i][j] then
            return false
         end
      end
   end
   return true
end

function occ(b)
   local ct = 0
   for i = 1,#b do
      for j = 1,#b[i] do
         if a[i][j] == "#" then
            ct = ct + 1
         end
      end
   end
   return ct
end

c, sme = dc(a), false
while sme == false do
   b = proc(a,3,1)
   sme = same(a,b)
   a = dc(b)
end
print("part 1 -",occ(a))
a, sme = dc(c), false
while sme == false do
   b = proc(a,4,#a)
   sme = same(a,b)
   a = dc(b)
end
print("part 2 -",occ(a))
