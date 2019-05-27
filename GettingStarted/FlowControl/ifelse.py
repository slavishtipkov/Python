number = 233

if number > 300:
    print(1)
elif number < 200:
    print(2)
elif number < 250:
    print(3)


if True:
    print("It's true!")

if False:
    print("It's true!")

# Ternary

a = 1
b = 2

True or print("bigger" if a > b else "smaller")


False or print("bigger" if a > b else "smaller")




number = 5

if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")


test = 5.5
if test:
    print("Test is defined and truthy")

text = "Python"
if text:
    print("Text is defined and truthy")

python_course = True
if python_course:
    print("This will execute")


aliens_found = None
if aliens_found:
    print("This will not execute")

if number != 5:
    print("test")

if number == 5 and python_course:
    print('opaa')