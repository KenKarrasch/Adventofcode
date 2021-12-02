f = io.open("a1test.txt","r")
-- aoc puzzles are mild this year, so thought I would 
-- try another language, Lua.
-- phone ide is nice, easier on the eye.
-- Part 1 only.
a = {}
i = 1
for line in f:lines() do
   a[i] = tonumber(line)
   i = i + 1
end
f:close()
s = 5
fd = true
for p = s+1,#a do
   fd = false
   for i = 1,s do
      for j = 1,s do
         if i ~= j then
            if a[p-i] + a[p-j] == a[p] then
               fd = true
            end
         end
      end
   end
   if fd == false then
      print("part 1 -",a[p])
   end
end
