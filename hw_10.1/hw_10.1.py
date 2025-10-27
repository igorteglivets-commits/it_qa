#Створіть клас Employee, який має атрибути name та salary.
#Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
#Клас Manager повинен мати додатковий атрибут department,
#а клас Developer - атрибут programming_language.

#Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), Developer(ім'я, зарплата, мова програмування),
#а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


lead = TeamLead("Ігор", 5000, "R&D", "Python", 5)
print(f"Ім'я: {lead.name}")
print(f"Зарплата: {lead.salary}")
print(f"Відділ: {lead.department}")
print(f"Мова програмування: {lead.programming_language}")
print(f"Розмір команди: {lead.team_size}")


