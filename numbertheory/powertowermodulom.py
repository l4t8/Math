import math
def phi(n):
    x = n
    divisors = set()
    while n % 2 == 0:
        divisors.add(2)
        n //= 2
    while n % 3 == 0:
        divisors.add(3)
        n //= 3
    i = 5
    while i*i <= n:
        for k in (i, i+2):
            while n % k == 0:
                divisors.add(k)
                n //= k
        i += 6
    if n > 1:
        divisors.add(n)
    for i in divisors:
        x *= (1-(1/i))
    return int(x)

def tower(base, h, m):
    
    if base == 1: return 1
    elif h == 2: return pow(base,base,m)
    elif m == 1: return 0
    elif h == 0: return 1
    elif base % m == 0: return 0
    mods = [m]
    #Adds mods until they reach 1 
    for i in range(h-1):
        k = phi(mods[-1])
        if k == 1: break
        mods.append(k)
    #Adds bases 
    bases = []
    for mod in mods:
        if base % mod == 0: bases.append(mod)
        else: bases.append(base%mod)
    
    while len(bases) != 1:
        mods.pop(-1)
        newbase = pow(bases.pop(-2),bases.pop(-1),mods[-1])
        if newbase == 0: bases.append(mods[-1])
        else: bases.append(newbase)
    return int(bases[0]%mods[0])