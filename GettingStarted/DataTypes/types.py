

# STRINGS

print('Hello World' == "Hello World" == """Hello World""")

hel = 'hello'

hel.capitalize() == 'Hello'
hel.replace('e', 'a') == 'hallo'
hel.isdigit()

# String formats

name = "PythonBo"
machine = "HAL"

testformat = "Nice to meet you {0}. I am {1}".format(name, machine)
print(testformat)

print(f"Nice to meet you {name}. I am {machine}")


# Boolean and None

python_course = True
java_course = False

print("Boolean and None")

print(int(python_course) == 1)
print(java_course == 0)
print(str(python_course) == "True")

aliens_found = None

print(aliens_found)
print(aliens_found == java_course)


# int
answer = 42

# float
pi = 3.14159


# Don't worry about conversions
print(answer + pi)

# checking convertors
isequal = int(pi) == 3
iseq = float(answer) == 42.0

print(isequal)
print(iseq)


def add_numbers(a, b):
    print(a + b)

add_numbers(1, 2)

def add_numbers_type_hinting(a: int, b: int) -> int:
    return a + b

print(add_numbers_type_hinting(1, 3))