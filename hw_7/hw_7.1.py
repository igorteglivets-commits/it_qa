# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number}x{multiplier}={result}")
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_num():
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

sum_two_num()


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_numbers(numbers):
    total_numbers = sum(numbers)
    count_of_numbers = len(numbers)
    average = total_numbers / count_of_numbers
    print(f"Середнє арифметичне: {average}")

# Виклик функції з будь-яким списком наприклад: [2,3,3,2]
average_of_numbers([2,3,3,2])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]  # перевертає рядок зріз

while True:
    user_input = input("Введіть рядок: ")
    reversed_text = reverse_string(user_input)
    print("Рядок у зворотному порядку:", reversed_text)

    again = input("Хочете спробувати ще раз? (так/ні): ").lower()  # тут ловер
    if again == "так":
        continue
    else:
        print("Дякую! Програму завершено.")
        break


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words_list):
    return max(words_list, key=len)

while True:
    user_input = input("Введіть слова через пробіл: ")
    words = user_input.split()
    longest = longest_word(words)
    print("Найдовше слово:", longest)

    again = input("Хочете спробувати ще раз? (так/ні): ").lower()
    if again != "так":
        print("Дякую! Програму завершено.")
        break

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""