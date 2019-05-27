# str         tuple
# list        range
# disc        set


# Collection Protocols - Container, Sized, Iterable, Sequence, Mutable Sequence, Mutable Set, Mutable Mapping


# To implement a protocol, objects must support certain operations
# Most collections implement Container, Sized and Iterable
# All except set and dict are sequences


# Container         - str, list, range, tuple, bytes, set, dict
###############################################################
# Sized             - str, list, range, tuple, bytes, set, dict
###############################################################
# Iterable          - str, list, range, tuple, bytes, set, dict
###############################################################
# Sequence          - str, list, range, tuple, bytes
###############################################################
# Mutable Sequence  - list
###############################################################
# Mutable Set       - set
###############################################################
# Mutable Mapping   - dict



# Container Protocol
    # Membership testing using 'in' and 'not in'

# Sized Protocol
    # Determine number of elements with len(s)

# Iterable Protocol
    # Can produce an iterator with iter(s)
        # for item in iterable:
            # do_something(item)

# Sequence Protocol
    # Retrieve elements by index
        # item = seq[index]
    # Find items by value
        # index = seq.index(item)
    # Count items
        # num = seq.count(item)
    # Produce a reversed sequence
        # r = reversed(seq)






# Tuples are immutable sequence types
    # Literal syntax: optional parentheses around a comma separated list
    # Single element tuples must use trailing comma
    # Tuple unpacking - return values and idiomatic swap

# Strings are immutable sequence types of Unicode codepoints
    # String concatenation is most efficiently performed with join() on an empty separator
    # The partition() method is a useful and elegant string parsing tool
    # The format() method provides a powerful way of replacing placeholders with values

# Ranges represent integer sequences with regular intervals
    # Ranges are arithmetic progressions
    # The enumerate() function is often a superior alternative to range()

# Lists are heterogeneous mutable sequence types
    # Negative indexes work backwards from the end
    # Slicing allows us to copy all or part of a list
    # The full slice is a common idiom for copying lists although and copy() method and list() constructor is less obscure
    # List (and other collection) copies are shallow
    # List repetition is shallow

# Dictionaries map immutable keys to mutable values
    # Iteration and membership testing is done with respect to the keys
    # Order is arbitrary
    # The keys(), values() and items() methods provide views onto different aspects of a dictionary, allowing convenient iteration

# Sets store an unordered collection of unique elements
    # Sets support powerful and expressive set algebra operations and predicates

# Protocols such as iterable, sequence and container characterise the collections
