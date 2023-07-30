import matplotlib.pyplot as plt
from random import choice
cur = [0,0]
x = []
y = []
last = ""
initialcoords = [[0, 1.0], [-0.866, 0.5], [-0.866, -0.5], [0, -1.0], [0.866, -0.5], [0.866, 0.5]]
for i in range(100000):
    u = choice(initialcoords)
    while last == u:
        u = choice(initialcoords)
    cur[0] = (u[0]*2+cur[0])/3
    cur[1] = (u[1]*2+cur[1])/3
    last = u
    x.append(cur[0])
    y.append(cur[1])

plt.axis("equal")
plt.scatter(x, y, color='blue',s=1)
plt.show()