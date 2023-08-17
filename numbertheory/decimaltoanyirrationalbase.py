from math import pi

def converter(n, decimals=0, base=pi):
    
    if base == 10 and decimals == 0:
        return str(n)
    
    #This works for all numbers that fit that condition
    elif base == 10:
        if str(n).count(".") == 1:
            return (str(n) + "." + "0"*decimals)[:-2]
        return str(n) + "." + "0"*decimals
    
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = list(range(10,37))
    negative = False
    
    daput = []
    k = 0
    
    if 0 > n:
        negative = True
        n = -1*n
        
    while n // base**k > 1:
        k += 1
        
    while k*(-1)-1 != decimals:
        daput.append(n//(base**k))
        n %= base**k
        k -= 1
    
    theput = ""
    for i in daput:
        if int(i) in nums:
            theput += str(abc[nums.index(int(i))])
        else:
            theput += str(int(i))
            
    diput = theput[::-1]
    diput = diput[:decimals] + "." + diput[decimals:]
    duput = diput[::-1]
    
    #Testing for errors made along the way
    if duput[-1] == ".":
        duput = duput[:-1]
    if duput[0] == "0" and duput[1] != ".":
        duput = duput[1:]
    if negative:
        duput = "-" + duput
    
    return duput
