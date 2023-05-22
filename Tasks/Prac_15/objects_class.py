class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашние задания:{self.avg_grade()}\n' \
              f'Курсы в процессе обучения:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'
        return res

    def avg_grade(self):
        if not self.grades:
            return 0
        full_grade = 0
        for k in self.grades.values():
            j = k.copy()
            while len(j) != 0:
                i = j.pop()
                full_grade += int(i)
        return full_grade / len(k)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return res

    def avg_grade(self):
        if not self.grades:
            return 0
        full_grade = 0
        for k in self.grades.values():
            j = k.copy()
            while len(j) != 0:
                i = j.pop()
                full_grade += int(i)
        return full_grade / len(k)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_lecturer_1 = Lecturer('Дим', 'Димыч')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Федор', 'Федоров')
best_lecturer_2.courses_attached += ['Java']

cool_rewiewer_1 = Reviewer('Some', 'Buddy')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']

cool_rewiewer_2 = Reviewer('Иван', 'Иванов')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

student_1 = Student('Петр', 'Петров', 'Male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Олег', 'Олегов', 'Male')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 4)

student_2.rate_hw(best_lecturer_2, 'Java', 5)
student_2.rate_hw(best_lecturer_2, 'Java', 10)

cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_2, 'Java', 5)

cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 6)
cool_rewiewer_2.rate_hw(student_1, 'Python', 4)


print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')
print()
print()

student_list = [student_1, student_2]
lecturer_list = [best_lecturer_1, best_lecturer_2]


def student_rating(student_list, course_name):
    full_grades = 0
    i = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            full_grades += stud.avg_grade()
            i += 1

    return full_grades / i


def lecturer_rating(lecturer_list, course_name):
    full_grades = 0
    i = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            full_grades += lect.avg_grade()
            i += 1
    return full_grades / i


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
