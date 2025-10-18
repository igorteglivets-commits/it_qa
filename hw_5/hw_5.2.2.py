# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
# have age >=30. Print condition check result



people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

print("=== Step 1: Додаємо новий запис на початок ===")
people_records.insert(0, ('Igor', 'Tkachenko', 32, 'QA Engineer', 'Kyiv'))
for idx, record in enumerate(people_records):
    print(f"{idx}: {record}")

print("\n=== Step 2: Міняємо місцями елементи з індексами 1 і 5 ===")
people_records[1], people_records[5] = people_records[5], people_records[1]
for idx, record in enumerate(people_records):
    print(f"{idx}: {record}")

print("\n=== Step 3: Перевірка віку для індексів 6, 10, 13 ===")
indexes_to_check = [6, 10, 13]
check_result = all(people_records[i][2] >= 30 for i in indexes_to_check)
for i in indexes_to_check:
    print(f"Index {i}: {people_records[i][0]} {people_records[i][1]}, вік = {people_records[i][2]}")

print("\nРезультат перевірки (всі >= 30):", check_result)
