# Dominick Larson
# UWYO COSC 1010
# 11/4/2024
# Lab 08
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def string_checker(Checks):
    returnValue = False
    try:
        returnValue = float(Checks)
        returnValue = int(Checks)
    except:
        pass
    return returnValue
    
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope(m, b, a, an):
    M = string_checker(m)
    B = string_checker(b)
    A = string_checker(a)
    AN = string_checker(an)
    if (M and B and A and AN):
        yvare = []
        for x in range (A, AN):
            y = M * x + B
            yvare.append(y)
        return yvare
    else: 
        print("The inputs need to be numbers")
while True:
    m = input("input an m ")
    if (m == "exit"):
        break
    b = input("input an b ")
    if (b == "exit"):
        break
    a = input("input a lower bound x ")
    if (a == "exit"):
        break
    an = input("input an upper bound x ")
    if (an == "exit"):
        break
    print(slope(m, b, a, an))



print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quad(a,b,c):
    a = string_checker(a)
    b = string_checker(b)
    c = string_checker(c)
    Square = (b*b - 4*(a + c))
    if Square != complex:
        Squared1 = (((b*b - 4*(a + c))**0.5) + -b) / 2*a
        Squared2 = (((b*b - 4*(a + c))**0.5) - -b) / 2*a
        return (Squared1, Squared2)
    else:
        return False

while True:
    a = input("input a A ")
    if (a == "exit"):
        break
    b = input("input a B ")
    if (b == "exit"):
        break
    c = input("input a C ")
    if (c == "exit"):
        break
    if quad(a,b,c) != False:
        print (quad(a,b,c))
    else:
        print ("squared value cannot be negative")