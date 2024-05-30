#Question 1
#1.	Write a Python program to print "Hello Python"?
print("Hello Python")
print("\n")

#Question 2
#Write a Python program to do arithmetical operations addition and division.?
a = 5 + 4
print("Addtion output : ", a)
b = 10
c = 5
z = b / c
print("Division output : ", z)
print("\n")

#Question 3
#3.	Write a Python program to find the area of a triangle?
base = 12
height = 6
area = (base * height) / 2
print("Area of Triangle : ", area)
print("\n")

#Question 4
#4.	Write a Python program to swap two variables?
a = 10
b = 5
print("Before swap value of a : ", a)
print("Before swap value of b : ", b)

temp = a
a = b
b = temp
print("After swap value of a : ", a)
print("After swap value of b : ", b)
print("\n")

#Question 5
#5.	Write a Python program to generate a random number?
import random
a = 10
b = 1000
r = random.randint(a, b)
print(("Random value between {} to {} : ").format(a, b), r)