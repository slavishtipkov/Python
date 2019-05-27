
# Generators in Python

    # specify iterable sequences
        # all generators are iterators

    # are lazily evaluated
        # the next value in the sequence is computed on demand

    # can model infinite sequences
        # such as data streams with no definite end

    # are composable into pipelines
        # for natural stream processing



def gen123():
    yield 1
    yield 2
    yield 3


#g = gen123()

#print(next(g)) # 1

#print(next(g)) # 2

#print(next(g)) # 3


#for v in gen123():
#    print(v)



def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


g = gen246()

next(g)

next(g)

next(g)

next(g)