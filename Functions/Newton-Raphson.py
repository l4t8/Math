def findaround(coefficients,value):

    #The value is only a starting value
    #The function does not work for functions without solution

    # With coefficients [-1,2,3,1,2] --> f(x) = -x^4 + 2x^3 + 3x^2 + x + 2
    # Calculates the coefficients of the derivative
    deriv = [coeff*exp for exp,coeff in enumerate(coefficients[::-1])][::-1][:-1]

    x = "0"
    if not deriv: return 
    while value != x:
        x = value
        value = value - sum([coeff*(value**exp) for exp,coeff in list(enumerate(coefficients[::-1]))])/sum([coeff*(value**exp) for exp,coeff in list(enumerate(deriv[::-1]))])
    return value

print(findaround([1,1,1],2))