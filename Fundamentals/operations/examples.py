
# Passed by object reference and 'worked' direct over it, so the 'input' obj reference is changed

m = [9, 15, 24]
def modify(k):
    k.append(39)
    print("k= ", k)

modify(m) # k=  [9, 15, 24, 39]





# the value of the reference is copied, not the value of the object

f = [14, 23, 37]
def replace(g):
    g = [17, 28, 45]
    print("g = ", g)


replace(f) # g =  [17, 28, 45]
