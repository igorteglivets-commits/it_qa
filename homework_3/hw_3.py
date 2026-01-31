

alice_in_wonderland = """ 
Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to, said the Cat.
I don't much care where —— said Alice.
Then it doesn't matter which way you go, said the Cat.
—— so long as I get somewhere, Alice added as an explanation.
Oh, you're sure to do that, said the Cat, if you only walk long enough.
"""

print(alice_in_wonderland)



single_quotes = [ch for ch in alice_in_wonderland if ch == "'"]
print(single_quotes)



print(f"Площа Чорного моря становить 436402 км²,\n"
    f"а площа Азовського моря становить 37800 км²,- разом {436402 + 37800}")

#Мережа супермаркетів має 3 склади, де всього розміщено
#375 291 товар. На першому та другому складах перебуває
#250 449 товарів. На другому та третьому – 222 950 товарів.
#Знайдіть кількість товарів, що розміщені на кожному складі.


total_goods = 375_291
sum_1_2 = 250_449
sum_2_3 = 222_950

# розрахунки
y = (sum_1_2 + sum_2_3 - total_goods)  # склад 2
x = sum_1_2 - y                        # склад 1
z = sum_2_3 - y                        # склад 3

print(f"Перший склад: {x}")
print(f"Другий склад: {y}")
print(f"Третій склад: {z}")



months = 18
payment_per_month = 1179
total_price = months * payment_per_month

print(f"Михайло з батьками платитимуть {months} місяців по {payment_per_month} грн.")
print(f"Отже, вартість комп’ютера становить {total_price} грн.")



print(f"a) 8019 % 8 = {8019 % 8}")
print(f"b) 9907 % 9 = {9907 % 9}")
print(f"c) 2789 % 5 = {2789 % 5}")
print(f"d) 7248 % 6 = {7248 % 6}")
print(f"e) 7128 % 5 = {7128 % 5}")
print(f"f) 19224 % 9 = {19224 % 9}")



print(f"Піца велика: {4*274} грн")
print(f"Піца середня: {2*218} грн")
print(f"Сік: {4*35} грн")
print(f"Торт: {350} грн")
print(f"Вода: {3*21} грн")
print(f"Загальна сума замовлення: {4*274 + 2*218 + 4*35 + 350 + 3*21} грн")




print(f"Щоб вклеїти всі фото, Ігорю знадобиться {232 // 8} сторінок.")




distance = 1600
tank = 48
consumption_per_100km = 9

fuel_needed = distance * consumption_per_100km // 100

refills = fuel_needed // tank

print(f"Для подорожі потрібно {fuel_needed} літрів бензину.")
print(f"Щонайменше родині потрібно заїхати на заправку {refills} рази.")

