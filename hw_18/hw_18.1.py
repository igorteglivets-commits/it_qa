def even_numbers(n):
    """Генератор парних чисел від 0 до n."""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def fibonacci(n):
    """Генератор чисел Фібоначчі до n."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# приклад використання
if __name__ == "__main__":
    N = 10

    print("Парні числа:")
    for num in even_numbers(N):
        print(num)

    print("\nФібоначчі:")
    for num in fibonacci(N):
        print(num)
