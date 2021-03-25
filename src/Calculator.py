def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return a - b


def Multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b


def division(a, b):
    a = int(a)
    b = int(b)
    return a / b


def squaring(a):
    a = int(a)
    return a * a


def squareRooting(a):
    a = int(a)
    return a ** 0.5


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def sqrt(self, a):
        self.result = squareRooting(a)
        return self.result
