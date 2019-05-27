
# tuple - once created => 
    # heterogeneous immutible sequence
    # can contain any objects
    # nested tuples
    # the objects in it can't be replaced or removed or new elements added
    # syntax => ("asd", 5) => elements access with square brackets and zero-based index
    # len(t) for number of elements
    # iteration with 'for' loop
    # concatenation with '+' operator
    # repetition with '*' operator
    # chain square-brackets indexing to access inner elements - e.g. t[2][1]
    # can't use one object in parentheses as a single element tuple
    # for a single element tuple include a 'trailing comma'
    # the empty tuple is simply empty parentheses
    # delimiting parentheses are optional for one or more elements
    # tuples are useful for multiple return values - min, max, lower, upper, etc.
    # tuple unpacking allows us to destructure directly into named values
    # tuple unpacking works with arbitrarily nested tuples (although not with other data structures)
    # use the tuple(iterable) constructor to create tuples from other iterable series of objects
    # the 'in' and 'not in' operators can be used with tuples - and other collection types for membership testing


t = ("Norway", 4.666, 3)

t[0] # Norway

h = (391)

type(h) # <class 'int'>


p = 1, 1, 1, 4, 6, 189

print(type(p)) # tuple

def minmax(items):
    return min(items), max(items)


print(minmax([83, 33, 84, 32, 85, 31, 86])) # 31, 86


lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])

lower # 31
upper # 86


print(tuple("GGMU")) # ('G', 'G', 'M', 'U')

print('M' in tuple("GGMU")) # True