# task 01 == Виправте синтаксичні помилки :)
print("Hello", end = " ")
print("world!")


# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4

print("Яблук:", apples)
print("Бананів:", bananas)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4


perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Периметр фігури:", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?

"""


apples = 4
pears = apples + 5
plums = apples - 2

print("Яблук було:", apples, "Груш було:", pears, "Слив було:", plums)

total = apples + pears + plums
print("Всього дерев:", total)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

before_lunch = 5
after_lunch = before_lunch - 10
in_evening = after_lunch + 4

print("Надвечір", in_evening )


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

drama_b = 24
drama_g = drama_b // 2

ill_b = drama_b - 1       # хлопці, які прийшли
present_g = drama_g - 2    # дівчата, які прийшли

total_present = ill_b + present_g

print("Сьогодні у театральному гуртку", (total_present), "дитини")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2

total = book_1 + book_2 + book_3
print(total)