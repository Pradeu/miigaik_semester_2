class Car:
    def __init__(self, color="Белый", type="Иномарка", year="2004", status="Не заведен"):
        self.color = color
        self.type = type
        self.year = year
        self.status = status

    def show_stats(self):
        print(f"Цвет автомобиля: {self.color}\n"
              f"Тип автомобиля: {self.type}\n"
              f"Год выпуска автомобиля: {self.type}\n"
              f"Статус автомобиля: {self.status}\n")

    def turn_on(self):
        self.status = "Заведен"
        print(f"Автомобиль заведен\n")

    def turn_off(self):
        self.status = "Не заведен"
        print(f"Автомобиль не заведен\n")

    def setYear(self, year):
        self.year = year
        print(f"Установлен год выпуска автомобиля: {self.year}\n")

    def setType(self, type):
        self.type = type
        print(f"Установлен тип автомобиля: {self.type}\n")

    def setColor(self, color):
        self.color = color
        print(f"Установлен цвет автомобиля: {self.color}\n")


car = Car()
car.turn_off()
car.turn_on()
car.show_stats()

car_1 = Car()
car_1.setYear("2005")
car_1.setType("Грузовик")
car_1.setColor("Серый")
car_1.show_stats()
