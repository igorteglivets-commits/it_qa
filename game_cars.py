import random
import time


# 1. Клас машинки
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.position = 0  # позиція на треку

    def drive(self, bonus=0):
        step = random.randint(1, 5) + bonus
        self.position += step
        return step


# 2. Створюємо машинки
car1 = Car("Toyota", "Camry")
car2 = Car("BMW", "X5")
car3 = Car("Ford", "Focus")

cars = [car1, car2, car3]

# 3. Вибір користувачем з обробкою помилок
while True:
    try:
        choice = int(input("Вибери машинку: 1 - Toyota, 2 - BMW, 3 - Ford: "))
        if choice not in [1, 2, 3]:
            raise ValueError("Номер машинки повинен бути 1, 2 або 3!")
        player_car = cars[choice - 1]
        break
    except ValueError as e:
        print("Помилка:", e)

# 4. Комп'ютер вибирає випадкову машинку
computer_car = random.choice(cars)
print(f"Комп’ютер вибрав: {computer_car.make} {computer_car.model}")

# 5. Довжина треку
track_length = 30

# 6. Гонка
round_number = 1
while player_car.position < track_length and computer_car.position < track_length:
    print(f"\n--- Раунд {round_number} ---")

    # Вводимо бонус з ексепшинами
    while True:
        try:
            bonus = int(input("Введи бонус швидкості (0-3): "))
            if bonus < 0 or bonus > 3:
                raise ValueError("Бонус має бути між 0 і 3!")
            break
        except ValueError as e:
            print("Помилка:", e)

    computer_bonus = random.randint(0, 3)

    # Рухаємо машинки
    player_step = player_car.drive(bonus)
    computer_step = computer_car.drive(computer_bonus)

    # Показуємо трек
    print("Трек:")
    print("Твоя машинка:     " + "-" * player_car.position + "🚗")
    print("Машинка комп'ютера:" + "-" * computer_car.position + "🤖")

    round_number += 1
    time.sleep(1)

# 7. Підсумок гонки
print("\n=== Фініш! ===")
if player_car.position >= track_length and computer_car.position >= track_length:
    print("Нічия! ⚖️ Обидві машинки дісталися фінішу одночасно!")
elif player_car.position >= track_length:
    print("Вітаю! Твоя машинка виграла гонку! 🏁🎉")
else:
    print("Комп’ютер виграв гонку! 🤖🏁")
