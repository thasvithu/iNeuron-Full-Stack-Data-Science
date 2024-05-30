#1.	Write a Python program to convert kilometers to miles?
def question1():
    km = float(input("Enter kilometers : "))
    miles = km * 0.621371

    print(f"{km} kilometers is equal to {miles:.2f} miles\n")

#question1()

#-----------------------------------------------------------
#2.	Write a Python program to convert Celsius to Fahrenheit?
def question2():
    cel = float(input("Enter celsius : "))
    far = (cel * 9) / 5 + 32

    print(f"{cel} celsius is equal to {far} fahrenheit")


#----------------------------------------------
#3.	Write a Python program to display calendar?
from calendar import Calendar

def question3():
    # Create a Calendar object
    cal = Calendar()

    # Get the current year and month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))

    # Display the calendar for the given year and month
    print(month(year, month))

#question3()


#-------------------------------------------------------
#4.	Write a Python program to solve quadratic equation?
import math

def question4(a, b, c):
    check = b * b - 4 * a * c

    if check > 0:
        #two real solutions
        positive_solution = (-b + math.sqrt(check)) / (2 * a)
        negative_solution = (-b - math.sqrt(check)) / (2 * a)
        return positive_solution, negative_solution

    elif check == 0:
        #one real solution
        solution = (-b) / (2 * a)
        return solution

    else:
        #no real slution
            print("No Real Solution")

#print("Output : ", question4(2, 5, -3))



#-------------------------------------------------------
#5.	Write a Python program to swap two variables without temp variable?
def question5():
    x = 10
    y = 5
     
    print(f"Before swaping value of x = {x} and value of y = {y}")
    x, y = y, x
    print(f"After swaping value of x = {x} and value of y = {y}\n")

#question5()