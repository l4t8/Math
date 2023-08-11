from math import sqrt,ceil,floor
def isPP(n):
    for i in range(2,ceil(sqrt(n))+1):
        x = pow(n,1/i)
        if ceil(x)-x < 0.00000001:x = ceil(x)
        elif x-floor(x) < 0.00000001:x = floor(x)
        if int(x) == float(x): return [int(x),i]
