import random


# 1. Клас машинки
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self, bonus=0):
        speed = random.randint(20, 100) + bonus  # швидкість + бонус
        return speed


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

# 4. Комп'ютер вибирає випадкову машинку
computer_car = random.choice([car1, car2, car3])
print(f"Комп’ютер вибрав: {computer_car.make} {computer_car.model}")

# 5. Лічильники перемог
player_wins = 0
computer_wins = 0

# 6. Гонка - 5 раундів
for i in range(1, 6):
    print(f"\n--- Раунд {i} ---")

    # Користувач обирає бонус
    bonus = int(input("Введи бонус швидкості для своєї машинки (0-20): "))

    # Комп’ютер отримує випадковий бонус
    computer_bonus = random.randint(0, 20)

    # Обчислюємо швидкість
    player_speed = player_car.drive(bonus)
    computer_speed = computer_car.drive(computer_bonus)

    print(f"Твоя машинка: {player_car.make} {player_car.model}, швидкість {player_speed} км/год (бонус +{bonus})")
    print(
        f"Машинка комп’ютера: {computer_car.make} {computer_car.model}, швидкість {computer_speed} км/год (бонус +{computer_bonus})")

    if player_speed > computer_speed:
        print("Ти виграв цей раунд! 🏆")
        player_wins += 1
    elif player_speed < computer_speed:
        print("Комп’ютер виграв цей раунд! 🤖")
        computer_wins += 1
    else:
        print("Нічия! ⚖️")

# 7. Підсумок гонки
print("\n=== Підсумок гонки ===")
print(f"Ти виграв {player_wins} раундів")
print(f"Комп’ютер виграв {computer_wins} раундів")

if player_wins > computer_wins:
    print("Вітаю! Ти виграв гонку! 🏁🎉")
elif player_wins < computer_wins:
    print("Комп’ютер виграв гонку! 🤖🏁")
else:
    print("Гонка завершилась нічією! ⚖️")
