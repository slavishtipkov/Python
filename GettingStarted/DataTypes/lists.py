# List

student_names = ["Sharo", "Petio", "Kotio"]

print(student_names) # ["Sharo", "Petio", "Kotio"]

print(student_names[0]) # Normal

student_names.append("Kotka")

print(student_names.count("Sharo")) # counts how many times appears given element - 1 is the right

student_names[2] = "Zuzu"

print(student_names.index("Sharo")) # 0 - right answ

print(student_names) # ['Sharo', 'Petio', 'Zuzu', 'Kotka']

print("Sharo" in student_names) # true

print("Konio" in student_names) # false

print(len(student_names)) # 4 - right

print("Sharo" in student_names) # Yep

# Slicing

kravi = ["milka", "shpilka", "darilka", "merilka"]

del kravi[1] # deletes the el with index = 1

print(kravi) # ['milka', 'darilka', 'merilka']

print(kravi[1:]) # Remove one from the begining

print(student_names[1:-1]) # Remove 1 from the begining and 1 from the end