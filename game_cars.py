import random  # щоб випадкові числа працювали


# 1. Клас машинки
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        speed = random.randint(20, 100)  # випадкова швидкість
        print(f"{self.make} {self.model} їде зі швидкістю {speed} км/год!")


# 2. Створюємо машинки
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2022)
car3 = Car("Ford", "Focus", 2019)

# 3. Вибір користувачем
print("Вибери машинку: 1 - Toyota, 2 - BMW, 3 - Ford")
choice = int(input("Введи номер машинки: "))

if choice == 1:
    player_car = car1
elif choice == 2:
    player_car = car2
else:
    player_car = car3

# 4. Гра - 5 поїздок
for i in range(1, 6):
    print(f"\n--- Поїздка {i} ---")
    player_car.drive()
