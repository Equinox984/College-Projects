class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        raise NotImplementedError("Subclasses must implement calculate()")

class Addition(Operation):
    def calculate(self):
        return self.a + self.b

class Multiplication(Operation):
    def calculate(self):
        return self.a * self.b

class Subtraction(Operation):
    def calculate(self):
        return self.a - self.b

class Division(Operation):
    def calculate(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.a / self.b
