
#dict
    # delimited by { and }
    # key-value pairs comma separated
    # corresponding keys and values joined by colon
    # the KEY obj must be immutable
    # the VALUE obj can be mutable
    # dict() constructor accepts:
        # iterable series of key-value 2-tuples
        # keyword arguments - requires keys are valid Python identifiers
    # Copying  -  d.copy() for copying dictionaries
    # Or the other copying simply dict(d) constructor
    # Extend a dictionary with update()
    # Update replaces values corresponding to duplicate keys
    # Iteration is over keys
    # Get corresponding value with d[key] lookup
    # Remember! Order is arbitrary!
    # Use values() for an iterable view onto the series of values
    # No efficient way to get the key corresponding to a value
    # keys() method gives iterable view onto keys - not often needed
    # Use items() for an iterable view onto the series of key-value tuples
    # Use with tuple unpacking
    # The 'in' and 'not in' operators work on the keys
    # Use del keyword to remove by key
    # keys myst be immutable
    # values may be mutable
    # The dictionary itself is mutable
    # Python Standard Library 'pprint' module
    # Be careful not to rebind the module reference!
    # Knows how to pretty-print all built-in data structures, including => dict

d = {'article': 'asdfhfd', 'bob': 'worm'}

print(d['bob']) # 'worm'