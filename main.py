from math import sqrt

def intro():
    
    global a
    global b
    global c

    print("Welcome to an calculator to resolve second grade equations. Enter the following numbers when asked:\n")
    try:
        a = int(input("Please enter 'a' or the component of the value x^2 = "))
    except ValueError:
            print("Please enter a valid number! \n")
            intro()

    try:
        b = int(input("Please enter 'b' or the component of the value x = "))
    except ValueError:
        print("Please enter a valid number! \n")
        intro()

    try:
        c = int(input("Please enter 'c' or the component of the value without x = "))
    except ValueError:
        print("Please enter a valid number! \n")
    
    calculateDiscriminant()
    
    pass

def calculateDiscriminant():
    
    global discriminant
    discriminant = (b**2) -4*a*c

    if discriminant > 0:
        solveEquation(1)
        pass
    elif discriminant == 0:
        solveEquation(2)
        pass
    elif discriminant < 0:
        solveEquation(3)
        pass
    else:
        print("There was an error in the following calculation try again later \n")
        intro()
    
    pass

def solveEquation(typeOfDiscriminant):
    
    match typeOfDiscriminant:
        case 1:
            firstSolution = (-b + sqrt(discriminant)) / (2*a)
            secondSolution = (-b - sqrt(discriminant)) / (2*a)
            print("This equation have two solutions one of them is " + str(firstSolution) + " and the second one is " + str(secondSolution) + "\n")
            intro()

            pass

        case 2:
            firstSolution = (-b) / (2*a)
            print("This equation only have one solution " + str(firstSolution) + "\n")
            intro()
            pass

        case 3:
            firstSolution = str(((-b) / (2*a))) + " +i" + ((sqrt(discriminant)) / (2*a))
            secondSolution = str(((-b) / (2*a))) + " -i" + ((sqrt(discriminant)) / (2*a))
            print("This equation have two solutions one of them is " + str(firstSolution) + " and the second one is " + str(secondSolution) + "\n")
            intro()
            pass

        case _:
            pass

    
    pass

intro()
