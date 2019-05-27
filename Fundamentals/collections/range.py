
#range
    # arithmetic progression of integers
    # stop value is one-past-the-end
    # ranges are 'half-open' - start is includet but stop is not
    # stop value of a range used as start value of consecutive range
    # avoid range() for iterating over lists
    # Python is not C
    # don't be un-pythonic!
    # not using range - enumerate
        # Prefer enumerate() for counters
        # enumerate() yields (index, value) tuples
        # Often combined with tuple unpacking


for i in range(5): # 1 argument => start
    print(i) # 0 ... 4


print(list(range(5, 10))) # [5, 6, 7, 8, 9]  2 arguments => start stop
print(list(range(10, 15))) # [10, 11, 12, 13, 14] cool

print(list(range(10, 20, 2))) # [10, 12, 14, 16, 18]  3 arguments => start stop step


t = [6, 324, 4533, 463636, 345232, 235235]
for p in enumerate(t):                     # (0, 6)
    print(p)                               # (1, 324)
                                           # (2, 4533)
                                           # (3, 463636)
                                           # (4, 345232)
                                           # (5, 235235)

for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))  # i = 0, v = 6 .. etc.