class Car:
    def __init__(self, milage, year, model):
        """
        self is not keyword it is a pointer
        init is used to pass data to class
        """
        self.milage = milage
        self.year = year
        self.model = model


bmw = Car(50, 2024, "BMW 2024")

nano = Car(25, 2023, "NANO 2023")

# object or instance variables can not access using class
# print(Car.milage)

print(nano.milage)
