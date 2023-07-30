import matplotlib.pyplot as plt
from random import choice
from math import sin,cos,pi

ncoords = [(0+1j)]
initialcoords = []
cur = [0,1]
x = [0,0]
y = [0,0]
sides = int(input("Number of sides: "))
mul = round(sin(2*pi/sides),9)*1j+round(cos(2*pi/sides),9)
for i in range(sides-1):
    ncoords.append(round((ncoords[i]*mul).real,3)+round((ncoords[i]*mul).imag,3)*1j)

def polartocartesian(polar):
    polar = str(polar).replace("(","").replace(")","")
    n = 1
    if polar[0] == "-":
        n = -1
        polar = polar[1:]
    if "-" in polar:
        return (float(polar.split("-")[0])*n,float(polar.split("-")[1].replace("j",""))*-1)
    elif "+" in polar:
        return (float(polar.split("+")[0])*n,float(polar.split("+")[1].replace("j","")))
    elif "j" in polar:
        return (0,float(polar[:-1]))
    else:
        return (float(polar),0)
    
for i in ncoords:
    initialcoords.append(polartocartesian(i))

print(initialcoords)

for i in range(1000000):
    x.append(cur[0])
    y.append(cur[1])
    u = choice(initialcoords)
    cur[0] = (u[0]+cur[0])/2
    cur[1] = (u[1]+cur[1])/2
    
plt.axis("equal")
plt.scatter(x, y, color='blue',s=1)
plt.show()
