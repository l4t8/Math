vars = {}

def dinput(expression):
    valid = True
    if len(expression.split(" ")) == 2 and expression.replace(" ","") != "": expression = "This is not valid"
    expression = expression.replace(" ","")
    if expression == "": return ""
    equals = False
    if "=" in expression:
        equals = expression.split("=")[0]
        expression = expression.split("=")[1]
    for i in expression:
        if i in vars.keys():
            expression = expression.replace(i,str(vars[i]))
    if equals:
        vars[equals] = calc(expression)
        return calc(expression)
    else: return calc(expression)
    tokens = tokenize(expression)
        
#This code belongs to my solution of the mentioned kata in the description
def divideexpintoparts(daexp):
    #Divide the expression into nums and *, / --> [2,-2,3,"*",32,"/",32]
    #No need for "+" or "-"
    dalist = []
    currentint = True
    cur = ""
    for i in range(len(daexp)):
        if daexp[i] in "+-/*%":
            dalist.append(cur)
            cur = ""
            dalist.append(daexp[i])
        else:
            cur += daexp[i]
    dalist = [i for i in dalist if i != ""]
    dalist.append(cur)
    nlist = []
    for i in range(len(dalist)):
        if dalist[i] in "/*%":
            nlist.append(dalist[i])
        elif dalist[i] in "+-":
            pass
        elif i != 0 and dalist[i-1] == "-":
            nlist.append(float(dalist[i])*-1)
        else:
            nlist.append(float(dalist[i]))
    return [i for i in nlist if i != ""]

def solve(ez):
    
    #Solve the expression
    ez = divideexpintoparts(ez)
    
    #Make the multiplicacions and divisions
    while "*" in ez or "/" in ez or "%" in ez:
        for i in range(len(ez)):
            if ez[i] == "*":
                op1 = ez[i-1]
                op2 = ez.pop(i+1)
                ez.pop(i)
                ez[i-1] = float(op1)*float(op2)
                break
            elif ez[i] == "/":
                op1 = ez[i-1]
                op2 = ez.pop(i+1)
                ez.pop(i)
                ez[i-1] = float(op1)/float(op2)
                break
            elif ez[i] == "%":
                op1 = ez[i-1]
                op2 = ez.pop(i+1)
                ez.pop(i)
                ez[i-1] = float(op1)%float(op2)
                break
    #Due to the fact that we formated our list like [a,b,c,d] and not [a,"+",b,"+",c,"+",d] we can just sum
    return sum([float(i) for i in ez if i != ""])
        
        
def calc(expression):
    exp = str(expression).replace(" ","")
    exp = exp.replace("--","+")
    exp = exp.replace("+-","-")
    u = ""
    while "(" in exp:
        exp = exp.replace("--","+")
        exp = exp.replace("+-","-")
        for i in range(len(exp)):
            if exp[i] == "(":
                u = i
            elif exp[i] == ")":
                #Replace all the parenthesis with a number with the solved expression in between the parenthesis
                exp = exp.replace(exp[u:i+1],str(solve(exp[u+1:i])))
                exp = exp.replace("--","+")
                exp = exp.replace("+-","-")
                break
    return float(solve(exp))

print("This is an interpreter able to perform easy mathematical operations involving the use of trivial operators\
(+/%-*) and variable assignment.")
while True:
    x = input(">")
    print(dinput(x))