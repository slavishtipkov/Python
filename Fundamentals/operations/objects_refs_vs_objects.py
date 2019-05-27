# If you want a function to modify a copy of an object, it's the responsibility of the function to do the copy!!!



# If you want to modify the obj
def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g = ", g)

test = [14, 23, 37]

replace_contents(test) # SAME
print(test) # SAME

# Pass by Object reference
# The value of the reference (its 'content') is copied, not the value of the object


# Return statements do the same
def f(d):
    return d

c = [1, 2, 3]

e = f(c)

print(c is e) # TRUE => The return statements pass the obj reference | No copies!




# Default Arguments

## def function(a, b=value) # <- Default value for 'b', they are optional args by providing default values
# function arguments
def banner(message, border='-'):
    line = border * len(message) # multiplying string to be eq on msg length
    print(line)
    print(message)
    print(line)

banner('Norwegian Blue') # Uses '-'

banner('Sun, Moon and Stars', '*') # If we do provide the optional arg it is used

# The msg is positioned argument and the border is a keyword argument. The actual positioned arguments are mached up by the sequence
# and the keyword arguments are matched by name
banner("Sun, Moon and Stars", border = "*") # The msg is a positional arg, and the sign is keyword arg

banner(border = ".", message="Hello from Earth") # If we replace them, it's a problem :D 
                                               # All key arguments must be specified after the positional arguments !!!