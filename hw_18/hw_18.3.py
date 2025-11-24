def log_calls(func):
    """Декоратор, який логує аргументи та результат функції."""

    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат: {result}\n")
        return result

    return wrapper


def handle_exceptions(func):
    """Декоратор, який перехоплює та обробляє винятки."""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Сталася помилка у функції {func.__name__}: {e}")
            return None

    return wrapper



@log_calls
def add(a, b):
    return a + b


@handle_exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("Тест логуючого декоратора:")
    add(5, 7)

    print("Тест декоратора обробки помилок:")
    print(divide(10, 2))
    print(divide(10, 0))