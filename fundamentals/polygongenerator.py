import matplotlib.pyplot as plt
from math import sin,cos,pi

ncoords = [(0+1j)]
initialcoords = []
sides = int(input("Number of sides: "))
mul = round(sin(2*pi/sides),9)*1j+round(cos(2*pi/sides),9)
for i in range(sides):
    ncoords.append(round((ncoords[i]*mul).real,4)+round((ncoords[i]*mul).imag,4)*1j)

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

x = []
y = []
for i in initialcoords:
    x.append(i[0])
    y.append(i[1])

plt.axis("equal")
plt.scatter(x, y, color='blue',s=50)
plt.show()
