class ReverseListIterator:
    """Ітератор для зворотного виведення списку."""
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


class EvenIterator:
    """Ітератор, який повертає парні числа від 0 до N."""
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


# приклад використання
if __name__ == "__main__":
    print("Зворотний список:")
    items = [10, 20, 30, 40]
    for x in ReverseListIterator(items):
        print(x)

    print("\nПарні числа до 10:")
    for num in EvenIterator(10):
        print(num)
