# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
# Explanation video: http://youtu.be/pDpNSck2aXQ

# Variables used in the example if statements
a = 4
b = 5
c = 6

# Basic comparisons
if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than than b")

if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

# NOTE: It is very easy to mix when to use == and =.
# Use == if you are asking if they are equal, use =
# if you are assigning a value.
if a == b:
     print("a is equal to b")

# Not equal
if a != b:
    print("a and b are not equal")

# And
if a < b and a < c:
    print("a is less than b and c")

# Non-exclusive or
if a < b or a < c:
    print("a is less than either a or b (or both)")


# Boolean data type. This is legal!
a = True
if a:
      print("a is true")

 50 if not a:
 51     print("a is false")
 52
 53 a = True
 54 b = False
 55
 56 if a and b:
 57     print("a and b are both true")
