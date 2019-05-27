student_courses = []

def add_student_course(course):
    student_courses.append(course)


def print_student_courses():
    for course in student_courses:
        print("Student course => " + course)


def save_file(course):
    try:
        f = open("course.txt", "a")
        f.write(course + "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("course.txt", "r")
        for course in f.readlines():
            add_student_course(course)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
course = input("Enter course name: ")

add_student_course(course)

print_student_courses()
save_file(course)
read_file()