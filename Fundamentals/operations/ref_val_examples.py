# Value equality vs. identity
#
# Value => equivalent "contents"
# Identity => same object


# Value comparison can be controlled programatically


# Lists references

p = [4, 7, 11]
q = [4, 7, 11]

print(p == q) # true

print (p is q) # False => Different objects with same value

# id() deals with the objects, not the reference!!!

# NO VARIABLES

# instead => Named references to objects



r = [2, 4, 6]
s = r
s[0] = 1

print(s is r) #true



# References to objects

x = 1000

y = 500

x = y

print(x) # 500
print(y) # 500

print(x == y) # true

print(x is y) # true

# ints are immutable, created for every different one



a = 496
print(id(a)) #21345634623424

b = 1729
print(id(b)) #213453543452

b = a

print(id(b) == id(a)) # True  =>  The ids are equals, because these two refs points to the same object

print(id(b) is id(a)) # False  => It's false, because they are different refs with common object (value)
