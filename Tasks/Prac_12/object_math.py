class Math:
    def __init__(self, a=float(), b=float()):
        self.a = a
        self.b = b

    def addition(self):
        print(f"{self.a + self.b}\n")

    def multiplication(self):
        print(f"{self.a * self.b}\n")

    def division(self):
        print(f"{self.a // self.b}\n")

    def subtraction(self):
        print(f"{self.a - self.b}\n")


Math = Math(20, 5)
Math.addition()
Math.multiplication()
Math.division()
Math.subtraction()
