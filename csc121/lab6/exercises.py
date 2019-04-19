def problems():
    for i in range(10):
        print('*', end=' ')
    print()

def print_stars(n):
    for i in range(n):
        print('*', end= ' ')
    print()

def print_rows_of_stars(numbers):
    for n in numbers:
        print_stars(n)

def problem2():
    print_stars(10)
    print_stars(5)
    print_stars(20)

def problem3():
    for i in range(3):
        for j in range(10):
            print('*', end= ' ')
        print()



if __name__ =='__main__':
    problem2()
    problem3()
