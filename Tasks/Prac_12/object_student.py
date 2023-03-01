class Student:
    """Класс Student"""

    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        print(f"Имя студента: {self.name}\n")

    def getAge(self):
        print(f"Возраст студента: {self.age}\n")

    def getGroupNumber(self):
        print(f"Группа студента: {self.groupNumber}\n")

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


Ivan = Student()
Ivan.getAge()
Ivan.getName()
Ivan.getGroupNumber()
print(f"----------------------------\n")
Maria: Student = Student()
Maria.setNameAge("Maria", 17)
Maria.setGroupNumber("10C")
Maria.getAge()
Maria.getName()
Maria.getGroupNumber()
print(f"----------------------------\n")
Viktor = Student()
Viktor.setNameAge("Viktor", 15)
Viktor.setGroupNumber("8C")
Viktor.getAge()
Viktor.getName()
Viktor.getGroupNumber()
