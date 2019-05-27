# Errors should never pass silently, unless explicitly silenced. Errors are like bells and if we make them silent,
# they are of no use.

# Raising an exception interrupts normal program flow and transfers control to an exception handler

# Exception handlers defined using the try...except construct

# try block define a context for detecting exceptions

# Corresponding except blocks handle specific exception types

# Python uses exceptions pervasively
    # Many built-in language features depend on them

# except blocks can capture an exception, which are often of a standard type

# Programmer errors should not normally be handled

# Exceptional conditions can be signaled using raise

# raise without an argument re-raises the current exception

# Generally do not check for TypeErrors

# Exception objects can be converted to strings using str()

# A function's exceptions form part of its API
    # They should be documented properly

# Prefer to use built-in exception types when possible

# Use the try...finally construct to perform cleanup actions
    # May be used in conjuction with except blocks

# Output of print() can be redirected using the optional file argument

# Use and AND or FOR combining boolean expressions

# Return codes are too easily ignored

# Platform-specific actions can be implemented using EAFP along with catching ImportErrors



# Avoid protecting against TypeErrors
    # This is against the grain in Python
    # It's usually not worth checking types
    # This can limit your functions unnecessarily
    # Just let it fail



# Dealing with failers
    #Two Philosophies
        # LBYL - Look Before You Leap
        # EAFP - It's Easier to Ask Forgiveness than Permission


    # OS Example:
        # LBYL 

        # Only check for existance

import os

p = '/path/to/datafile.dat'

if os.path.exists(p):
    #os.sys.process_file(p)
#else:
    print('No such file as {}'.format(p))


        # More possible problems
            # Garbage
            # Directory 
            # Race condition


        
        # EAFP

p = '/path/to/datafile.dat'

try:
    #process_file(f)
    print('fake')
except OSError as e:
    print('Could not process file because{}'.format(str(e)))




# Local vs. Non-Local Handling

    # Error codes require interspersed, local handling
    # Exceptions allow centralized, non-local handling



# EAFP + Exceptions

    # Exceptions require explicit handling

    # Error codes are silent by default
        # EAFP + Exceptions = errors are difficult to ignore!




# Resource Cleanup with Finally
    # try...finally lets you clean up whether an exception occurs or not

