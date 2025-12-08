import random
from .database import engine, SessionLocal, Base
from .models import Student, Course

Base.metadata.create_all(bind=engine)

session = SessionLocal()

course_titles = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
courses = [Course(title=title) for title in course_titles]
session.add_all(courses)

students = [Student(name=f'Student{i}') for i in range(1, 21)]
session.add_all(students)

for student in students:
    student.courses = random.sample(courses, k=random.randint(1, 3))

session.commit()
session.close()

print("Seed data inserted successfully!")
