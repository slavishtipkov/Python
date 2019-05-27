# Python is Dynamic and STRONGLY typed

# Dynamic type system =>
# In a dynamic type system object types are only resolved at runtime

def add(a, b):
    return a + b

 # Becouse it's dynamic lang, it's able to try operations without type check before time of running

add(5, 7) # Dynamic

add(3.1, 4.6) # Dynamic

add('asd', 'test') # Dynamic


# Strong type system => In a strong type system there is no implicit type conversion

add("The answer is ", 42) # This produces a type error



# Object references have no type!
# they can be rebound or reassigned and so on

# Python Name Scopes => Scopes are contexts in which named references can be looked up


# Python Name Scopes
    # Local => Inside the current function
    # Enclosing => Any and all enclosing functions
    # Global => Top-level of module
    # Built-in => Provided by the builtins module

# L ocal
# E nclosing
# G lobal
# B uilt-in

# LEGB rule => 