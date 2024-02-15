class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        if self.num1 > 0 and self.num2 > 0:
            return self.num1 + self.num2
        else:
            return "Invalid input"

    def subtract(self):
        if self.num1 > 0 and self.num2 > 0:
            return self.num1 - self.num2
        else:
            return "Invalid input"

    def multiply(self):
        if self.num1 > 0 and self.num2 > 0:
            return self.num1 * self.num2
        else:
            return "Invalid input"

    def divide(self):
        if self.num1 > 0 and self.num2 > 0:
            return self.num1 / self.num2
        else:
            return "Invalid input"


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calc = Calculator(num1, num2)

print("Addition: ", calc.add())
print("Subtraction: ", calc.subtract())
print("Multiplication: ", calc.multiply())
print("Division: ", calc.divide())
