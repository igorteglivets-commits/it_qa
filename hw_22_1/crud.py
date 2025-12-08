from .database import SessionLocal
from .models import Student, Course


def add_student(name: str, course_ids: list):
    session = SessionLocal()
    student = Student(name=name)

    courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    student.courses = courses

    session.add(student)
    session.commit()
    session.refresh(student)
    session.close()
    return student


def get_students_in_course(course_id: int):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == course_id).first()
    students = course.students if course else []
    session.close()
    return students


def get_courses_of_student(student_id: int):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    courses = student.courses if student else []
    session.close()
    return courses


def update_student(student_id: int, new_name: str = None, new_course_ids: list = None):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        session.close()
        return None

    if new_name:
        student.name = new_name
    if new_course_ids is not None:
        courses = session.query(Course).filter(Course.id.in_(new_course_ids)).all()
        student.courses = courses

    session.commit()
    session.refresh(student)
    session.close()
    return student


def delete_student(student_id: int):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
    session.close()
    return student is not None


from hw_22_1 import crud

new_student = crud.add_student("Ivan", [1, 3])
print("Added student:", new_student.name)

students = crud.get_students_in_course(2)
print("Students in course 2:", [s.name for s in students])

courses = crud.get_courses_of_student(1)
print("Courses of student 1:", [c.title for c in courses])

updated = crud.update_student(1, new_name="Petro", new_course_ids=[2, 4])
print("Updated student:", updated.name)

deleted = crud.delete_student(1)
print("Deleted student?", deleted)


