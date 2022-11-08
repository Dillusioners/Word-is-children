#Author - Jayspray
#Team - Dillusioners
#Word - vast
#Info - The "VAST" majority need stuff in their daily life and what better than a complex calculator for students!
import cmath

print("#########################################################################################################")
print("                                WELCOME TO THE EQUATION SOLVER                                           ")
print("#########################################################################################################")
print("\n\n")

#Function for quadratic equations
def quadratic(num1, num2, num3):
    #Finding the discriminant
    d = (num2 ** 2) - (4 * num1 * num3)
    #Finding the solutions
    sol1 = (-num2 - cmath.sqrt(d)) / (2 * num1)
    sol2 = (-num2 + cmath.sqrt(d)) / (2 * num1)
    #Discerning type of discrimant
    if d > 0:
        print("Type of roots : Two Distinct Roots")
    elif d == 0:
        print("Type of roots : Two equal roots")
    else:
        print("Type of roots : Two complex roots")
    #printing result
    print("Roots of the equation are :-> {} and {} ".format(sol1, sol2))

#Function for simultaneous linear equations
def simultaneous(num1, num2, num3, num4, num5, num6):
    #Finding x and y through the cross multiplication method 
    x = ((num2 * num6) - (num5 * num3)) / ((num1 * num5) - (num4 * num2))
    y = ((num3 * num4) - (num6 * num1)) / ((num1 * num5) - (num4 * num2))
    print("Solutions are x = {} and y = {}".format(x, y))

#Generic brute force nothing much here
def simple_equation(num1 , num2, num3,upperB,lowerB):
    #num1x + num2y = num3
    print("Solutions :->")
    for y in range(lowerB,upperB):
        x = (num3 - num2 * y)/num1
        print("x = {} ; y = {}".format(x,y))
#Distance formula calculation
def dis_form(a1,b1,a2,b2):
    return cmath.sqrt((a1 - a2)**2 + (b1 - b2)**2)

#While loop for choice 
while True:
    try:
        print("Enter the serial numbers for the following...")
        choice = int(input("1.Quadratic Equations\n2.Simultaneous Linear Equations\n3.Simple Linear equation\n4.Distance formula\n>> "))
    except ValueError as e:
        print("Please enter 1, 2, 3 or 4!!!")
        print("Error :->", e)
    else:
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            print("OK moving on")
            break
        else:
            print("Please enter 1, 2, 3 or 4!!!")
#Big while loop to check choices
while True:
    print("So you have chosen option {}".format(choice))
    if choice == 1:
        print("General form of a quadratic equation -> ax**2 + bx + c = 0")
        #while loop inside while loop which has a lot of loggers to avoid any loop breaks
        while True:
            try:
                a = int(input(">> Enter a = "))
                b = int(input(">> Enter b = "))
                c = int(input(">> Enter c = "))
            except ValueError as e:
                print("Please enter Integer value -_-")
                print("Error :->", e)

            else:
                print("Your equation is {}x**2 + {}x + {} = 0".format(a, b, c))
                print("Is this your final choice? ")
                try:
                    print("Are you ok with the equation ?")
                    new_choice = int(input("Enter 1 for Y or 2 for N: "))
                except ValueError:
                    print("Please enter 1 or 2")
                else:
                    if new_choice != 1 and new_choice != 2:
                        print("Please enter 1 or 2")
                    elif new_choice == 1:
                        print("Ok moving on...")
                        break
                    else:
                        print("Ok")
        quadratic(a, b, c)
    #similar elif construct for simultaneous linear equations
    elif choice == 2:
        print("General form of a simultaneous Linear equation :-> a1x + b1y + c1 = 0 , a2x + b2y + c2 = 0")
        while True:
            try:
                a1 = int(input(">> a1 = "))
                b1 = int(input(">> b1 = "))
                c1 = int(input(">> c1 = "))
                a2 = int(input(">> a2 = "))
                b2 = int(input(">> b2 = "))
                c2 = int(input(">> c2 = "))
            except ValueError:
                print("Please enter numeric values only")
            else:
                print("Your equations are {}x + {}y + {} = 0 , {}x + {}y + {} = 0".format(a1, b1, c1, a2, b2, c2))
                try:
                    print("Are you ok with the equations ?")
                    new_choice = int(input("Enter 1 for Y or 2 for N: "))
                except ValueError:
                    print("Please enter 1 or 2")
                else:
                    if new_choice != 1 and new_choice != 2:
                        print("Please enter 1 or 2")
                    elif new_choice == 1:
                        print("Ok moving on...")
                        break
                    else:
                        print("Ok")
        simultaneous(a1,b1,c1,a2,b2,c2)
    #Same stuff for simple equations
    elif choice == 3:
        print("General form of a simple equation :-> ax + by = c")
        while True:
            try:
                a = int(input("a = "))
                b = int(input("b = "))
                c = int(input("c = "))
                uB = int(input(">> Enter upper bound..."))
                lB = int(input(">> Enter lower bound..."))
                if lB > uB:
                    print("Program never executes...bye bye :)")
                    break

            except ValueError:
                print("Please enter numeric values for a,b and c only")
            else:
                print("Your equation is {}x + {}y = {}".format(a,b,c))
                print("And your upper and lower bounds are {} and {}".format(uB,lB))
                try:
                    print("Are you ok with the equation ?")
                    new_choice = int(input("Enter 1 for Y or 2 for N: "))
                except ValueError:
                    print("Please enter 1 or 2!!")
                else:
                    if new_choice != 1 and new_choice != 2:
                        print("Please enter 1 or 2")
                    elif new_choice == 1:
                        print("Ok moving on...")
                        break
                    else:
                        print("Ok")
        simple_equation(a,b,c,uB,lB)
    #Finally distance formula
    elif choice == 4:
        print("General formula for finding distance between 2 points :-> sqrt((x1 - x2)**2 + (y1 - y2)**2)")
        list1 = list()
        list2 = list()
        while True:
            try:
                x1 = int(input("Enter value for x1 : "))
                x2 = int(input("Enter value for x2 : "))
                y1 = int(input("Enter value for y1 : "))
                y2 = int(input("Enter value for y2 : "))
            except ValueError:
                print(">> Please enter numbers only signed/unsigned")
            else:
                print("Your coordinates are -> ({},{}) and ({},{})".format(x1,y1,x2,y2))
                try:
                    new_choice = int(input("Are you okay with the coordinates?: 1 for Y/2 for N : "))
                except ValueError:
                    print("Please enter 1 or 2")
                else:
                    if new_choice != 1 and new_choice != 2:
                        print("Please enter 1 or 2")
                    elif new_choice == 1:
                        print("Ok moving on")
                        break
                    else:
                        print("Okay")
        print(dis_form(x1,y1,x2,y2))
    break

print("[Broadcast]Program has ended...Time SU has entered our land")
