
f = open('24-14.txt').read().split('\n')
import re
md = []

for i in f:
    numbers = re.findall(r'-?\d+', i)
    md.append(list(map(int, numbers)))
print(md)


def update_position(robot, W, H, time):
    x, y, vx, vy = robot
    new_x = (x + vx * time) % W
    new_y = (y + vy * time) % H
    return (new_x, new_y, vx, vy)

W, H = 11, 7 # Room dimensions
W, H = 101, 103 # Room dimensions

time = 100  # Seconds to simulate

# List of robots with initial positions and velocities
robots = []

for i in md:
    robots.append((i[0],i[1],i[2],i[3]))    

updated_robots = [update_position(robot, W, H, time) for robot in robots]

cy = H//2
cx = W//2

for i in updated_robots:
    print(i)
print(H,W)
print(cx,cy)
q1,q2,q3,q4 = 0,0,0,0

for i in updated_robots:
    if i[1] > cy and i[0] > cx:
        q1 += 1
    if i[1] > cy and i[0] < cx:
        q2 += 1
    if i[1] < cy and i[0] > cx:
        q3 += 1
    if i[1] < cy and i[0] < cx:
        q4 += 1    

print(q1,q2,q3,q4) 
print(q1*q2*q3*q4)
