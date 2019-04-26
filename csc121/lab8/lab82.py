""" Lab 8 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

def background():
    arcade.set_background_color(arcade.color.DARK_VIOLET)
    arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 3, 0,
    arcade.color.DARK_SCARLET)
    arcade.draw_lrtb_rectangle_filled(0, 800, 570 / 3, 0,
    arcade.color.CAPUT_MORTUUM)
    # Moon and stars
    arcade.draw_circle_filled(125, 505, 50, arcade.color.CREAM)
    point_list = ((565, 470),
                  (460, 340),
                  (600, 460),
                  (250, 274),
                  (670, 500),
                  (500, 400),
                  (676, 460),
                  (270, 300),
                  (300, 370),
                  (200, 540),
                  (170, 330),
                  (360, 270),
                  (170, 430),
                  (150, 600),
                  (50, 550),
                  (70, 400),
                  (370, 560),
                  (440, 500),
                  (510, 510))
    arcade.draw_points(point_list, arcade.color.WHITE, 10)
    # House
    texture1 = arcade.load_texture("house.png")
    scale = .3
    arcade.draw_texture_rectangle(650, 329, scale * texture1.width,
                                  scale * texture1.height, texture1, 0)
    # Underground tomb
    texture2 = arcade.load_texture("coffin.png")
    scale = .1
    arcade.draw_texture_rectangle(170, 70, scale * texture2.width,
                                  scale * texture2.height, texture2, 50)

def ghost():
    texture0 = arcade.load_texture("ghost.png")
    scale = .2
    arcade.draw_texture_rectangle(50, 50, scale * texture0.width,
                                  scale * texture0.height, texture0, 0)

class ghost:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        arcade.draw_texture_rectangle(self.position_x, self.position_y, self.radius)

    def update(self):
        # Move ghostie
        self.position_y += self.change_y
        self.position_x += self.change_x

        # ghost hitting edge of screen
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    """ Custom Window Class """

    def __init__(self):
        """ Initializer """

        # Call parent class Initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - User Control")
        # No pointer
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.DARK_VIOLET)

    def on_draw(self):
        arcade.start_render()
        self.ghost.draw()

        background()

    def update(self, delta_time):
        self.ghost.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ghost.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ghost.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ghost.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ghost.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ghost.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ghost.change_y = 0

        if self.key:
            if abs(self.key.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.key.x * MOVEMENT_SPEED


def main():
    window = MyGame()
    arcade.run()


main()
