import matplotlib.pyplot as plt
from random import choice
cur = [0.5,0.5]
x = []
y = []
last = ""
initialcoords = [[0, 1.0], [-0.951, 0.309], [-0.588, -0.809], [0.588, -0.809], [0.951, 0.309]]
for i in range(1000000):
    u = choice(initialcoords)
    while last == u:
        u = choice(initialcoords)
    cur[0] = (u[0]+cur[0])/2
    cur[1] = (u[1]+cur[1])/2
    last = u
    x.append(cur[0])
    y.append(cur[1])

plt.axis("equal")
plt.scatter(x, y, color='blue',s=1)
plt.show()