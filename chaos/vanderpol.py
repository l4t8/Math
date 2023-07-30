import matplotlib.pyplot as plt
from random import randint

for j in range(int(input("Number of points: "))):

    x = randint(1,10)/10
    y = randint(1,10)/10
    xs = []
    ys = []

    for i in range(int(100)):
        u = x
        x += round(u-(1/3)-u**3-y,5)
        y += x
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, color='blue',marker='.', linestyle='-')

plt.axis("equal")
plt.show()