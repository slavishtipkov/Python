x = 5

def f(a):
    return a

c = f(x)

print(c) # 5

print(x) # 5

print(x == c) # True

print(c is x) # True

# The integers are immutable objects, so the refferences points to the same (5) object



x = 4 # When another object is assigned to 'x', they are not equal again, neighte by value (object) or reference

print(c == x) # False