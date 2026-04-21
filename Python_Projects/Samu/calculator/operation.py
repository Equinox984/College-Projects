
class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        pass


class Addition(Operation):
    def __init__(self, a, b):
        super().__init__(a, b)

    def calculate(self):
        return self.a + self.b



class Multiplication(Operation):
    def __init__(self, a, b):
        super().__init__(a, b)

    def calculate(self):
        return self.a * self.b