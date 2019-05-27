import time
print(time.time())

def show_default(arg = time.time()):
    print(arg)


show_default() # EQUAL
show_default() # EQUAL
show_default() # EQUAL

# Default Argument Evaluation

# Default argument values are evaluated when def is evaluated
# They can be modified like any other object


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ['bacon', 'eggs'] # ['bacon', 'eggs', 'spam']
print(add_spam(breakfast))

lunch = ['backed beans'] # ['backed beans', 'spam']
print(add_spam(lunch))

print(add_spam()) # ['spam']

print(add_spam()) # ['spam', 'spam']

print(add_spam()) # ['spam', 'spam', 'spam']
# The default value is executed just once => every next call it keeps the spams and append them

# The solution is straigh forward, but not obvious => ALWAYS USE IMMUTABLE OBJECTS SUCH AS INTEGERS OR STRINGS
def add_spam_with_imm_arg(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


print(add_spam_with_imm_arg()) # ['spam']

print(add_spam_with_imm_arg()) # ['spam']

print(add_spam_with_imm_arg()) # ['spam']

print(add_spam_with_imm_arg()) # ['spam']