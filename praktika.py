class Student:
    def __init__(self, name, age, avg_grade):
        self.name = name
        self.age = age
        self.avg_grade = avg_grade

    # Методы для установки значений
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_avg_grade(self, avg_grade):
        self.avg_grade = avg_grade

    # Методы для получения значений
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_avg_grade(self):
        return self.avg_grade

    # Метод для вывода информации о студенте
    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.avg_grade}")

    # Метод для оценки студента
    def evaluate_student(self):
        if self.avg_grade > 8:
            return "Отлично"
        elif 6 <= self.avg_grade <= 8:
            return "Хорошо"
        elif 4 <= self.avg_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Создание объектов класса "Студент"
student1 = Student("Иван Иванов", 20, 9.1)
student2 = Student("Мария Смирнова", 22, 7.5)
student3 = Student("Дмитрий Кузнецов", 19, 5.4)

# Демонстрация использования объектов класса "Студент"
students = [student1, student2, student3]

for student in students:
    student.display_info()
    print(f"Оценка: {student.evaluate_student()}\n")
