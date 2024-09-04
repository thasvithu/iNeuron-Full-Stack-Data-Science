#1.	Write a Python Program to Find the Factorial of a Number?
def factorial(num: int) -> int:
    """
    This function returns the factorial of a number.
    """

    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        fact: int = 1
        for i in range(1, num + 1):
            fact *= i
        return fact


if __name__ == "__main__":
    num: int = int(input("Enter a number : "))
    print(f"Factorial of {num} is {factorial(num)}")
