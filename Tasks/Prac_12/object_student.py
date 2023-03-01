class Student:
    """Класс Student"""

    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


Ivan = Student()
print(f"Возраст студента: {Ivan.getAge()}\n")
print(f"Имя студента: {Ivan.getName()}\n")
print(f"Группа студента: {Ivan.getGroupNumber()}\n")
print(f"----------------------------\n")

Maria: Student = Student()
Maria.setNameAge("Maria", 17)
Maria.setGroupNumber("10C")
print(f"Возраст студента: {Maria.getAge()}\n")
print(f"Имя студента: {Maria.getName()}\n")
print(f"Группа студента: {Maria.getGroupNumber()}\n")
print(f"----------------------------\n")

Viktor = Student()
Viktor.setNameAge("Viktor", 15)
Viktor.setGroupNumber("8C")
print(f"Возраст студента: {Viktor.getAge()}\n")
print(f"Имя студента: {Viktor.getName()}\n")
print(f"Группа студента: {Viktor.getGroupNumber()}\n")
