
# FUNCTIONSSSSSSSS

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student)
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def var_args(name, **kwargs):
    print(name)
    print(kwargs["descr"], kwargs["m"])


students_list = get_students_titlecase()

add_student("Mark", 0)
add_student("Sashko")
add_student("Ivan")
add_student("Michka")
add_student("Kirsi", 15444)

print_student_titlecase()

var_args("Mark", descr = "Loves Python", m=None, k="Hi", isit=True, ornot=False, arr=[])