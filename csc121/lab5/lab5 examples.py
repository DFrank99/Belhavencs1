# The i on line 1 is a variable that keeps track of how many times the program
# has looped. It is a new variable and can be named any legal variable name.
# Programmers often use i as for the variable name, because the i is short for
# increment. This variable helps track when the loop should end. The range
# function controls how many times the code in the loop is run. In this case,
# five times.

for i in range(5):
    print("I will not chew gum in class.")

def print_about_gum(repetitions):

    # Loop that many times
    for i in range(repetitions):
        print("I will not chew gum in class.")


def main():
    print_about_gum(10)


main()
