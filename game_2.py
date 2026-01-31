import time


# Клас машинки
class Car:
    def __init__(self, name):
        self.name = name
        self.position = 0  # де зараз машинка

    def drive(self):
        self.position += 1
        return self.position


# Створюємо дві машинки
car1 = Car("Toyota")
car2 = Car("BMW")

# Довжина треку
track_length = 10

# Гонка
while car1.position < track_length and car2.position < track_length:
    car1.drive()
    car2.drive()

    # Відображаємо трек
    print("Трек:")
    print("Toyota: " + "-" * car1.position + "🚗")
    print("BMW:    " + "-" * car2.position + "🚙")

    time.sleep(0.5)  # затримка для анімації
    print("\n")

# Підсумок
if car1.position >= track_length and car2.position >= track_length:
    print("Нічия! ⚖️ Обидві машинки дісталися фінішу одночасно!")
elif car1.position >= track_length:
    print("Toyota виграла гонку! 🏁🎉")
else:
    print("BMW виграла гонку! 🏁🎉")
