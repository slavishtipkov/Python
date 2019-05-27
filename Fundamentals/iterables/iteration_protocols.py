
# Iteration protocols
    # Iterable protocol - Iterable objects can be passed to the built-in iter() function to get an iterator
        # iterator = iter(iterable)

    # Iterator protocol - Iterator objects can be passed to the built-in iter() function to fetch the next item
        # item = next(iterator)



iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)

print(next(iterator))

print(next(iterator))

print(next(iterator))

print(next(iterator))

# print(next(iterator)) # StopIteration => Exception, because of no next element to iterate



def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")


# test

print(first([1, 2, 3, 4, 5, 6]))