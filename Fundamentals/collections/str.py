
# str
    # homogeneous immutable sequence of Unicode codepoints (characters)
    # len(s) gives number of codepoints (characters)
    # Strings are immutable so the '+=' operator re-binds the reference to a new object
    # Call the join() method on the separator string
    # Use split() to divide a string into a list
    # without an argument, split() divides on whitespace
    # join()-ing an empty separator si an important and fast way to concatenating a collection of strings
    # The way may not be obvious at first
    # To concatenate invoke join on empty text => something for nothing :D
    # the partition() method divides a string into three arround a separator: prefix, separator, suffix
    # tuple unpacking is useful to destructure the result
    # use underscore as a dummy name for the separator
    # Underscore convention understood by many tools
    # Use format() to insert values into strings
    # Replacement fields delimited by { and }
    # Integer field names matched with positional arguments
    # Field names can be omitted if used in sequence
    # Named fields are matched with keyword arguments
    # Access values through keys or indexes with square brackets in the replacement field
    # Access attributes using dot in the replacement field
    # The replacement field mini-language provides many value and alignment formatting options


test = "first" "second" # "firstsecond" 
print(test)

print("unforgetable".partition("forget")) # ('un', 'forget', 'able')

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure) # London
print(arrival) # Edinburgh


origin, _, destination = "Seattle-Boston".partition('-')
print(origin) # Seattle
print(destination) # Boston


colors = ';'.join(['#45ff23', '#2321fa'])

''.join(['high', 'way', 'man']) # 'highwayman' fast way of concat

multiline_string = """asdd asd asd sa das dsad \n
    asdasddasdsad sad\ das\  \n
        das\gdfhgfhgf"""

print(multiline_string)

backslash_escape = 'asd das d \\ asdd'

print(backslash_escape)