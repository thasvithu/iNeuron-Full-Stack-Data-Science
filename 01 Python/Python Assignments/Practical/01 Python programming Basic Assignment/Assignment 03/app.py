"""
Author @vithusan
2024/05/24
"""

#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
def question1(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
#number = int(input("Enter a number : "))
#print(f"{number} is {question1(number)}")


#--------------------------------------------------------------
#2.	Write a Python Program to Check if a Number is Odd or Even?
def question2(num):
    return "Even Number" if num % 2 == 0 else "Odd Number"

#num = int(input("Enter a number : "))
#print(f"{num} is {question2(num)}")


#---------------------------------------------
#3.	Write a Python Program to Check Leap Year?
def question3(year):
    return "Leap Year" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not Leap Year"

#year = int(input("Enter a year : "))
#print(f"{year} is {question3(year)}")


#------------------------------------------------
#4.	Write a Python Program to Check Prime Number?
import math

def question4(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
         
#num = int(input("Enter a number to check prime or not: "))
#print(f"{num} is Prime: {question4(num)}")



#-------------------------------------------------------------------------------
#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
import math

def question4():
    for i in range(1, 101):
        if i < 2:
            print(f"{i} is not prime")
        elif i == 2:
            print(f"{i} is prime*")
        elif i % 2 == 0:
            print(f"{i} is not prime")
        else:
            is_prime = True

            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if i % j == 0:
                    print(f"{i} is not prime")
                    is_prime = False
                    break
            if is_prime:
                print(f"{i} is prime*")

question4()