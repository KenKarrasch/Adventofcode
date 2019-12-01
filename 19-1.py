f = open('19-1.txt').read().split('\n')
# Had to think on how to round. Started 25min late.
# May have made the leaderboard if I wasn't late. Oh well.
fl = 0
p1 = 0
for m in f:
    mass = int(m)
    p1 += ((mass-mass%3)/3)-2
    rfl = mass
    while rfl > 0:
        nrfl = ((rfl-rfl%3)/3)-2
        if round(nrfl > 0):
            fl += round(nrfl)
        rfl = round(nrfl)   
print ('part 1 -', p1)
print ('part 2 -', fl)
