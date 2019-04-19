# TYPE
print(type(3))

x = 3
print("x =", x, "and is of type:", type(x))

x = 3.145
print("x =", x, "and is of type:", type(x))

x = "Hi there"
print("x =", x, "and is of type:", type(x))

x = True
print("x =", x, "and is of type:", type(x))

x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))

x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))

x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))

x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))

# LISTS
x = [1, 2]
print(x)

x = [1, 2]
print(x)

x[0] = 22
print(x)
    # looping in lists
my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

    # lists in lists
my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)

    # Looping with index and element
for index, value in enumerate(my_list):
    print(index, value)

    # adding to lists
my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)
print("----")
if 8 == 6 or 8 == 7 or 8 == 8:
    print("TRUE")
else: print("False")
print("----")
if 4 + 5 <= 10:
    print("TRUE")
else:
    print("FALSE")
print("----")
value = 10
if value <= 10:
    print("YES")
elif value == 10:
    print("MAYBE")
print("NO")
print("----")
a=0
for i in range(10):
    a += 1
print(a)
print("----")
if 3 < 4:
    print("A")
else:
    print("B")
print("C")
print("----")
if 8 == (6 or 7 or 8):
    print("TRUE")
else:
    print("nope")
print("----")
a = 0
for i in range(10):
    a += 1
    for j in range(10):
        a += 1
print(a)
print("----")
def function(value):
    return value % 2 == 0
print("----")
x = 5
if function(x):
    print('YES')
else:
    print('NO')

for y in range(1, 11):
    print(y)
print("----")
def square(x):
     return x*x

for i in range(4):
    if i%2 == 0:
        print(square(i))
print("----")
if 5 + 5 < 10:
    print("TRUE")

for y in range(4):
    print(y)
print("----")
def square(x):
    return x*x

for i in range(4):
    if i%2 == 0:
        print(square(i))
print("----")
a = 0
for i in range(10):
    a += 1
for j in range(10):
    a += 1
print(a)
print("----")
a = True
if not a:
    print("A")
else:
    print("B")
print("C")
print("----")
a = 0
for i in range(10):
    for j in range(10):
        a += 1
print(a)
print("----")
for y in range(4):
    print("y")
print("----")
for number in [6, 5, 4, 3, 2]:
    print("I have", number, "cookies. I'm going to eat one.")
print("----")
for x in range(4):
    print("Hello")
