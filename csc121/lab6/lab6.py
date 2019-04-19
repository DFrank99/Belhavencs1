import arcade

y = 0
x = 0

def draw_section_outlines():
    color = arcade.color.BLACK

    # Bottom squares
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    # Top squares
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)

# Entire box of dots
def draw_section_1():
    for row in range(30):
        for column in range(30):
            # Instead of zero, calculate proper x location using column
            x = 10 * column

            # Instead of zero, calcute proper y location using row
            y = 10 * row

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            print ()
# Box of dots that are black and white
def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 10 * column + 304


            y = 10 * row


            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            if column % 1 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    # Replace "pass" with loop code
    # Use modulus operator and an if statement to select color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x

def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = 10 * column + 603


            y = 10 * row


            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            if row % 1 == 0 and row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = 10 * column + 903


            y = 10 * row


            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    # Use modulus operator and an if statement to select color
    #if ... and ...

def draw_section_5():
    for row in range(30):
        for column in range(row+1):
            x = 10 * row

            y = 10 * column + 304

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    # Do NOT use if statements tp complete 5-8. Manipulate loops Instead


def draw_section_6():
    for column in range(30):
        for row in range(30-column):
            x = 10 * column + 303

            y = 10 * row + 303

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_7():
    for row in range(30):
        for column in range(row+1):
            x = 10 * column + 603

            y = 10 * row + 303

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_8():
    for row in range(30):
        for column in range(row):
            for column in range(30-row):
                x = 10 * column + 903

                y = 10 * row + 303

                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw outlines
    draw_section_outlines()

    # Draw sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__=='__main__':
    main()
