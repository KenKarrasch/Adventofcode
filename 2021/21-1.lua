f = io.open("21-1.txt","r")
-- kick off with lua
p = 0
ct = 0
a = {}
r = 0
t = 0

for l in f:lines() do
    a[r] = tonumber(l)
    if a[r] > p then
        ct = ct + 1
    end
    p = a[r]
    r = r + 1
end
print("part 1 -",ct-1)
ct = 0
p = 0
ln = r
r = 0
for j = 0,ln-3 do
    t = 0
    for i = r,r+2 do
        t = t + a[i]
    end
    if t > p then
        ct = ct + 1
    end
    p = t
    r = r + 1
end
print("part 2 -",ct-1)
f.close()
