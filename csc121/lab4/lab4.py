import arcade
# (position l/r,position up/down,width,height)
# openning window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_ground():
    # Floor
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0,
    arcade.color.CORAL_PINK)

def draw_window():
    # ------Window
    #Outline of outline of window
    arcade.draw_rectangle_filled(550, 500, 320, 150, arcade.color.COFFEE)
    # Lighter part of window
    arcade.draw_rectangle_outline(550, 500, 300, 120, arcade.color. BLACK, 2)
    # Outline of window
    arcade.draw_rectangle_outline(550, 500, 270, 100, arcade.color.BONE, 10)
    # Actual Window
    arcade.draw_rectangle_filled(550, 500, 260, 95, arcade.color.CYBER_GRAPE)

def draw_outside():
    # Snow and moon outside with drawn points
    arcade.draw_circle_filled(625, 505, 30, arcade.color.CREAM)
    arcade.draw_circle_outline(625, 505, 30, arcade.color.CADMIUM_YELLOW, 5)

    point_list = ((565, 470),
                  (565, 480),
                  (460, 470),
                  (525, 526),
                  (450, 530),
                  (430, 500),
                  (648, 490),
                  (600, 460),
                  (610, 542),
                  (676, 460))
    arcade.draw_points(point_list, arcade.color.WHITE, 10)

def draw_snow():
    point_list = ((565, 470),
                  (565, 480),
                  (460, 470),
                  (525, 526),
                  (450, 530),
                  (430, 500),
                  (648, 490),
                  (600, 460),
                  (610, 542),
                  (676, 460))
    arcade.draw_points(point_list, arcade.color.WHITE, 10)

def draw_picture():
    # ------Picture
    arcade.draw_rectangle_filled(90, 500, 70, 90, arcade.color.VIVID_VIOLET)

    texture6 = arcade.load_texture("images/unicornspace.png")
    scale = .10
    arcade.draw_texture_rectangle(90, 499, scale * texture6.width,
                                  scale * texture6.height, texture6, 0)

    texture5 = arcade.load_texture("images/frame.png")
    scale = .16
    arcade.draw_texture_rectangle(90, 500, scale * texture5.width,
                                  scale * texture5.height, texture5, 0)

def draw_dresser():
    # ------Dresser
    # Mirror
    texture8  = arcade.load_texture("images/glass.png")
    scale = .3
    arcade.draw_texture_rectangle(499, 395, scale * texture8.width,
                                  scale * texture8.height, texture8, 0)
    # Foundation
    arcade.draw_rectangle_filled(580, 250, 70, 150, arcade.color.VIVID_VIOLET)
    arcade.draw_rectangle_filled(420, 250, 70, 150, arcade.color.VIVID_VIOLET)
    arcade.draw_rectangle_filled(500, 290, 150, 70, arcade.color.VIVID_VIOLET)

    # Counter
    arcade.draw_rectangle_filled(500, 290, 200, 30, arcade.color.BLACK)
    arcade.draw_rectangle_outline(500, 290, 200, 30, arcade.color.CYBER_GRAPE, 3)

    # Drawers
    arcade.draw_rectangle_outline(580, 200, 45, 30, arcade.color.BLACK, 2)
    arcade.draw_rectangle_outline(420, 200, 45, 30, arcade.color.BLACK, 2)
    arcade.draw_rectangle_outline(580, 250, 45, 30, arcade.color.BLACK, 2)
    arcade.draw_rectangle_outline(420, 250, 45, 30, arcade.color.BLACK, 2)

    # Knobs
    arcade.draw_point(580, 250, arcade.color.CYBER_GRAPE, 6)
    arcade.draw_point(580, 200, arcade.color.CYBER_GRAPE, 6)

    # Mirror Frame
    texture7 = arcade.load_texture("images/mirror.png")
    scale = .3
    arcade.draw_texture_rectangle(499, 395, scale * texture7.width,
                                  scale * texture7.height, texture7, 0)

def draw_mirror():
    # Second Mirror
    texture9 = arcade.load_texture("images/mirror1.png")
    scale = .2
    arcade.draw_texture_rectangle(700, 350, scale * texture9.width,
                                  scale * texture9.height, texture9, 0)

def draw_bed():
    # ------Bed
    # Bed Frame
    arcade.draw_rectangle_filled(100, 125, 715, 50, arcade.color.DEEP_COFFEE)

    # Bed Sheets
    arcade.draw_rectangle_filled(100, 200, 700, 150, arcade.color.CHARM_PINK)

    # Lace
    texture = arcade.load_texture("images/lace.png")
    scale = .08
    arcade.draw_texture_rectangle(131, 108, scale * texture.width,
                                  scale * texture.height, texture, 0)

    # Pillows
    texture3 = arcade.load_texture("images/pinkerpillow.png")
    scale = .08
    arcade.draw_texture_rectangle(50, 300, scale * texture3.width,
                                  scale * texture3.height, texture3, 0)

    texture2 = arcade.load_texture("images/pinkpillow.png")
    scale = .08
    arcade.draw_texture_rectangle(100, 300, scale * texture2.width,
                                  scale * texture2.height, texture2, 0)

def draw_rug():
    # ------Rug
    arcade.draw_ellipse_filled(600, 100, 15, 160, arcade.color.COTTON_CANDY, 90)

def draw_princess(x, y):
    # ------Princess
    texture4 = arcade.load_texture("images/girl.png")
    scale = .7
    arcade.draw_texture_rectangle(260 + x, 300, scale * texture4.width,
                                  scale * texture4.height, texture4, 0)

def draw_couch():
        # -----Couch
        # Couch
        texture10 = arcade.load_texture("images/couch.png")
        scale = .7
        arcade.draw_texture_rectangle(760, 230, scale * texture10.width,
                                      scale * texture10.height, texture10, 0)

def draw_skulls():
    # Skulls
    texture11 = arcade.load_texture("images/skulls.png")
    scale = .2
    arcade.draw_texture_rectangle(757, 170, scale * texture11.width,
                                  scale * texture11.height, texture11, 0)

def draw_cat():
    # ------Cat
    texture12 = arcade.load_texture("images/cat.png")
    scale = .2
    arcade.draw_texture_rectangle(757, 250, scale * texture12.width,
                                  scale * texture12.height, texture12, 0)

def on_draw(delta_time):
    # Draws everything
    arcade.start_render()

    draw_ground()
    draw_window()
    draw_outside()
    draw_snow()
    draw_picture()
    draw_dresser()
    draw_mirror()
    draw_rug()
    draw_bed()
    draw_couch()
    draw_cat()
    draw_skulls()
    draw_princess(on_draw.princess1_x, 300)
    # moving right with positive, large = faster
    on_draw.princess1_x += 1
# starting place
on_draw.princess1_x = 100


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Princess Room")
    # Background
    arcade.set_background_color(arcade.color.BUBBLE_GUM)
    # ------call on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()

if __name__ == '__main__':
    main()
