class Math:
    def __init__(self, a=float(), b=float()):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a // self.b

    def subtraction(self):
        return self.a - self.b


Math = Math(20, 5)
print(f"Результат сложения: {Math.addition()}\n")
print(f"Результат умножения: {Math.multiplication()}\n")
print(f"Результат деления: {Math.division()}\n")
print(f"Результат вычитания: {Math.subtraction()}\n")
