import csv
import os

def merge_csv_and_remove_duplicates(file1, file2, key):
    for f in (file1, file2):
        if not os.path.exists(f):
            raise FileNotFoundError(f"Файл {f} не знайдено!")

    # Читаємо обидва файли
    all_data, all_columns = [], set()
    for filename in (file1, file2):
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            all_data.extend(reader)
            all_columns.update(reader.fieldnames)

    all_columns.discard('')  # прибираємо порожні колонки

    # Видаляємо дублікати
    seen, unique = set(), []
    for row in all_data:
        k = row.get(key, tuple(row.values()))
        if k not in seen:
            seen.add(k)
            unique.append(row)

    # Записуємо результат
    output_file = "merged_unique.csv"
    with open(output_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_columns))
        writer.writeheader()
        writer.writerows(unique)

    print(f"Унікальних рядків: {len(unique)}, результат збережено у {output_file}")
    return unique, all_columns

# Виклик функції
merged_data, all_columns = merge_csv_and_remove_duplicates(
    "random_1.csv", "random_2.csv", "ContactID"
)
