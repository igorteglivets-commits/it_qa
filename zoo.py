# Клас Тварина
class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.hunger = 5  # 0 - дуже сита, 10 - дуже голодна
        self.alive = True  # якщо False -> тварина втекла

    def make_sound(self):
        if not self.alive:
            print(f"{self.name} більше немає в зоопарку... 😢")
            return
        if self.hunger >= 8:
            print(f"{self.name} ({self.species}) дуже голодна і каже: 'Дай їсти!' 😿")
        else:
            print(f"{self.name} ({self.species}, {self.age} років) каже: {self.sound}")

    def feed(self):
        if not self.alive:
            print(f"{self.name} вже втекла, ти не можеш її нагодувати 😔")
            return
        if self.hunger > 0:
            self.hunger -= 2
            if self.hunger < 0:
                self.hunger = 0
            print(f"🍎 Ти погодував {self.name}. Ситість тепер: {10 - self.hunger}/10")
        else:
            print(f"{self.name} вже сита і не хоче їсти! 😊")

    def status(self):
        if not self.alive:
            print(f"{self.name} втекла з зоопарку! 🚪🐾")
        else:
            print(f"{self.name}: ситість {10 - self.hunger}/10")

    def get_hungrier(self):
        """Тварина стає голоднішою з часом"""
        if self.alive and self.hunger < 10:
            self.hunger += 1
        elif self.hunger >= 10 and self.alive:
            print(f"⚠️ {self.name} не витримала голоду і втекла з зоопарку! 🏃‍♂️🐾")
            self.alive = False


# Створюємо об'єкти (тварин)
cat = Animal("Мурчик", "кіт", 3, "Мяу! 🐱")
dog = Animal("Шарік", "собака", 5, "Гав! 🐶")
parrot = Animal("Ківі", "папуга", 2, "Карр! 🦜")

# Список тварин
zoo = [cat, dog, parrot]

# Меню
while True:
    print("\n=== ЗООПАРК ===")
    for i, animal in enumerate(zoo, start=1):
        status = "✅" if animal.alive else "❌ Втекла"
        print(f"{i}. {animal.name} ({animal.species}) - {status}")
    print("0. Вийти 🚪")

    choice = input("Вибери номер тварини: ")

    if not choice.isdigit():
        print("❌ Треба ввести число.")
        continue

    choice = int(choice)

    if choice == 0:
        print("Дякуємо, що завітав у зоопарк! 👋")
        break

    if 1 <= choice <= len(zoo):
        selected_animal = zoo[choice - 1]

        # Підменю для вибраної тварини
        while True:
            print(f"\n--- {selected_animal.name} ---")
            print("1. Почути звук 🐾")
            print("2. Нагодувати 🍎")
            print("3. Подивитися статус 📊")
            print("0. Назад 🔙")

            action = input("Що зробити? ")

            if not action.isdigit():
                print("❌ Треба ввести число.")
                continue

            action = int(action)

            if action == 1:
                selected_animal.make_sound()
            elif action == 2:
                selected_animal.feed()
            elif action == 3:
                selected_animal.status()
            elif action == 0:
                break
            else:
                print("❌ Невірна дія!")

            # 🔥 Після кожної дії всі тварини голоднішають
            for a in zoo:
                if a != selected_animal:
                    a.get_hungrier()

    else:
        print(f"❌ Введи число від 0 до {len(zoo)}.")
