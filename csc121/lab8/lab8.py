import arcade
import math
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
DEAD_ZONE = 0.02

def background():
    arcade.set_background_color(arcade.color.DARK_VIOLET)
    arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 3, 0,
    arcade.color.DARK_SCARLET)
    arcade.draw_lrtb_rectangle_filled(0, 800, 570 / 3, 0,
    arcade.color.CAPUT_MORTUUM)
    arcade.draw_lrtb_rectangle_filled(0, 800, 550 / 3, 0,
    arcade.color.BISTRE)
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
    texture1 = arcade.load_texture("images/house.png")
    scale = .3
    arcade.draw_texture_rectangle(650, 329, scale * texture1.width,
                                  scale * texture1.height, texture1, 0)
    # Underground tomb
    texture2 = arcade.load_texture("images/coffin.png")
    scale = .1
    arcade.draw_texture_rectangle(170, 70, scale * texture2.width,
                                  scale * texture2.height, texture2, 50)

class Player:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def draw(self):
        """ Draw the object with the instance variables we have. """
        arcade.draw_rectangle_outline(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the object
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the object hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.sound)

        """ Update the player position"""
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Ghostie Adventure")
        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        self.player_sprite = None


        # Create our ball
        self.player_sprite =  Player(50, 50, 0, 0, 15, arcade.color.CORN)
        #sounds
        self.sound = arcade.load_sound("images/laser.ogg")
        self.click = arcade.load_sound("images/click.ogg")

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        background()
        self.player_sprite.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Mouse button pressed"""
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.click)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

    def update(self, delta_time):
        self.player_sprite.update()


def main():
    window = MyGame()
    arcade.run()


main()
