# defining variable, python does not need the variable type
x = 5

# if statetements dont need parentheses and statements end in a colon ":" 
if x == 5:
    # python uses indentation to indicate blocks of code
    # must use comma or str() to print number variables with string
    print("x is ",x)

# example how not to indent and a multiline comment
'''
print("This is okay")
    print("This is not okay")
'''

# single and double quotes are the same in python
print("This is double quotes")
print('This is single quotes')

# variables are CaSe sensitive
a = 55
A = "abcd"
# A isn't going overwrite a

# legal variable names are
smallcake = 1
BIGCAKE = 2
tiny_cake = 3
HUGE_CAKE = 4
_also_cake = 5
stillcake5 = 6

# variable names must start with a letter or the underscore character
# illegal variable names
'''
3cake = 1 # starts with a number
my-cake = 2 # contains dash
this cake = 3 # contains space
'''

# unpacking a collection of data to different variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)