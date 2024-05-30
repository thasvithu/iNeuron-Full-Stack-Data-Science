#creating class
class Car:
    pass

bmw = Car() #object creation
print(bmw)

bmw.milage = 10
bmw.year = 2024
bmw.model = "BMW NEW 2024"

print(bmw.milage)
print(bmw.year)
print(bmw.model)

nano = Car()
nano.milage = 20
nano.year = 2023
nano.model = "BMW NEW 2024"

print(nano.milage, bmw.milage)