class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = None

    def set_grade(self):
        """Введення середнього балу з перевіркою"""
        while True:
            try:
                grade = int(input(f"Введіть середній бал для {self.name} {self.surname} (0–5): "))
                if 0 <= grade <= 5:
                    self.average_grade = grade
                    break
                print("⚠️ Бал має бути цілим числом від 0 до 5!")
            except ValueError:
                print("❌ Введіть число!")

    def show_info(self):
        """Вивід інформації про студента"""
        print(f"{self.name} {self.surname}, {self.age} років — середній бал: {self.average_grade}")

    def update_grade(self):
        """Оновлення середнього балу через input"""
        while True:
            try:
                grade = int(input(f"Введіть новий середній бал для {self.name} (0–5): "))
                if 0 <= grade <= 5:
                    self.average_grade = grade
                    print(f"✅ Бал оновлено: {self.average_grade}")
                    break
                print("⚠️ Бал має бути цілим числом від 0 до 5!")
            except ValueError:
                print("❌ Введіть число!")


# Створюємо список студентів
students = [
    Student("Іван", "Петренко", 18),
    Student("Марія", "Коваленко", 19),
    Student("Олег", "Сидоренко", 20)
]

# Вводимо оцінки
for s in students:
    s.set_grade()

# Виводимо інформацію
print("\n📋 Інформація про студентів:")
for s in students:
    s.show_info()

# Функція для обчислення середнього балу групи
def group_average(students_list):
    total = sum(s.average_grade for s in students_list)
    return total / len(students_list)

print(f"\n🎓 Середній бал групи: {round(group_average(students), 2)}")

# Можливість оновити бал студентів
while True:
    name_input = input("\nВведіть ім'я студента для зміни балу (або 'вихід'): ").capitalize()
    if name_input.lower() == "вихід":
        break

    for s in students:
        if s.name == name_input:
            s.update_grade()
            print(f"🎓 Новий середній бал групи: {round(group_average(students), 2)}")
            break
    else:

        print("⚠️ Студента з таким іменем не знайдено.")

# 🔹 Після виходу з циклу виводимо підсумковий середній бал групи
final_average = round(group_average(students), 2)
print(f"\n📊 Підсумковий середній бал групи після всіх змін: {final_average}")