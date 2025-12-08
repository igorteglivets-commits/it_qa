from .database import SessionLocal
from .models import Student, Course

session = SessionLocal()

print("Список студентів та їх курсів:")

students = session.query(Student).all()
for s in students:
    course_names = [c.title for c in s.courses]
    print(f"{s.name}: {', '.join(course_names)}")

session.close()
from hw_22_1 import crud

def main():
    print("=== Додавання нового студента ===")
    new_student = crud.add_student("Ivan", [1, 3])  # додаємо студента до курсів 1 та 3
    print(f"Added student: {new_student.name}, ID: {new_student.id}\n")

    print("=== Список студентів на курсі 2 ===")
    students_in_course = crud.get_students_in_course(2)
    print([s.name for s in students_in_course], "\n")

    print("=== Курси студента ID=1 ===")
    courses_of_student = crud.get_courses_of_student(1)
    print([c.title for c in courses_of_student], "\n")

    print("=== Оновлення студента ID=1 ===")
    updated_student = crud.update_student(1, new_name="Petro", new_course_ids=[2, 4])
    if updated_student:
        print(f"Updated student: {updated_student.name}")
        courses = [c.title for c in updated_student.courses]
        print(f"New courses: {courses}\n")
    else:
        print("Student not found\n")

    print("=== Видалення студента ID=1 ===")
    deleted = crud.delete_student(1)
    print("Deleted student?" , deleted, "\n")

    print("=== Перевірка студентів на курсі 2 після видалення ===")
    students_in_course = crud.get_students_in_course(2)
    print([s.name for s in students_in_course], "\n")


if __name__ == "__main__":
    main()
