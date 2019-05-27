##################################################################
# GENERATOR => FUNCTION WITH AT LEAST ONE 'YIELD' STATEMENT !    #
##################################################################

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# Lucas's generator

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


for x in (p for p in lucas() if is_prime(p)):
        print(x)