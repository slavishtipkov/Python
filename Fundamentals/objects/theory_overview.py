# Special cases aren't special enough to break the rules


# We follow patterns, not to kill complexity, but to master it!

# all vars in Python are objects

# Everything is an object => primitive, functions, objects, modules, etc.



# Think of named references to objects rather than variables
    # Assignment attaches a name to an object
    # Assigning from one reference to another puts two name tags on the same object

# The garbage collector reclaims unreachable objects

# id() returns a unique and constant identifier
    # rarely used in production

# The 'is' operator determines equality of identity

# Test for equivalence using '=='

# Function arguments are passed by object-reference
    # functions can modify mutable arguments

# Reference is lost if a formal function argument is rebound
    # To change a mutable argument, replace its CONTENT

# RETURN also passes by object-reference

# Function arguments can be specified with defaults

# Default argument expressions evaluated once, when 'def' is executed

# Python uses dynamic typing
    # We don't specify types in advance

# Python uses strong typing
    # Types are not coerced to match

# Names are looked up in four nested scopes
    # LEGB rule => Local, Enclosing, Global and Built-ins

# Global references can be read from a local scope

# Use 'global' to assign to global references from a local scope

# Everything in Python is an object
    # This includes modules and functions
    # They can be treated just like other objects

# import and 'def' result in binding to named references

# 'type' can be used to determine the type of an object

# dir() can be used to introspect an object and get its attributes

# The name of a function or module object can be accessed through its __name__ attribute

# The docstring for a function or module object can be accessed through its __doc__ attribute

# Use len() to measure the length of a string

# You can multiply a string by an integer
    # Produces a new string with multiple copies of the operand
    # This is called the 'repetition' operation