
student = {
    "name": "Marko",
    "last_name": "Polo",
    "student_id": 1513333,
    "feedback": None,
    "courses": {
        "current": ["Python", "Web basics", "Css", "Python"],
        "past": ["html", "js basics"]
    }
}

print(student)

print(student.get("nameeee", "default"))

print(student.keys())

print(student.values())

del student["name"]


try:
    last_name = student["last_name"]
    test = 3 + last_name
    
    print("Ima batko.." + last_name)
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together!!!")
    print(error)
except Exception:
    print("Unknown error... lose lose")
finally:
    print("This code ends here no matter what")
