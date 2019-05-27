
##################################################################
# GENERATOR => FUNCTION WITH AT LEAST ONE 'YIELD' STATEMENT !    #
##################################################################


 # Python offers for creating iterable objects. Comprehensions, generators and any object that 
 # follows iterable or iterator protocols can be used in iterations. Python provides a number of built-in functions
 # for performing common iterator operations. These functions form the call of a sort of vocabulary for working with 
 # iterators, and they can be combined to produce powerful statements in very concise, readable code.




 # Generator comprehensions

    # Similar syntax to list comprehensions

    # Create a generator object

    # Concise

    # Lazy evaluation



#million_squares = (x*x for x in range(1, 1000001)) from 1 to 1 million
#list(million_squares)


#print(sum(x*x for x in range(1, 10000001)))  from 1 to 10 millions, I can't reproduce on my machine :D





# Stateful generators

    # Generators resume execution

    # Can maintain state in local variables

    # Complex control flow

    # Lazy evaluation



# Simple si better than complex

# Code is written once
# But read over and over
# Fewer is clear

# Minimum of side effects
# Maximum functional

# print([x for x in range(101) if is_prime(x)])



from utils import is_prime


print(sum(x for x in range(1001) if is_prime(x)))
