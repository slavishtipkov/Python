students = []

class Student:

    school_name = "PGASG" # Static

    def __init__(self, name, student_id = 332): # Constructor
        self.name = name
        self.student_id = student_id


    def __str__(self): # ToString like
        return "Student " + self.name + " learning in " + self.school_name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.school_name



class HighSchoolStudent(Student):

    school_name = "UASG => VIAS BATKO... :((" # Static ovveride

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize() # Calls parent definition
        return original_value + "-HS" # Add additional behaviour (Ovveriding again)


bojo = HighSchoolStudent("nojooo")
print(bojo.get_name_capitalize()) # Nojooo-HS