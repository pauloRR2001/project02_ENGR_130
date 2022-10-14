'''
===============================================================================
ENGR 130 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     HW6 - Task1 Functions
	Author:         Paulo Ramirez, ramir378
	Team ID:        19 (individual for this hw) 
	

=+=============================================================================
'''
"""
------------------------------------
Name of function: intCheck
Viarialbes:
        numb #Function input, number
Purpose: Checks if the input is an integer and outputs error if it is not 
Author: ramir378
------------------------------------
"""
def intCheck(numb):
    if numb != round(numb, 0) or numb < 0:
        print('Error: Input a positive integer')
        return (True)
    else:
        return (False)
    
"""
------------------------------------
Name of function: myFactorial
Viarialbes:
        numb #Function input, number to calculate factorial of
        fac #Factorial of numb
Purpose: Calculates the factorial of the input and returns it. 
        Where factorial = n(n-1)(n-2)*...2*1
Author: This function was developed by team 19
------------------------------------
"""
def myFactorial(numb):
    fac = 1
    while numb >= 1:
        fac = fac * numb
        numb = numb - 1
    return fac

"""
-------------------------------------
Name of function: summand
Viarialbes:
        x #Independent variable of the function (a and b)
        n #Number of cycles (terms) the function goes through
        arg #Argument - Shortcut of common argument for inner functions
        a_n #Named by calculus convention, nth output of the function
            as a function of n
Purpose: This function is each factor in the summation (argument of the sigma)
        it uses myFactorial and an alternating sign based on n
Author: ramir378
------------------------------------
"""
def summand(x, n):
    arg = 2 * n + 1
    a_n = ((-1) ** n) * (x ** arg) / ((arg) * myFactorial(arg))
    return a_n

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''