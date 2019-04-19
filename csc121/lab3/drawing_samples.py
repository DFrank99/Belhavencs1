"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three of the double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# This is a lingle-line comment
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the and dimensions (width and height)
# Set the window title to "Drawing Example"
arcade.open_window(600, 600, "Drawing Example")

#background colour
# go here -> for colors http://arcade.academy/arcade.color.html
# and https://www.webfx.com/web-design/color-picker/color-chart/
arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

#Ready to Draw
arcade.start_render()

# Drawing code: go here to see what chaped can be drawn
# http://arcade.academy/examples/drawing_primitives.html
#Draw rectangle
# left of 5, right of 35
# Top pf 590, bottom of 570
arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)

# Different way to draw a rectangle
# Center rectangle at (100, 520) with a width of 45 and height of 25
arcade.draw_rectangle_filled(100, 520, 45, 25, arcade.color.BLUSH)

# Rotate a rectangle
# Center rectangle at (200, 520) with a width of 45 and height of 25
# Also, rotate it 45 degrees.
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH, 45)


# Draw a point at (50, 580) that is 5 pixels large
arcade.draw_point(50, 580, arcade.color.RED, 5)

# Draw a line
# Start point of (75, 590)
# End point of (95, 570)
arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)

# Draw a circle outline centered at (140, 580) with a radius of 18 and a line
# width of 3.
arcade.draw_circle_outline(140, 580, 18, arcade.color.WISTERIA, 3)

# Draw a circle centered at (190, 580) with a radius of 18
arcade.draw_circle_filled(190, 580, 18, arcade.color.WISTERIA)

# Draw an ellipse. Center it at (240, 580) with a width of 30 and
# height of 15.
arcade.draw_ellipse_filled(240, 580, 30, 15, arcade.color.AMBER)

# Draw text starting at (10, 450) with a size of 20 points.
arcade.draw_text("Simpson College", 10, 450, arcade.color.BRICK_RED, 20)

# Draw a grid
# Draw vertical lines every 120 pixels
for x in range(0, 601, 120):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

# Draw horizontal lines every 200 pixels
for y in range(0, 601, 200):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)

# Draw a point
arcade.draw_text("draw_point", 3, 405, arcade.color.BLACK, 12)
arcade.draw_point(60, 495, arcade.color.RED, 10)

# Draw a set of points
arcade.draw_text("draw_points", 123, 405, arcade.color.BLACK, 12)
point_list = ((165, 495),
              (165, 480),
              (165, 465),
              (195, 495),
              (195, 480),
              (195, 465))
arcade.draw_points(point_list, arcade.color.ZAFFRE, 10)

# Draw a line
arcade.draw_text("draw_line", 243, 405, arcade.color.BLACK, 12)
arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 3)

# Draw a set of lines
arcade.draw_text("draw_lines", 363, 405, arcade.color.BLACK, 12)
point_list = ((390, 450),
              (450, 450),
              (390, 480),
              (450, 480),
              (390, 510),
              (450, 510)
              )
arcade.draw_lines(point_list, arcade.color.BLUE, 3)

# Draw a line strip
arcade.draw_text("draw_line_strip", 483, 405, arcade.color.BLACK, 12)
point_list = ((510, 450),
              (570, 450),
              (510, 480),
              (570, 480),
              (510, 510),
              (570, 510)
              )
arcade.draw_line_strip(point_list, arcade.color.TROPICAL_RAIN_FOREST, 3)

# Draw a polygon
arcade.draw_text("draw_polygon_outline", 3, 207, arcade.color.BLACK, 9)
point_list = ((30, 240),
              (45, 240),
              (60, 255),
              (60, 285),
              (45, 300),
              (30, 300))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)

# Draw a filled in polygon
arcade.draw_text("draw_polygon_filled", 123, 207, arcade.color.BLACK, 9)
point_list = ((150, 240),
              (165, 240),
              (180, 255),
              (180, 285),
              (165, 300),
              (150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

# Draw an outline of a circle
arcade.draw_text("draw_circle_outline", 243, 207, arcade.color.BLACK, 10)
arcade.draw_circle_outline(300, 285, 18, arcade.color.WISTERIA, 3)

# Draw a filled in circle
arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

# Draw an ellipse outline, and another one rotated
arcade.draw_text("draw_ellipse_outline", 483, 207, arcade.color.BLACK, 10)
arcade.draw_ellipse_outline(540, 273, 15, 36, arcade.color.AMBER, 3)
arcade.draw_ellipse_outline(540, 336, 15, 36,
                            arcade.color.BLACK_BEAN, 3, 45)

# Draw a filled ellipse, and another one rotated
arcade.draw_text("draw_ellipse_filled", 3, 3, arcade.color.BLACK, 10)
arcade.draw_ellipse_filled(60, 81, 15, 36, arcade.color.AMBER)
arcade.draw_ellipse_filled(60, 144, 15, 36,
                           arcade.color.BLACK_BEAN, 45)

# Draw an arc, and another one rotated
arcade.draw_text("draw_arc/filled_arc", 123, 3, arcade.color.BLACK, 10)
arcade.draw_arc_outline(150, 81, 15, 36,
                        arcade.color.BRIGHT_MAROON, 90, 360)
arcade.draw_arc_filled(150, 144, 15, 36,
                       arcade.color.BOTTLE_GREEN, 90, 360, 45)

# Draw an rectangle outline
arcade.draw_text("draw_rect", 243, 3, arcade.color.BLACK, 10)
arcade.draw_rectangle_outline(295, 100, 45, 65,
                              arcade.color.BRITISH_RACING_GREEN)
arcade.draw_rectangle_outline(295, 160, 20, 45,
                              arcade.color.BRITISH_RACING_GREEN, 3, 45)

# Draw a filled in rectangle
arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)

# Load and draw an image to the screen
# Image from kenney.nl asset pack #1
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
texture = arcade.load_texture("images/playerShip1_orange.png")
scale = .6
arcade.draw_texture_rectangle(540, 120, scale * texture.width,
                              scale * texture.height, texture, 0)
arcade.draw_texture_rectangle(540, 60, scale * texture.width,
                              scale * texture.height, texture, 45)

#Finish drawing
arcade.finish_render()

#Keep the window up until manual closing
arcade.run()
