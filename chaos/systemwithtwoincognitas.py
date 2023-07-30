import matplotlib.pyplot as plt
from random import randint

for j in range(int(input("Number of points: "))):

    x = randint(0,100)
    y = randint(0,100)
    xs = []
    ys = []

    for i in range(int(100)):
        x += -y-x*0.1
        y += x-0.4*y
        xs.append(x)
        ys.append(y)
    plt.plot(xs, ys, color='blue',marker='.', linestyle='-')

plt.axis("equal")
plt.show()