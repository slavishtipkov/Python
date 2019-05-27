
# list
    # heterogeneous mutable sequence
    # negative integers index from the end
    # The last element is at index -1
    # Avoid seq[len(seq) - 1]
    # Slicing extracts part of a list
    # slice = seq[start: stop]
    # Slice range is half-open - stop not included
    # Slicing works with negative indexes
    # Omitting the stop index slices to the end
    # Omitting the start index slices from the beginning [:stop]
    # Half-open ranges give complementary slices =>   s[:x] + s[x:] == s
    # Omitting the start and stop indexes slices from the beginning to the end - full slice
    # Important idiom for copying lists =>   full_slice = seq[:]
    # Other copy options =>   copy() method ...   u = seq.copy()   |   list() constructor ...   v = list(seq)
    # Repeat lists using the '*' operator
    # Most often used for initializing a list of know size with a constant: s = [constant] * size   
        # Multiple references to one instance of the constant in the produced list
    # Repetition is shallow!
    # Finding elements => index(item) returns the integer index of the first equivalent element raises => ValueError if not found
    # count(item) returns the number of matching elements
    # The 'in' and 'not in' operators test for membership
    # del seq[index] to remove by index
    # seq.remove(item) to remove by value; raises ValueError if not present
    # remove() equivalent to del seq[seq.index(item)]
    # Insert items with =>  seq.insert(index, item)
    # Concatenate lists with '+' operator
    # In-place extension with '+=' operator or extend() method
    # k.reverse() reverses in place
    # k.sort() sorts in place
    # k.sort(reverse=True) gives descending sort
    # 'key' argument to sort() method accepts a function for producing a sort key from an item
    # be aware of unintentional side-effects with in situ reearrangements
    # sorted() built-in function sorts any iterable series and returns a list
    # reversed() built-in function reverses any iterable series


x = [4, 9, 2, 1]
y = sorted(x)
print(y) # [1, 2, 4, 9]
print(x) # [4, 9, 2, 1]

p = [9, 3, 1, 0]
q = reversed(p)
print(q) # <list_reverseiterator object at 0x7f0c6e35b860>
list(q) # [0, 1, 3, 9]

example = "show how to index into sequence".split()
print(example[4]) # into
print(example[-5]) # how
print(example[1:-1]) # ['how', 'to', 'index', 'into']
print(example[3:]) # ['index', 'into', 'sequence']


shallow_copy_test = [[1, 2], [3, 4]]
b = shallow_copy_test[:]  # New reference for the biggest list, but it keeps the same references to inner elements (inner 2 list => [1,2], [3,4])
print(b)



test = [1, 2, 3, 4].append('asd')
print(test) # No error, prints => 'None'