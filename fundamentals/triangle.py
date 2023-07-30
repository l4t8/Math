import matplotlib.pyplot as plt
from random import choice

initialcoords = [[0,0],[1,0],[0.5,0.866025]]
x = [0,1,0.5]
y = [0,0,0.866025]
cur = [float(input("Insert x of the initial point: ")),float(input("Insert y of the initial point: "))]
for i in range(int(input("Insert number of iterations: "))):
    x.append(cur[0])
    y.append(cur[1])
    u = choice(initialcoords)
    cur[0] = (u[0]+cur[0])/2
    cur[1] = (u[1]+cur[1])/2
plt.axis("equal")
plt.figure("Sierpinski triangle")
plt.scatter(x, y, color='blue',s=1)
plt.show()