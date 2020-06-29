'''
Description:
Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater or equal to zero
Examples:
differenatiate("12x+2", 3)      ==>   returns 12
differenatiate("x^2+3x+2", 3)   ==>   returns 9
'''

def differentiate(equation, point):
    
    # Parsing Equation
    temp = []
    for term in equation.split('+'):
        resplit = term.split('-')
        if resplit[0] is not '':
            temp.append(resplit[0])
        for i in range(1, len(resplit)):
            temp.append('-'+resplit[i])
    equation = temp
    
    #Calculating differential
    
    value = 0
    for term in equation:
        if 'x' in term:
            constant, power = term.split('x')
            
            if constant in ['-', '']:
                constant = int(constant+'1')
            else:
                constant = int(constant)

            if power is '':
                value += int(constant)
            else:
                power = int(power[1:])
                differential = constant * power * (point ** (power - 1))
                value += differential
        

    return value
